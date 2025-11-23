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

### 2. Deploy to Render

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click **New +** → **Web Service**
3. Connect your GitHub repository
4. Configure:
   - **Name**: `case-detector`
   - **Root Directory**: `backend`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app.wsgi:application`
   - **Instance Type**: Free or Starter

### 3. Set Environment Variables in Render

Add these environment variables in Render dashboard:

```bash
PYTHON_VERSION=3.8.5
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=case-detector.onrender.com,.onrender.com
CORS_ALLOWED_ORIGINS=https://case-detector.vercel.app
```

### 4. Database Migration

After deployment, run in Render shell:
```bash
python manage.py migrate
python manage.py createsuperuser
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
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
```

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
