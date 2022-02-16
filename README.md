# prerequisites like python, pip and virtualenv installation
# clone the git repository
# make a virtualenv and activate it 
# Go to kira-test repository 
`cd kira-test`
# now run `pip install -r requirements.txt` to install all the packages
# migrating
`python manage.py migrate`

This will create the database
# Now create superuser
`python manage.py createsuperuser`
# Running the server
`python manage.py runserver`
