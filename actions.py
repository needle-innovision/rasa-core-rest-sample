# Imports
# ---------
import logging
import requests

from rasa_core_sdk import Action

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

        # dispatcher.utter_message(joke)
        dispatcher.utter_attachment(response)

        # dispatcher.utter_button_message(text="Did you mean this?",
        #                                 buttons=[{'title': 'Yes', 'payload': '1'},
        #                                          {'title': 'No', 'payload': '0'}])
        return []
