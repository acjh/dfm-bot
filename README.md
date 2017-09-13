# Facebook Messenger Bot tutorial using Django/Python

This has the starter code for the tutorial by [Abhay Kashyap](https://github.com/abhay1).

[Tutorial: How to build a Facebook Messenger bot using Django, Ngrok](https://abhaykashyap.com/blog/post/tutorial-how-build-facebook-messenger-bot-using-django-ngrok)

## Breaking Changes

* `bottutorial` → `dfmbot`
* `django-facebook-messenger-bot-tutorial` → `dfm-bot`
* `FbYomamabotConfig` → `FbDfmbotConfig`
* `yomamabot` → `dfmbot`
* `YoMamaBotView` → `DFMBotView`

## How to use

Run the following commands. You will need Python 3.3+ and have [Virtual Environment Wrapper](http://virtualenvwrapper.readthedocs.io/en/latest/) setup.

    git clone https://github.com/acjh/dfm-bot.git
    cd dfm-bot
    mkvirtualenv dfmbot
    pip install -r requirements.txt
    cd dfmbot
    python manage.py runserver

Follow the tutorial to setup Ngrok.
Edit the `VERIFY_TOKEN` variable in `dfm-bot/dfmbot/fb_dfmbot/views.py` to include the Verify token.
It is set to `2318934571` as default that is used in the tutorial. This can be any token as long as it matches the one you tell Facebook.

Once you have your webhook setup, get your Page Access Token. Then set the `PAGE_ACCESS_TOKEN` variable in the file `dfm-bot/dfmbot/fb_dfmbot/views.py` to your page access token.

# Using PostgreSQL

1. Create person model
2. Import person model
3. PostgreSQL installation: https://djangogirls.gitbooks.io/django-girls-tutorial-extensions/optional_postgresql_installation/
   * Create the database
     - `# CREATE USER dfmuser;`
     - `# CREATE DATABASE dfmdb OWNER dfmuser;`
   * Updating settings
     ```python
     DATABASES = {
          'default': {
              'ENGINE': 'django.db.backends.postgresql',
              'NAME': 'dfmdb',
              'USER': 'dfmuser',
              'PASSWORD': '',
              'HOST': 'localhost',
              'PORT': '',
          }
      }
      ```
   * Installing PostgreSQL package for Python
     - `(dfmbot) ~/dfmbot$ pip3 install psycopg2`
   * Applying migrations and creating a superuser
     - `(dfmbot) ~/dfmbot$ python manage.py makemigrations`
     - `(dfmbot) ~/dfmbot$ python manage.py migrate`
     - `(dfmbot) ~/dfmbot$ python manage.py createsuperuser --username dfmuser`
4. Retrieve a single object with `get()`
   * Create person if does not exist
     ```python
     try:
         user = Person.objects.get(fbid=fbid)
     except Person.DoesNotExist:
         user = Person(fbid=fbid)
         user.save()
     ```

## Errors

* `Person.DoesNotExist` → Person does not exist in database
