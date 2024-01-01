
Commit changes to github
- git push origin main

To deploy to heroku:
- git push heroku main

To collect static files:
- heroku run python manage.py collectstatic

Create super user in heroku:
- heroku run python manage.py createsuperuser

Disable Static
-  heroku config:set DISABLE_COLLECTSTATIC=1