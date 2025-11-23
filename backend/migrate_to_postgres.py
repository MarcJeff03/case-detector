"""
Simple script to migrate from SQLite to PostgreSQL
"""
import os
import sys
import subprocess

# Get PostgreSQL URL
postgres_url = os.environ.get('DATABASE_URL', '')

if not postgres_url or 'postgresql' not in postgres_url:
    print("❌ ERROR: Please set DATABASE_URL environment variable to PostgreSQL connection string")
    sys.exit(1)

print("=" * 60)
print("Data Migration: SQLite → PostgreSQL")
print("=" * 60)

# Step 1: Export from SQLite
print("\n[1/3] Exporting from SQLite...")
if 'DATABASE_URL' in os.environ:
    del os.environ['DATABASE_URL']

result = subprocess.run([
    sys.executable, 'manage.py', 'dumpdata',
    '--natural-foreign',
    '--natural-primary',
    '--exclude=contenttypes',
    '--exclude=auth.permission',
    '--indent=2'
], capture_output=True, text=False)  # Use binary mode

if result.returncode != 0:
    print(f"❌ Export failed: {result.stderr.decode('utf-8', errors='ignore')}")
    sys.exit(1)

# Save to file
with open('migration_data.json', 'wb') as f:
    f.write(result.stdout)

print(f"✅ Exported {len(result.stdout)} bytes")

# Step 2: Run migrations on PostgreSQL
print("\n[2/3] Setting up PostgreSQL schema...")
os.environ['DATABASE_URL'] = postgres_url

result = subprocess.run([
    sys.executable, 'manage.py', 'migrate', '--noinput'
], capture_output=True, text=True)

if result.returncode != 0:
    print(f"❌ Migrations failed: {result.stderr}")
    sys.exit(1)

print("✅ Schema created")

# Step 3: Import to PostgreSQL
print("\n[3/3] Importing data to PostgreSQL...")

result = subprocess.run([
    sys.executable, 'manage.py', 'loaddata', 'migration_data.json'
], capture_output=True, text=False)  # Use binary mode

if result.returncode != 0:
    print(f"❌ Import failed:")
    print(result.stderr.decode('utf-8', errors='ignore'))
    sys.exit(1)

print("✅ Data imported successfully!")

print("\n" + "=" * 60)
print("✅ Migration Complete!")
print("=" * 60)
print("\nYour data has been transferred to PostgreSQL.")
print("You can now deploy to Render with DATABASE_URL set.")
print("=" * 60)
