# Case Detector - Quick Start with Docker 🐳

Get the entire application running in **one command**!

## Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed
- [Git](https://git-scm.com/) installed

## Quick Start (5 minutes)

```bash
# 1. Clone the repository
git clone https://github.com/MarcJeff03/case-detector.git
cd case-detector

# 2. Start everything with Docker Compose
docker-compose up

# 3. Open your browser
# - Frontend: http://localhost:8080/login.html
# - Backend API: http://localhost:8000/api/
```

That's it! 🎉

## What Just Happened?

Docker Compose started two services:
- **Backend** (Django): Running on port 8000 with all dependencies (FFmpeg, Tesseract, etc.)
- **Frontend** (Static files): Serving HTML/CSS/JS on port 8000

## First Time Setup

Create a superuser to access the admin panel:

```bash
# Run this after docker-compose up
docker-compose exec backend python manage.py migrate
docker-compose exec backend python manage.py createsuperuser
```

Then login at http://localhost:8000/admin/

## Common Commands

```bash
# Start services
docker-compose up

# Start in background
docker-compose up -d

# View logs
docker-compose logs -f backend

# Stop services
docker-compose down

# Rebuild after code changes
docker-compose up --build

# Access backend shell
docker-compose exec backend python manage.py shell

# Run migrations
docker-compose exec backend python manage.py migrate
```

## Features Included

✅ Audio transcription (Whisper + FFmpeg)
✅ PDF text extraction (Poppler + PyPDF2)
✅ OCR text recognition (Tesseract)
✅ NLP case analysis (PyTorch + Transformers)
✅ Django REST API
✅ Static HTML frontend with Vue.js

## Production Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) for deploying to:
- **Backend**: Render (with Docker)
- **Frontend**: Vercel

## Troubleshooting

**Port already in use?**
```bash
# Change ports in docker-compose.yml
# For example: "8001:8000" instead of "8000:8000"
```

**Permission denied?**
```bash
# On Linux/Mac, you might need:
sudo docker-compose up
```

**Container won't start?**
```bash
# Check logs
docker-compose logs backend

# Rebuild from scratch
docker-compose down -v
docker-compose build --no-cache
docker-compose up
```

## Need Help?

- Check [DEPLOYMENT.md](DEPLOYMENT.md) for detailed documentation
- View logs: `docker-compose logs -f`
- Check running containers: `docker-compose ps`

---

**Happy Coding!** 🚀
