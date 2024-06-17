# create a virtual environment named 'venv' if it doesn't already exist
python3.9 -m venv venv

# activate the virtual environment
source venv/bin/activate

# install all deps in the venv
pip install django
pip install cmake
pip install -r requirements.txt
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

# collect static files using the Python interpreter from venv
# python3 manage.py collectstatic --noinput

# [optional] Start the application here 
# python manage.py runserver