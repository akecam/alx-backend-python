from django.core.management.base import BaseCommand, CommandError
from django.db import connection
from django.conf import settings
from django.core.management.color import color_style
import os


class Command(BaseCommand):
    help = 'Test database connection and display configuration'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.style = color_style()

    def add_arguments(self, parser):
        parser.add_argument(
            '--verbose',
            action='store_true',
            help='Display detailed database information',
        )

    def handle(self, *args, **options):
        self.stdout.write(self.style.HTTP_INFO("=" * 60))
        self.stdout.write(self.style.HTTP_INFO("DATABASE CONNECTION TEST"))
        self.stdout.write(self.style.HTTP_INFO("=" * 60))

        # Display database configuration
        self.test_environment_variables()
        self.test_database_connection(options['verbose'])

    def test_environment_variables(self):
        """Test that all required environment variables are set."""
        self.stdout.write(f"\n{self.style.WARNING('Environment Variables:')}")

        env_vars = {
            'DB_HOST': os.environ.get('DB_HOST', 'Not set'),
            'DB_PORT': os.environ.get('DB_PORT', 'Not set'),
            'DB_NAME': os.environ.get('DB_NAME', 'Not set'),
            'DB_USER': os.environ.get('DB_USER', 'Not set'),
            'DEBUG': os.environ.get('DEBUG', 'Not set'),
        }

        for var, value in env_vars.items():
            self.stdout.write(f"  {var}: {value}")

        # Check password without displaying it
        db_password = os.environ.get('DB_PASSWORD')
        if db_password:
            self.stdout.write(f"  DB_PASSWORD: {'*' * len(db_password)}")
        else:
            self.stdout.write(f"  DB_PASSWORD: Not set")

    def test_database_connection(self, verbose=False):
        """Test the database connection."""
        self.stdout.write(f"\n{self.style.WARNING('Database Configuration:')}")

        db_config = settings.DATABASES['default']
        self.stdout.write(f"  Engine: {db_config.get('ENGINE')}")
        self.stdout.write(f"  Name: {db_config.get('NAME')}")
        self.stdout.write(f"  User: {db_config.get('USER')}")
        self.stdout.write(f"  Host: {db_config.get('HOST')}")
        self.stdout.write(f"  Port: {db_config.get('PORT')}")

        try:
            self.stdout.write(f"\n{self.style.WARNING('Testing connection...')}")

            # Test basic connection
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
                result = cursor.fetchone()

            if result and result[0] == 1:
                self.stdout.write(f"{self.style.SUCCESS('✓ Database connection successful!')}")

                # Get database info
                with connection.cursor() as cursor:
                    cursor.execute("SELECT VERSION()")
                    version = cursor.fetchone()[0]
                    self.stdout.write(f"  MySQL Version: {version}")

                # Check tables
                self.check_tables(verbose)

                self.stdout.write(f"\n{self.style.SUCCESS('🎉 Database is ready!')}")
                self.stdout.write(f"\n{self.style.WARNING('Next steps:')}")
                self.stdout.write("  1. python manage.py migrate")
                self.stdout.write("  2. python manage.py createsuperuser")
                self.stdout.write("  3. python manage.py runserver")

        except Exception as e:
            self.stdout.write(f"{self.style.ERROR('✗ Database connection failed!')}")
            self.stdout.write(f"  Error: {str(e)}")

            self.stdout.write(f"\n{self.style.WARNING('Troubleshooting:')}")
            self.stdout.write("  1. Check if MySQL service is running")
            self.stdout.write("  2. Verify .env file contains correct credentials")
            self.stdout.write("  3. Ensure database and user exist in MySQL")
            self.stdout.write("  4. Check network connectivity to database host")

            raise CommandError('Database connection test failed')

    def check_tables(self, verbose=False):
        """Check existing tables in the database."""
        try:
            with connection.cursor() as cursor:
                cursor.execute("SHOW TABLES")
                tables = cursor.fetchall()

            if tables:
                self.stdout.write(f"\n{self.style.WARNING('Database Tables:')}")
                if verbose:
                    for table in tables:
                        self.stdout.write(f"  ✓ {table[0]}")
                else:
                    self.stdout.write(f"  Found {len(tables)} tables")
                    self.stdout.write("  Use --verbose to see table names")
            else:
                self.stdout.write(f"\n{self.style.NOTICE('No tables found - migrations needed')}")

        except Exception as e:
            self.stdout.write(f"{self.style.ERROR('Could not check tables: ' + str(e))}")
