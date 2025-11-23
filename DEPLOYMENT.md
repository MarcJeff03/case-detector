# Deployment Guide: Render (Backend) + Vercel (Frontend)

This guide explains how to deploy the Case Detector application with the backend on Render and frontend on Vercel.

## Architecture

- **Backend (Django)**: Deployed on Render at `https://case-detector.onrender.com`
- **Frontend (Static HTML)**: Deployed on Vercel at `https://case-detector.vercel.app`
- **Communication**: Frontend makes API calls to backend via CORS

## Backend Deployment (Render)

### 1. Prepare Backend

The backend is already configured in `backend/` folder with:
- Django REST Framework
- CORS enabled for Vercel domain
- Session/CSRF cookies configured for cross-origin
- **Dockerfile** ready for containerized deployment

### 2. Deploy to Render (Choose Option A or B)

#### Option A: Docker Deployment (Recommended ✅)

Docker provides consistent environments and includes all dependencies (FFmpeg, Tesseract, etc.).

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click **New +** → **Web Service**
3. Connect your GitHub repository
4. Configure:
   - **Name**: `case-detector`
   - **Root Directory**: `backend`
   - **Environment**: **Docker**
   - **Dockerfile Path**: `backend/Dockerfile`
   - **Docker Build Context Directory**: `backend`
   - **Instance Type**: Free or Starter

Render will automatically:
- Build the Docker image from your Dockerfile
- Install all system dependencies (FFmpeg, Tesseract, Poppler)
- Run `gunicorn` on port 8000

#### Option B: Native Python Deployment

Without Docker (requires manual dependency setup):

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click **New +** → **Web Service**
3. Connect your GitHub repository
4. Configure:
   - **Name**: `case-detector`
   - **Root Directory**: `backend`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app.wsgi:application --bind 0.0.0.0:8000`
   - **Instance Type**: Free or Starter

⚠️ **Note**: Audio transcription won't work without FFmpeg. You'll need to add build commands to install system dependencies.

### 3. Set Environment Variables in Render

Add these environment variables in Render dashboard:

```bash
PYTHON_VERSION=3.8.5
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=case-detector.onrender.com,.onrender.com
CORS_ALLOWED_ORIGINS=https://case-detector.vercel.app

# Database - PostgreSQL (Required for persistent data)
DATABASE_URL=your-postgresql-connection-string

# Admin user credentials (auto-created on first deploy)
ADMIN_USERNAME=admin
ADMIN_EMAIL=admin@example.com
ADMIN_PASSWORD=your-secure-password
```

**How to get DATABASE_URL:**
1. In Render dashboard, click **New +** → **PostgreSQL**
2. Name it (e.g., `case-detector-db`)
3. Select **Free** tier
4. Click **Create Database**
5. Copy the **Internal Database URL**
6. Paste it as `DATABASE_URL` in your Web Service environment variables

### 4. Database Migration

**✅ Migrations run automatically on every deployment!**

The Dockerfile is already configured to:
1. Run database migrations: `python manage.py migrate --noinput`
2. Create default admin user: `python manage.py createdefaultuser`
3. Start the server: `gunicorn app.wsgi:application`

**✅ PostgreSQL is Now Configured!**

The project is set up to use PostgreSQL automatically when you provide the `DATABASE_URL` environment variable. Your data will persist across restarts!

**What You Get:**
- ✅ **Persistent data** - Users, papers, complaints survive restarts
- ✅ **Production-ready** - Better performance and reliability
- ✅ **Free tier** - Render's PostgreSQL free tier is sufficient for testing
- ✅ **Automatic fallback** - Uses SQLite for local development if no DATABASE_URL

**Access Admin Panel:**
- URL: `https://case-detector.onrender.com/admin/`
- Username: `admin` (or your ADMIN_USERNAME)
- Password: Your ADMIN_PASSWORD

### 5. Why Use Docker? 🐳

