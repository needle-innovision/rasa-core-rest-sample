# Imports
# -----------
import logging

from rasa_core import run
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.policies import FallbackPolicy
from rasa_core.policies.memoization import MemoizationPolicy

# Function
# ------------
from rasa_core.utils import EndpointConfig


def train_dialog(dialog_training_data_file, domain_file, path_to_model='models/dialogue'):
    logging.basicConfig(level='INFO')
    logging.info(dialog_training_data_file)

    # Action to be called if the confidence of intent / action is below the threshold
    fallback = FallbackPolicy(fallback_action_name="action_default_fallback",
                              core_threshold=0.3, # Define the threshold that you need to capture
                              nlu_threshold=0.3)

    # Configuring the endpoint webhook
    core_endpoint_config = EndpointConfig(url='http://localhost:5055/webhook')

    # Configuring the agent
    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(max_history=2), fallback],
                  interpreter=RasaNLUInterpreter('models/nlu/default/chat'),
                  action_endpoint=core_endpoint_config)

    # Load the stories for training the dialog
    training_data = agent.load_data(dialog_training_data_file)

    # Start training the dialog
    agent.train(training_data)

    # Save the training data
    agent.persist(path_to_model)

    # Run interactive learning
    # interactive.run_interactive_learning(agent, dialog_training_data_file, skip_visualization=True)
    return agent


# Function to run the bot
# -----------------------
def run_bot(serve_forever=True):
    # Configure the interpreter
    interpreter = RasaNLUInterpreter('models/nlu/default/chat')

    # Configure the webhook for custom actions
    action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")

    # Configure the agent
    agent = Agent.load('models/dialogue', interpreter=interpreter, action_endpoint=action_endpoint)

    # Run the bot in command line mode
    run.serve_application(agent, channel='cmdline')
    return agent


if __name__ == '__main__':
    # Train
    train_dialog('data/stories.md', 'domain.yml')

    # Run the bot
    run_bot()
