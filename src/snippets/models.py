import uuid
from django.db import models
from django.db.models import Q
from django.conf import settings
from django.db.models.functions import Lower

from common.models import BaseModel


class OwnershipType(models.TextChoices):
    USER = "USER", "User"
    ANONYMOUS = "ANONYMOUS", "Anonymous"


class Visibility(models.TextChoices):
    PUBLIC = "PUBLIC", "Public"
    UNLISTED = "UNLISTED", "Unlisted"
    PRIVATE = "PRIVATE", "Private"

class VersionType(models.TextChoices):
    AUTO = "AUTO", "auto"
    NAMED = "NAMED", "named"

class SnippetPermissionRole(models.TextChoices):
    VIEWER = "VIEWER", "viewer"
    EDITOR = "EDITOR", "editor"

class ShareAccessType(models.TextChoices):
    VIEW = "VIEW", "view"
    EDIT = "EDIT", "edit"

class InvitationStatus(models.TextChoices):
    PENDING = "PENDING", "Pending"
    ACCEPTED = "ACCEPTED", "Accepted"
    EXPIRED = "EXPIRED", "Expired"
    REVOKED = "REVOKED", "Revoked"


class Snippet(BaseModel):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="snippets",
    )
    ownership_type = models.CharField(
        max_length=20,
        choices=OwnershipType.choices,
        default=OwnershipType.USER,
    )
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    visibility = models.CharField(
        max_length=20,
        choices=Visibility.choices,
        default=Visibility.PRIVATE,
    )
    language = models.CharField(max_length=30, blank=True)
    current_version = models.ForeignKey(
        "SnippetVersion",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="current_for_snippets",
    )
    expires_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "snippets"
        constraints = [
            models.CheckConstraint(
                condition=(
                    Q(ownership_type=OwnershipType.USER, owner__isnull=False)
                    | Q(ownership_type=OwnershipType.ANONYMOUS, owner__isnull=True)
                ),
                name="snippet_owner_matches_ownership_type",
            ),
        ]


class AnonymousOwnership(BaseModel):
    snippet = models.OneToOneField(
        Snippet,
        on_delete=models.CASCADE,
        related_name="anonymous_ownership",
    )
    credential_hash = models.CharField(max_length=128, unique=True)
    revoked_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "anonymous_ownership"


class SnippetVersion(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid7,
        editable=False
    )
    snippet = models.ForeignKey(
        Snippet,
        on_delete=models.CASCADE,
        related_name="versions",
    )
    version_number = models.PositiveIntegerField()
    content = models.TextField()
    content_hash = models.CharField(max_length=64)
    version_type = models.CharField(
        max_length=20,
        choices=VersionType.choices,
        default=VersionType.AUTO
    )
    version_name = models.CharField(max_length=100, null=True, blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='created_snippet_versions'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "snippet_versions"
        constraints = [
            models.UniqueConstraint(
                fields=["snippet", "version_number"],
                name="unique_version_number_per_snippet",
            ),
            models.CheckConstraint(
                condition=(
                    Q(version_type=VersionType.AUTO, version_name__isnull=True)
                    | (
                        Q(version_type=VersionType.NAMED)
                        & Q(version_name__isnull=False)
                        & ~Q(version_name="")
                    )
                ),
                name="valid_snippet_version_name",
            ),
            models.CheckConstraint(
                condition=models.Q(version_number__gt=0),
                name="snippet_version_number_positive",
            ),
        ]


class SnippetPermission(BaseModel):
    snippet = models.ForeignKey(
        Snippet,
        on_delete=models.CASCADE,
        related_name="permissions",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="snippet_permissions",
    )
    role = models.CharField(
        max_length=20,
        choices=SnippetPermissionRole.choices,
        default=SnippetPermissionRole.VIEWER,
    )
    revoked_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "snippet_permissions"
        constraints = [
            models.UniqueConstraint(
                fields=["snippet", "user"],
                condition=Q(revoked_at__isnull=True),
                name="unique_active_snippet_permission",
            )
        ]


class SnippetShareLink(BaseModel):
    snippet = models.ForeignKey(
        Snippet,
        on_delete=models.CASCADE,
        related_name="share_links",
    )
    token_hash = models.CharField(max_length=255, unique=True)
    access_type = models.CharField(
        max_length=10,
        choices=ShareAccessType.choices,
    )
    expires_at = models.DateTimeField(null=True, blank=True)
    max_uses = models.PositiveIntegerField(null=True, blank=True)
    use_count = models.PositiveIntegerField(default=0)

    revoked_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='created_snippet_share_links'
    )

    class Meta:
        db_table = "snippet_share_links"
        constraints = [
            models.UniqueConstraint(
                fields=["snippet"],
                condition=Q(revoked_at__isnull=True),
                name="unique_active_share_link_per_snippet",
            ),
            models.CheckConstraint(
                condition=Q(max_uses__isnull=True) | Q(max_uses__gt=0),
                name="share_link_max_uses_positive",
            ),
            models.CheckConstraint(
                condition=(
                    Q(max_uses__isnull=True)
                    | Q(use_count__lte=models.F("max_uses"))
                ),
                name="share_link_use_count_within_limit",
            )
        ]


class SnippetInvitation(BaseModel):
    snippet = models.ForeignKey(
        Snippet,
        on_delete=models.CASCADE,
        related_name="invitations",
    )
    email = models.EmailField()
    role = models.CharField(
        max_length=20,
        choices=SnippetPermissionRole.choices,
        default=SnippetPermissionRole.VIEWER,
    )
    token_hash = models.CharField(max_length=128, unique=True)
    status = models.CharField(
        max_length=20,
        choices=InvitationStatus.choices,
        default=InvitationStatus.PENDING,
    )
    expires_at = models.DateTimeField()
    accepted_at = models.DateTimeField(null=True, blank=True)
    invited_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="sent_snippet_invitations",
    )

    class Meta:
        db_table = "snippet_invitations"
        constraints = [
            models.UniqueConstraint(
                Lower("email"),
                "snippet",
                condition=Q(status=InvitationStatus.PENDING),
                name="unique_pending_invitation_per_snippet_email",
            )
        ]