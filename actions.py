# Imports
# ---------
import logging
import requests

from rasa_core_sdk import Action
from random import randint

# Logger initialization
logger = logging.getLogger(__name__)


class ActionJoke(Action):
    def name(self):
        return 'action_joke'

    def run(self, dispatcher, tracker, domain):
        logging.basicConfig(level='INFO')

        logger.info("""Getting into custom actions""")

        response = requests.get("http://api.icndb.com/jokes/random").json()

        # Get the joke object
        joke = response['value']['joke']

        # Log the joke object in the console
        logging.info(joke)

        # Respond back with text
        dispatcher.utter_message(joke)

        # Use this if you want a json response in rest mode
        # dispatcher.utter_attachment(response)

        # Use this for affirmation modes
        # dispatcher.utter_button_message(text="Did you mean this?",
        #                                 buttons=[{'title': 'Yes', 'payload': '1'},
        #                                          {'title': 'No', 'payload': '0'}])
        return []


class ActionGif(Action):
    def name(self):
        return 'action_gif'

    def run(self, dispatcher, tracker, domain):
        logging.basicConfig(level='INFO')

        logger.info("""Getting into gif actions""")

        response = requests.get("https://api.tenor.com/v1/trending").json()

        # Get the gifs objects length
        gifs_length = len(response['results'])
        gindex = randint(0, gifs_length)

        # Get the gifs objects length
        gif = {
            'type': 'IMAGE',
            'url': response['results'][gindex]['media'][0]['gif']['url']
        }

        # Log the joke object in the console
        logging.info(gif)

        # Respond back with text
        dispatcher.utter_attachment(gif)

        return []
