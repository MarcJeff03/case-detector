# Deployment Checklist

## ✅ Completed
- [x] PostgreSQL database created on Render
- [x] Migrations ready (19 migrations)
- [x] Code pushed to GitHub
- [x] Auto-admin user creation configured
- [x] PostgreSQL packages added to requirements.txt

## 📋 Deploy to Render (Backend)

### Step 1: Add Environment Variables

Go to your **Render Web Service** → **Environment** and add:

```
DATABASE_URL=postgresql://case_detector_user:A1ynj069x7zcsM1bEH8PhT2Hw23heQtB@dpg-d4hhlb2dbo4c73bfrol0-a/case_detector

ADMIN_USERNAME=admin
ADMIN_EMAIL=admin@example.com
ADMIN_PASSWORD=admin

SECRET_KEY=your-django-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-app.onrender.com
CORS_ALLOWED_ORIGINS=https://case-detector.vercel.app
```

**Important:** 
- Use **Internal Database URL** for DATABASE_URL (not External)
- Replace `your-app.onrender.com` with your actual Render domain
- Replace `your-django-secret-key-here` with a secure secret key

### Step 2: Deploy

1. Click **"Manual Deploy"** → **"Deploy latest commit"**
2. Wait for deployment to complete (5-10 minutes)
3. Check logs for:
   ```
   ✅ Running migrations...
   ✅ Creating default admin user...
   ✅ Starting gunicorn...
   ```

### Step 3: Test Backend

1. Visit: `https://your-app.onrender.com/admin/`
2. Login with:
   - Username: `admin`
   - Password: `admin`
3. ✅ You should see Django admin panel!

---

## 📋 Deploy to Vercel (Frontend)

Your frontend is already configured in `frontend/public/config.js` to auto-detect the environment.

### Step 1: Deploy to Vercel

1. Go to [Vercel Dashboard](https://vercel.com/dashboard)
2. Click **"Add New"** → **"Project"**
3. Import your GitHub repository: `MarcJeff03/case-detector`
4. Configure:
   - **Framework Preset:** Other
   - **Root Directory:** `frontend`
   - **Build Command:** (leave empty)
   - **Output Directory:** `public`
5. Click **"Deploy"**

### Step 2: Test Frontend

1. Visit: `https://case-detector.vercel.app/login.html`
2. Try logging in with admin credentials
3. ✅ Frontend should connect to your Render backend!

---

## 🔧 Troubleshooting

### Backend Issues

**Problem:** Can't connect to PostgreSQL
- Check DATABASE_URL is set correctly (Internal URL)
- Verify PostgreSQL database is running in Render

**Problem:** Admin user not created
- Check logs for `createdefaultuser` command
- Verify ADMIN_USERNAME, ADMIN_EMAIL, ADMIN_PASSWORD are set

**Problem:** Static files not loading
- Whitenoise is configured, should work automatically
- Check `STATIC_ROOT` and `STATIC_URL` in settings.py

### Frontend Issues

**Problem:** CORS errors
- Check CORS_ALLOWED_ORIGINS includes your Vercel URL
- Make sure it starts with `https://`

**Problem:** API calls failing
- Check `config.js` is loaded properly
- Verify Render backend URL is accessible

---

## 🎉 Success Checklist

- [ ] Backend deployed on Render
- [ ] PostgreSQL connected and migrations applied
- [ ] Admin login works at `/admin/`
- [ ] Frontend deployed on Vercel
- [ ] Frontend can connect to backend API
- [ ] CORS working properly

---

## 📝 Next Steps After Deployment

1. **Change admin password** (go to admin panel → Users → admin → change password)
2. **Add your research data** through admin panel
3. **Test all features** (complaints, credibility checks, etc.)
4. **Monitor logs** for any errors
5. **Set up custom domain** (optional)

---

## 🔗 Useful Links

- **Render Dashboard:** https://dashboard.render.com/
- **Vercel Dashboard:** https://vercel.com/dashboard
- **GitHub Repo:** https://github.com/MarcJeff03/case-detector
- **PostgreSQL Database:** Check Render dashboard → PostgreSQL

---

**Ready to deploy!** Start with Step 1: Add Environment Variables to Render.
