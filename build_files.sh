# # create a virtual environment named 'venv' if it doesn't already exist
python3.9 -m venv venv

# # activate the virtual environment
source venv/bin/activate
pip install -r requirements.txt

# # install all deps in the venv
# # pip install django
# # pip install cmake==3.25
# # pip install dlib
# pip install -r requirements.txt


python3.9 manage.py collectstatic
python manage.py runserver