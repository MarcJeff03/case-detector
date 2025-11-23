"""
Script to transfer data from SQLite to PostgreSQL
Run this script locally before deploying to Render
"""

import os
import sys

def main():
    print("=" * 60)
    print("SQLite to PostgreSQL Data Transfer")
    print("=" * 60)
    
    # Check for DATABASE_URL
    postgres_url = os.environ.get('DATABASE_URL', '')
    
    if not postgres_url or 'postgresql' not in postgres_url:
        print("\n❌ ERROR: DATABASE_URL is not set to PostgreSQL!")
        print("\nPlease set DATABASE_URL environment variable:")
        print("   Windows PowerShell:")
        print('   $env:DATABASE_URL="postgresql://user:password@host:port/dbname"')
        print("\n   Then run this script again.")
        sys.exit(1)
    
    print(f"\n✓ PostgreSQL URL configured")
    
    # Step 1: Export from SQLite
    print("\n" + "=" * 60)
    print("Step 1: Exporting data from SQLite")
    print("=" * 60)
    
    print("\nRemoving DATABASE_URL temporarily to use SQLite...")
    del os.environ['DATABASE_URL']
    
    print("Running dumpdata command...")
    exit_code = os.system('python manage.py dumpdata --natural-foreign --natural-primary --exclude=contenttypes --exclude=auth.permission --indent=2 --output=data_backup.json')
    
    if exit_code != 0:
        print("\n❌ ERROR: Failed to export data from SQLite")
        sys.exit(1)
    
    print("✓ Data exported to: data_backup.json")
    
    # Step 2: Import to PostgreSQL
    print("\n" + "=" * 60)
    print("Step 2: Setting up PostgreSQL database")
    print("=" * 60)
    
    print("\nRestoring DATABASE_URL for PostgreSQL...")
    os.environ['DATABASE_URL'] = postgres_url
    
    print("Running migrations on PostgreSQL...")
    exit_code = os.system('python manage.py migrate --noinput')
    
    if exit_code != 0:
        print("\n❌ ERROR: Failed to run migrations")
        sys.exit(1)
    
    print("✓ PostgreSQL schema created")
    
    print("\n" + "=" * 60)
    print("Step 3: Importing data to PostgreSQL")
    print("=" * 60)
    
    print("\nImporting data from JSON...")
    exit_code = os.system('python manage.py loaddata data_backup.json')
    
    if exit_code != 0:
        print("\n❌ ERROR: Failed to import data")
        sys.exit(1)
    
    print("✓ Data imported to PostgreSQL")
    
    print("\n" + "=" * 60)
    print("✓ Transfer Complete!")
    print("=" * 60)
    print("\nYour data has been successfully transferred to PostgreSQL.")
    print("\nNext steps:")
    print("1. Verify data in PostgreSQL admin panel")
    print("2. Keep data_backup.json as a backup")
    print("3. Deploy to Render with DATABASE_URL environment variable")
    print("\n" + "=" * 60)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Transfer cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        print("\nMake sure:")
        print("1. You're in the backend folder")
        print("2. db.sqlite3 exists")
        print("3. DATABASE_URL is set correctly")
        print("4. PostgreSQL is accessible")
        sys.exit(1)
