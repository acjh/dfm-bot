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
