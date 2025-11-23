# SQLite to PostgreSQL Migration Guide

This guide shows you how to transfer all your existing SQLite data to PostgreSQL.

## Prerequisites

1. Your current SQLite database (`db.sqlite3`) with all your data
2. A PostgreSQL database created on Render (or locally)
3. Python virtual environment activated

## Step-by-Step Instructions

### Option 1: Using the Transfer Script (Recommended)

#### 1. Create PostgreSQL Database on Render

**Note**: This is a SEPARATE database service, NOT a new web service. Your existing backend web service will connect to this database.

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click **New +** → **PostgreSQL** (NOT Web Service!)
3. Configure:
   - **Name**: `case-detector-db`
   - **Database**: `case_detector`
   - **User**: (auto-generated)
   - **Region**: Same as your web service
   - **Instance Type**: **Free** (256MB storage)
4. Click **Create Database**
5. Wait for it to provision (takes 1-2 minutes)
6. Copy the **Internal Database URL** from the database info page
   - It looks like: `postgresql://user:pass@dpg-xxx.oregon-postgres.render.com/dbname`

#### 2. Set DATABASE_URL Environment Variable

**Windows PowerShell:**
```powershell
cd backend
$env:DATABASE_URL="paste-your-postgresql-url-here"
```

**Windows CMD:**
```cmd
cd backend
set DATABASE_URL=postgresql://case_detector_user:A1ynj069x7zcsM1bEH8PhT2Hw23heQtB@dpg-d4hhlb2dbo4c73bfrol0-a/case_detector
```

**Linux/Mac:**
```bash
cd backend
export DATABASE_URL="paste-your-postgresql-url-here"
```

#### 3. Install PostgreSQL Package

```powershell
pip install psycopg2-binary dj-database-url
```

#### 4. Run Transfer Script

```powershell
python transfer_data.py
```

The script will:
- ✅ Export all data from SQLite to `data_backup.json`
- ✅ Create PostgreSQL schema (run migrations)
- ✅ Import all data into PostgreSQL
- ✅ Show success message

#### 5. Verify Data Transfer

Start Django with PostgreSQL:
```powershell
python manage.py runserver
```

Visit http://localhost:8000/admin/ and verify:
- Users exist
- Papers/documents are there
- Complaints are present
- All data looks correct

### Option 2: Manual Method

If the script doesn't work, use Django's built-in commands:

#### 1. Export from SQLite

Make sure `DATABASE_URL` is NOT set (using SQLite):
```powershell
cd backend
python manage.py dumpdata --natural-foreign --natural-primary --exclude=contenttypes --exclude=auth.permission --indent=2 --output=data_backup.json
```

#### 2. Switch to PostgreSQL

Set DATABASE_URL:
```powershell
$env:DATABASE_URL="postgresql://user:pass@host/dbname"
```

#### 3. Create Schema

```powershell
python manage.py migrate --noinput
```

#### 4. Import Data

```powershell
python manage.py loaddata data_backup.json
```

## Troubleshooting

### Error: "cannot import name 'dj_database_url'"

Install the package:
```powershell
pip install dj-database-url
```

### Error: "could not connect to server"

Check your DATABASE_URL:
- Make sure it's the **Internal Database URL** from Render
- Verify the database is running in Render dashboard
- Try connecting with a PostgreSQL client to test

### Error: "relation does not exist"

Run migrations first:
```powershell
python manage.py migrate
```

### Error: "duplicate key value"

Your PostgreSQL database already has data. Either:
- Drop and recreate the database
- Or use `--ignorenonexistent` flag:
  ```powershell
  python manage.py loaddata --ignorenonexistent data_backup.json
  ```

## Deploy to Render

Once data is transferred successfully:

1. Push your code to GitHub:
   ```powershell
   git add -A
   git commit -m "Add PostgreSQL configuration"
   git push origin main
   ```

2. In Render Web Service, add environment variable:
   ```
   DATABASE_URL=your-postgresql-internal-url
   ```

3. Deploy - your data will already be in PostgreSQL!

## Backup

Keep `data_backup.json` as a backup:
- Store it safely (not in git repository)
- You can restore anytime with: `python manage.py loaddata data_backup.json`

## Notes

- **Media files** (uploaded PDFs, images) are NOT transferred by this script
- You'll need to upload media files separately to Render Disk or S3
- The admin user password will be transferred (you can login with existing credentials)

---

**Need Help?** Check the script output for specific error messages.
