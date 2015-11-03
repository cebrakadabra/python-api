## Python REST API
with Django REST Framework
http://www.django-rest-framework.org/

## How to get the Django REST Framework
install it with pip
```
pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support
```

## start application by running
```
python manage.py runserver
```

### If you would like to startup in a virtual env
```
virtualenv env
source env/bin/activate
```

### if you want to clean up your migrations in Development
```
rm -f tmp.db db.sqlite3
rm -r snippets/migrations
python manage.py makemigrations snippets
python manage.py migrate
```

### Development Notes
- simple api with one endpoint named snippets finished
- API which follows the DRY concept
- using class based views, rather than function based views
- using generic class based views (lot of code reduce!)
- added authentication
- created the root endpoint for the api, hyperlinked
- created login/logout in the browsable api
- View Sets and routers
  - allows the developer to concentrate on modeling the state and interactions of the API, and leave the URL construction to be handled automatically, based on common conventions

### Default user:
admin:root

if you want to configure a new one run
```
python manage.py createsuperuser
```

### Issue Board
In the browsable API it's only possible to create a new snippet via the raw data post statement.
The api form has a bug on the code field.
