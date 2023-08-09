#!/bin/ash
echo "Appliying all migrations"

python manage.py makemigrations
python manage.py migrate
exec "$@"