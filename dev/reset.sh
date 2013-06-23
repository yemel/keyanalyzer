sudo -u postgres psql -c "DROP DATABASE analyzer"
sudo -u postgres psql -c "CREATE DATABASE analyzer ENCODING 'UTF-8'"
python manage.py syncdb --noinput
python manage.py migrate
