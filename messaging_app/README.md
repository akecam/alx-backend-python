# Messaging App - Docker Setup

This Django messaging application is configured to run with Docker Compose using MySQL as the database.

## Prerequisites

- Docker and Docker Compose installed on your system
- Git (for cloning the repository)

## Quick Start

1. **Clone the repository and navigate to the project directory:**
   ```bash
   git clone <your-repo-url>
   cd messaging_app
   ```

2. **Create your environment file:**
   ```bash
   cp .env.example .env
   ```

3. **Edit the `.env` file with your preferred values:**
   ```bash
   nano .env  # or use your preferred editor
   ```

4. **Build and start the containers:**
   ```bash
   docker-compose up --build
   ```

5. **Access the application:**
   - Web application: http://localhost:8000
   - MySQL database: localhost:3306

## Environment Variables

The application uses the following environment variables (defined in `.env`):

### Database Configuration
- `MYSQL_ROOT_PASSWORD`: MySQL root password
- `MYSQL_DATABASE`: Name of the MySQL database
- `MYSQL_USER`: MySQL user for the application
- `MYSQL_PASSWORD`: MySQL password for the application user

### Django Configuration
- `DB_HOST`: Database host (should be 'db' for Docker Compose)
- `DB_PORT`: Database port (default: 3306)
- `DB_NAME`: Database name (should match MYSQL_DATABASE)
- `DB_USER`: Database user (should match MYSQL_USER)
- `DB_PASSWORD`: Database password (should match MYSQL_PASSWORD)
- `DEBUG`: Django debug mode (True/False)
- `SECRET_KEY`: Django secret key

## Docker Services

### Web Service (`web`)
- **Image**: Built from the local Dockerfile
- **Port**: 8000 (mapped to host port 8000)
- **Dependencies**: MySQL database service
- **Features**:
  - Automatically runs migrations on startup
  - Hot-reloading enabled for development
  - Waits for database to be ready before starting

### Database Service (`db`)
- **Image**: MySQL 8.0
- **Port**: 3306 (mapped to host port 3306)
- **Persistent Storage**: MySQL data is stored in a Docker volume
- **Configuration**: Uses environment variables from `.env` file

## Common Commands

### Start the services:
```bash
docker-compose up
```

### Start in background (detached mode):
```bash
docker-compose up -d
```

### Stop the services:
```bash
docker-compose down
```

### View logs:
```bash
# All services
docker-compose logs

# Specific service
docker-compose logs web
docker-compose logs db
```

### Execute commands in containers:
```bash
# Django management commands
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic

# Access MySQL shell
docker-compose exec db mysql -u root -p
```

### Rebuild containers after code changes:
```bash
docker-compose up --build
```

## Database Management

### Creating a Superuser
```bash
docker-compose exec web python manage.py createsuperuser
```

### Running Migrations
```bash
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```

### Accessing MySQL Database
```bash
# Using Docker
docker-compose exec db mysql -u messaging_user -p messaging_db

# From host (if MySQL client is installed)
mysql -h localhost -P 3306 -u messaging_user -p messaging_db
```

## Development Workflow

1. **Make code changes** in your local files
2. **Code is automatically synced** to the container via volume mount
3. **Django auto-reloads** when code changes are detected
4. **Database changes persist** in the Docker volume

## Troubleshooting

### Database Connection Issues
- Ensure the database service is running: `docker-compose ps`
- Check database logs: `docker-compose logs db`
- Verify environment variables in `.env` file

### Port Conflicts
- If ports 8000 or 3306 are already in use, modify the port mappings in `docker-compose.yml`

### Permission Issues
- Ensure the `wait-for-it.sh` script is executable: `chmod +x wait-for-it.sh`

### Fresh Database Start
```bash
# Stop services and remove volumes
docker-compose down -v

# Start fresh
docker-compose up --build
```

## Security Notes

- **Never commit** your `.env` file to version control
- **Change default passwords** in production
- **Use strong passwords** for database users
- **Review and update** the Django SECRET_KEY for production

## Production Deployment

For production deployment, consider:
- Using environment-specific `.env` files
- Setting up proper SSL/TLS certificates
- Configuring proper backup strategies for the database
- Using external database services
- Implementing proper logging and monitoring

## API Documentation

The application provides REST API endpoints. Once running, you can:
- Access the Django admin at: http://localhost:8000/admin/
- View API endpoints at: http://localhost:8000/api/
- Use tools like Postman with the provided collection in `post_man-Collections/`
