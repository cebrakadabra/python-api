## Python REST API
with Django REST Framework

## How to get the Django REST Framework
install it with pip
```
pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support
```

### Development Notes
- simple api with one endpoint named snippets finished
- API which follows the DRY concept
- using class based views, rather than function based views
- using generic class based views (lot of code reduce!)
- added authentication
- created the root endpoint for the api, hyperlinked
- created login/logout in the browsable api

### One Bug
In the browsable API it's only possible to create a new snippet via the raw data post statement.
The api form has a bug on the code field.
