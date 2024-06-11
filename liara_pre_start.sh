echo "Running pre-start script..."

# run migrations
python manage.py makemigrations
python manage.py migrate

# other needed commands
# ...

echo "Pre-start script finished."