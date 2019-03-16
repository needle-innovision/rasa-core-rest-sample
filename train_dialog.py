# Imports
# -----------
import logging

from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.policies import FallbackPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.training import interactive


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

    training_data = agent.load_data(dialog_training_data_file)

    agent.train(training_data)
    agent.persist(path_to_model)
    interactive.run_interactive_learning(agent, dialog_training_data_file, skip_visualization=True)
    # return agent


# Train
# --------
train_dialog('data/stories.md', 'domain.yml')
