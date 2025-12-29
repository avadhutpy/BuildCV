# syntax=docker/dockerfile:1

FROM python:3.13.9-alpine3.21

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=utf-8

WORKDIR /app

# Install runtime & build dependencies. Use virtual .build-deps so we can remove build tools after pip install.
# Note: some libraries are required for building wheels; others are runtime libs needed by packages like WeasyPrint.

RUN apk update && \
    apk add --no-cache --virtual .build-deps \
    build-base \
    python3-dev \
    libffi-dev \
    openssl-dev \
    zlib-dev \
    pkgconfig \
    postgresql-dev \
    cargo

RUN apk add --no-cache \
    bash \
    curl \
    ca-certificates \
    libjpeg-turbo-dev \
    libpng-dev \
    tiff-dev \
    libwebp-dev \
    libxml2-dev \
    libxslt-dev \
    freetype-dev \
    fontconfig \
    ttf-dejavu \
    cairo-dev \
    pango-dev \
    harfbuzz-dev \
    gdk-pixbuf-dev \
    shared-mime-info


RUN apk add --no-cache weasyprint \
    py3-pip \
    so:libgobject-2.0.so.0 \
    so:libpango-1.0.so.0 \
    so:libharfbuzz.so.0 \
    so:libharfbuzz-subset.so.0 \
    so:libfontconfig.so.1 \
    so:libpangoft2-1.0.so.0



# Copy requirements and install python deps
COPY requirements.txt /app/requirements.txt

# Upgrade pip, then install requirements (no cache)
RUN pip install --upgrade pip setuptools wheel \
    && pip wheel --no-cache-dir --wheel-dir /wheels -r /app/requirements.txt \
    && pip install --no-cache-dir --no-index --find-links /wheels -r /app/requirements.txt

# Remove build deps to reduce image size
RUN apk del .build-deps \
    && rm -rf /wheels /root/.cache

# Copy application source
COPY . /app

# Expose port and add a simple healthcheck (uses curl)

# Default command (adjust to your preferred production start: gunicorn/uvicorn, etc.)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]