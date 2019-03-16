import logging

from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.policies import MemoizationPolicy, FallbackPolicy
from rasa_core.training import interactive
from rasa_core.utils import EndpointConfig

logger = logging.getLogger(__name__)


# Function to run the training in online interactive mode
# -------------------------------------------------------
def train_online(interpreter,
                 domain_file="domain.yml",
                 training_data_file='data/stories.md'):
    # Configure the custom action endpoint
    action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")

    # Action to be called if the confidence of intent / action is below the threshold
    fallback = FallbackPolicy(fallback_action_name="action_default_fallback",
                              core_threshold=0.3,  # Define the threshold that you need to capture
                              nlu_threshold=0.3)

    # Configure the agent
    agent = Agent(domain_file,
                  policies=[
                      MemoizationPolicy(max_history=2),
                      fallback
                      # Doesn't work for system without gpu support
                      # KerasPolicy(max_history=3, epochs=3, batch_size=50)
                  ],
                  interpreter=interpreter,
                  action_endpoint=action_endpoint)

    # Load the training data file
    data = agent.load_data(training_data_file)

    # Initiate the training process
    agent.train(data)

    # Run the training in interactive mode
    # Note: Visualization is disabled because of a bug in the system
    interactive.run_interactive_learning(agent, training_data_file, skip_visualization=True)

    return agent


if __name__ == '__main__':
    logging.basicConfig(level="INFO")
    nlu_interpreter = RasaNLUInterpreter('models/nlu/default/chat')
    train_online(nlu_interpreter)
