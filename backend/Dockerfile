FROM python:3.8.5-slim

# Update apt sources to use Debian archive (for old Buster)
RUN sed -i 's|http://deb.debian.org/debian|http://archive.debian.org/debian|g' /etc/apt/sources.list && \
    sed -i 's|http://security.debian.org/debian-security|http://archive.debian.org/debian-security|g' /etc/apt/sources.list && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        default-libmysqlclient-dev \
        pkg-config \
        poppler-utils \
        tesseract-ocr \
        tesseract-ocr-eng \
        libtesseract-dev \
        libleptonica-dev \
        portaudio19-dev \
        ffmpeg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app

ENV DJANGO_SETTINGS_MODULE=app.settings
RUN python manage.py collectstatic --noinput || true

EXPOSE 8000

# Auto-run migrations and create default user on startup
CMD python manage.py migrate --noinput && \
    python manage.py createdefaultuser && \
    gunicorn app.wsgi:application --bind 0.0.0.0:8000 --workers 1
    