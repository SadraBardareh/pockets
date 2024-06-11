echo "Running pre-start script..."

# run migrations
python manage.py makemigrations
python manage.py migrate

celery -A pockets beat

echo "Pre-start script finished."