import os
from pathlib import Path

import environ


PROJECT_ROOT = Path(__file__).resolve().parents[2]


def initialize_environment():
    """
    Initialize environment variables before Django loads settings.

    Local development:
        Load variables from the project-root .env file.

    Production:
        Use environment variables injected by the deployment platform.
    """

    environment = os.environ.get("ENVIRONMENT")

    # Load .env only when not explicitly running in production.
    if environment != "production":
        env_file = PROJECT_ROOT / ".env"

        if env_file.is_file():
            environ.Env.read_env(
                env_file=env_file,
                overwrite=False,
            )

    environment = os.environ.get("ENVIRONMENT", "development")

    if environment == "production":
        settings_module = os.environ.get("DJANGO_SETTINGS_MODULE")

        if settings_module != "config.settings.prod":
            raise RuntimeError(
                "Production requires DJANGO_SETTINGS_MODULE="
                "'config.settings.prod'"
            )

    else:
        os.environ.setdefault(
            "DJANGO_SETTINGS_MODULE",
            "config.settings.dev",
        )