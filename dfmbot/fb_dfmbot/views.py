# dfmbot/fb_dfmbot/views.py
import json, requests, random, re
from pprint import pprint

from django.views import generic
from django.http.response import HttpResponse

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .models import Person

#  ------------------------ Fill this with your page access token! -------------------------------
PAGE_ACCESS_TOKEN = ""
VERIFY_TOKEN = "2318934571"

jokes = { 'stupid': ["""She needs a recipe to make ice cubes.""",
                     """She thinks DNA is the National Dyslexics Association."""],
         'fat':      ["""When she goes to a restaurant, instead of a menu, she gets an estimate.""",
                      """When the cops see her on a street corner, they yell, "Hey you guys, break it up!" """],
         'dumb': ["""When God was giving out brains, she thought they were milkshakes and asked for extra thick.""",
                  """She locked her keys inside her motorcycle."""] }

# Helper function
def post_facebook_message(fbid, recevied_message):
    # Remove all punctuations, lower case the text and split it based on space
    tokens = re.sub(r"[^a-zA-Z0-9\s]",' ',recevied_message).lower().split()
    joke_text = ''
    for token in tokens:
        if token in jokes:
            joke_text = random.choice(jokes[token])
            break
    if not joke_text:
        joke_text = "I didn't understand! Send 'stupid', 'fat', 'dumb' for a joke!"

    user_details_url = "https://graph.facebook.com/v2.6/%s"%fbid
    user_details_params = {'fields':'first_name,last_name,profile_pic', 'access_token':PAGE_ACCESS_TOKEN}
    user_details = requests.get(user_details_url, user_details_params).json()
    joke_text = 'Yo '+user_details['first_name']+'..! ' + joke_text

    user = update_user_details(fbid, user_details)
    pprint(user.last_message)
    user.last_message = recevied_message
    user.save()

    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s'%PAGE_ACCESS_TOKEN
    response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text":joke_text}})
    status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
    pprint(status.json())

def update_user_details(fbid, user_details):
    try:
        user = Person.objects.get(fbid=fbid)
    except Person.DoesNotExist:
        user = Person(fbid=fbid)
    user.first_name = user_details['first_name']
    user.last_name = user_details['last_name']
    user.save()
    return user

# Create your views here.
class DFMBotView(generic.View):
    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == VERIFY_TOKEN:
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    # Post function to handle Facebook messages
    def post(self, request, *args, **kwargs):
        # Converts the text payload into a python dictionary
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        # Facebook recommends going through every entry since they might send
        # multiple messages in a single call during high load
        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                # Check to make sure the received call is a message call
                # This might be delivery, optin, postback for other events
                if 'message' in message:
                    # Print the message to the terminal
                    pprint(message)
                    # Assuming the sender only sends text. Non-text messages like stickers, audio, pictures
                    # are sent as attachments and must be handled accordingly.
                    post_facebook_message(message['sender']['id'], message['message']['text'])
        return HttpResponse()
