# First we will pull a OS that will hold and run our application
FROM python:3.14.3-slim-bookworm


# Set Environment variables
ENV USER=CodeSandbox \ 
    PYTHONDONTWRITEBYTECODE=1 \ 
    PYTHONUNBUFFERED=1 \
    UV_PROJECT_ENVIRONMENT=/usr/local

# Run system clean and neccessary installation
RUN apt-get update && apt-get install --no-install-recommends -y \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*  \
    && useradd -m -s /bin/bash $USER


# Copy uv from source
COPY --from=ghcr.io/astral-sh/uv:0.11.3 /uv /uvx /bin/

# Create directory
ENV APP_DIR=/home/$USER/src

WORKDIR $APP_DIR

RUN --mount=type=cache,target=/home/$USER/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-dev --no-install-project


COPY pyproject.toml uv.lock ./
COPY src $APP_DIR

RUN --mount=type=cache,target=/home/$USER/.cache/uv \
    uv sync --frozen

ENV PYTHONPATH=$APP_DIR


RUN chown -R "$USER":"$USER" $APP_DIR
USER $USER

EXPOSE 8000

CMD ["gunicorn", "Core.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "4" , "--reload"]