**Advantages:**
- ✅ **Consistent environment**: Same setup locally and in production
- ✅ **All dependencies included**: FFmpeg, Tesseract, Poppler automatically installed
- ✅ **Faster debugging**: If it works locally, it works in production
- ✅ **Easy rollback**: Version control for entire environment
- ✅ **Isolation**: No conflicts with system packages

**What's in the Dockerfile:**
```dockerfile
FROM python:3.8.5-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg              # For audio transcription
    tesseract-ocr       # For OCR text extraction
    poppler-utils       # For PDF processing
    
# Install Python dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Run gunicorn
CMD ["gunicorn", "app.wsgi:application", "--bind", "0.0.0.0:8000"]
```

## Frontend Deployment (Vercel)

### 1. Prepare Frontend

The frontend is configured with:
- `config.js` - Auto-detects environment and uses correct backend URL
- All HTML files load `config.js` for API configuration
- `vercel.json` - Routing and static file configuration

### 2. Deploy to Vercel

#### Option A: Using Vercel CLI

```bash
# Install Vercel CLI
npm install -g vercel

# Login to Vercel
vercel login

# Deploy
cd case-detector-main
vercel --prod
```

#### Option B: Using Vercel Dashboard

1. Go to [Vercel Dashboard](https://vercel.com/dashboard)
2. Click **Import Project**
3. Connect your GitHub repository
4. Configure:
   - **Framework Preset**: Other
   - **Root Directory**: `./`
   - **Build Command**: (leave empty)
   - **Output Directory**: `frontend/public`

5. Deploy!

### 3. Configure Custom Domain (Optional)

In Vercel dashboard:
1. Go to project **Settings** → **Domains**
2. Add `case-detector.vercel.app` or your custom domain

## Testing the Connection

### 1. Test Backend (Render)

```bash
# Test backend is running
curl https://case-detector.onrender.com/api/

# Test CORS headers
curl -H "Origin: https://case-detector.vercel.app" \
     -H "Access-Control-Request-Method: POST" \
     -X OPTIONS \
     https://case-detector.onrender.com/authenticate_user/
```

### 2. Test Frontend (Vercel)

1. Visit `https://case-detector.vercel.app/login.html`
2. Open browser DevTools → Console
3. You should see: `🔧 API Configuration: { API_BASE_URL: 'https://case-detector.onrender.com', environment: 'production' }`
4. Try logging in - it should connect to Render backend

## Configuration Files

### `backend/app/settings.py`
```python
# CORS configuration for Vercel frontend
CORS_ALLOWED_ORIGINS = ['https://case-detector.vercel.app']
CORS_ALLOW_CREDENTIALS = True

# CSRF trusted origins
CSRF_TRUSTED_ORIGINS = [
    'https://case-detector.vercel.app',
    'https://case-detector.onrender.com',
]

# Session cookies for cross-origin
SESSION_COOKIE_SAMESITE = 'None'
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = 'None'
CSRF_COOKIE_SECURE = True
```

### `frontend/public/config.js`
```javascript
// Auto-detects environment:
// - Production (Vercel): uses https://case-detector.onrender.com
// - Development (localhost): uses http://localhost:8000
const API_BASE_URL = (hostname === 'case-detector.vercel.app') 
    ? 'https://case-detector.onrender.com' 
    : window.location.origin;
```

### `vercel.json`
```json
{
  "routes": [
    { "src": "/static/(.*)", "dest": "/frontend/public/static/$1" },
    { "src": "/config.js", "dest": "/frontend/public/config.js" },
    { "src": "/(.*)\\.html", "dest": "/frontend/public/$1.html" }
  ]
}
```

## Troubleshooting

### Issue: CORS Error

**Problem**: `Access-Control-Allow-Origin` error in browser console

**Solution**:
1. Check Render environment variable: `CORS_ALLOWED_ORIGINS=https://case-detector.vercel.app`
2. Ensure no trailing slashes in URLs
3. Verify `corsheaders` is in `INSTALLED_APPS` before `CommonMiddleware`

### Issue: CSRF Token Missing

**Problem**: `403 Forbidden` on POST requests

**Solution**:
1. Ensure cookies are being sent: `credentials: 'include'` in fetch
2. Check CSRF cookie settings in `settings.py`:
   - `CSRF_COOKIE_SAMESITE = 'None'`
   - `CSRF_COOKIE_SECURE = True`
3. Add Vercel domain to `CSRF_TRUSTED_ORIGINS`

### Issue: Static Files Not Loading

**Problem**: CSS/JS files return 404

**Solution**:
1. Verify `vercel.json` routes for `/static/` path
2. Check file paths in HTML: should be `/static/app/...`
3. Ensure files exist in `frontend/public/static/`

### Issue: Authentication Not Persisting

**Problem**: User gets logged out immediately

**Solution**:
1. Check session cookie settings:
   - `SESSION_COOKIE_SAMESITE = 'None'`
   - `SESSION_COOKIE_SECURE = True`
2. Verify `CORS_ALLOW_CREDENTIALS = True`
3. Ensure frontend sends `credentials: 'include'`

## Local Development

### Backend (Django)

#### Option A: Using Docker (Recommended)
```bash
cd backend

# Build the Docker image
docker build -t case-detector-backend .

# Run the container
docker run -p 8000:8000 \
  -e DEBUG=True \
  -e ALLOWED_HOSTS=localhost,127.0.0.1 \
  -v $(pwd)/db.sqlite3:/app/db.sqlite3 \
  -v $(pwd)/media:/app/media \
  case-detector-backend

# Or use docker-compose (easier!)
cd ..  # Go to project root
docker-compose up
```

**Using docker-compose.yml** (included in project):
```bash
# Start both backend and frontend
docker-compose up

# Or run in background
docker-compose up -d

# View logs
docker-compose logs -f backend

# Stop services
docker-compose down
```

Access:
- Backend: http://localhost:8000
- Frontend: http://localhost:8080/login.html

#### Option B: Native Python
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
```

⚠️ **Note**: Audio transcription requires FFmpeg installed on your system.

### Frontend (Static Files)
```bash
cd frontend/public
python -m http.server 8080
# Visit http://localhost:8080/login.html
```

Or open `frontend/public/login.html` directly in browser (Django backend must be running on localhost:8000)

## Security Checklist

- [ ] `DEBUG = False` in production (Render)
- [ ] Strong `SECRET_KEY` set in Render environment variables
- [ ] HTTPS enforced on both Render and Vercel
- [ ] CORS restricted to specific origins (no wildcards)
- [ ] CSRF protection enabled
- [ ] Secure cookies: `SameSite=None; Secure`
- [ ] Database backups configured on Render
- [ ] Media files stored in persistent storage (Render Disk or S3)

## Docker vs Native Python

| Feature | Docker 🐳 | Native Python 🐍 |
|---------|----------|------------------|
| Setup complexity | Low (one command) | Medium (manual deps) |
| System dependencies | ✅ Included (FFmpeg, Tesseract) | ❌ Manual install |
| Consistency | ✅ Same everywhere | ⚠️ OS-dependent |
| Audio transcription | ✅ Works out of box | ❌ Requires FFmpeg |
| PDF processing | ✅ Works out of box | ❌ Requires Poppler |
| Deployment | ✅ Click & deploy | ⚠️ Build commands needed |
| Performance | Good | Slightly better |
| Best for | Production, Teams | Solo dev, Simple projects |

**Recommendation**: Use Docker for Render deployment to ensure all features work (especially audio transcription and PDF processing).

## Monitoring

### Render Logs
```bash
# View logs in Render dashboard
# Or use Render CLI:
render logs -s case-detector
```

### Vercel Logs
```bash
# View logs in Vercel dashboard
# Or use Vercel CLI:
vercel logs case-detector
```

## Support

For issues, check:
- Render Logs: https://dashboard.render.com/
- Vercel Logs: https://vercel.com/dashboard
- Browser DevTools Console: F12 → Console tab
- Network Tab: Check API request/response headers

---

Last Updated: 2025-11-23
