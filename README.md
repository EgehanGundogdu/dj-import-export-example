# Django Model Import-Exporting Example Project

This repo contains sample project codes of the django model import export article published on [egehangundogdu.com.](https://egehangundogdu.com)

[If you want to read related article follow the link!]('https://www.egehangundogdu.com/django-import-export-model/')

# Setup 

```bash
virtualenv -p python3 .venv
source .venv/bin/activate
pip install -r requirements.txt
```

# Random data
```bash
python manage.py migrate
python manage.py create_drivers 50
python manage.py runserver 8000
```

# Then visit 
#### localhost:8000/export/
#### localhost:8000/import/



