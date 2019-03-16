# Imports
# -----------
from rasa_nlu import config
from rasa_nlu.model import Trainer, Interpreter
from rasa_nlu.training_data import load_data


# Function
# -----------
def train_nlu(data: object, config_file: object, model_dir: object) -> object:
    # Load the training data
    training_data = load_data(data)

    # Configure the trainer
    trainer = Trainer(config.load(config_file))

    # Start training
    trainer.train(training_data)

    # Persist the training model
    model_directory = trainer.persist(model_dir, fixed_model_name='chat')


# Testing
# -----------
def run_nlu():
    interpreter = Interpreter.load('./models/nlu/default/chat')
    print(interpreter.parse(u"how many days in january?"))


# Training
# -----------
if __name__ == '__main__':
    # Training the model
    train_nlu('data/nlu.md', 'nlu_config.yml', 'models/nlu')

    # Test the trained data
    run_nlu()
