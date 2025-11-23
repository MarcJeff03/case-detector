"""
Script to transfer data from SQLite to PostgreSQL
Run this script locally before deploying to Render
"""

import os
import sys
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from django.core.management import call_command
from django.db import connection

def transfer_data():
    """
    Transfer data from SQLite to PostgreSQL
    
    Instructions:
    1. Make sure you have your SQLite database (db.sqlite3) in the backend folder
    2. Set DATABASE_URL environment variable to your PostgreSQL connection string
    3. Run this script: python transfer_data.py
    """
    
    print("=" * 60)
    print("SQLite to PostgreSQL Data Transfer")
    print("=" * 60)
    
    # Check current database
    db_engine = connection.settings_dict['ENGINE']
    print(f"\n✓ Current database engine: {db_engine}")
    
    if 'postgresql' not in db_engine and 'psycopg' not in db_engine:
        print("\n❌ ERROR: DATABASE_URL is not set to PostgreSQL!")
        print("\nPlease set DATABASE_URL environment variable:")
        print("   Windows PowerShell:")
        print('   $env:DATABASE_URL="postgresql://user:password@host:port/dbname"')
        print("\n   Then run this script again.")
        sys.exit(1)
    
    print("\n" + "=" * 60)
    print("Step 1: Exporting data from SQLite")
    print("=" * 60)
    
    # Export data to JSON
    print("\nExporting all data to JSON fixture...")
    call_command('dumpdata', 
                 '--natural-foreign', 
                 '--natural-primary',
                 '--exclude=contenttypes',
                 '--exclude=auth.permission',
                 '--indent=2',
                 '--output=data_backup.json')
    
    print("✓ Data exported to: data_backup.json")
    
    print("\n" + "=" * 60)
    print("Step 2: Setting up PostgreSQL database")
    print("=" * 60)
    
    # Run migrations on PostgreSQL
    print("\nRunning migrations on PostgreSQL...")
    call_command('migrate', '--noinput')
    print("✓ PostgreSQL schema created")
    
    print("\n" + "=" * 60)
    print("Step 3: Importing data to PostgreSQL")
    print("=" * 60)
    
    # Load data into PostgreSQL
    print("\nImporting data from JSON...")
    call_command('loaddata', 'data_backup.json')
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
        transfer_data()
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        print("\nIf you see 'cannot import name' errors, make sure:")
        print("1. You're in the backend folder")
        print("2. DATABASE_URL is set correctly")
        print("3. PostgreSQL is accessible")
        sys.exit(1)
