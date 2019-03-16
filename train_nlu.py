# Imports
# -----------
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.training_data import load_data


# Function
# -----------
def train(data: object, config_file: object, model_dir: object) -> object:
    # Load the training data
    training_data = load_data(data)

    # Configure the trainer
    trainer = Trainer(config.load(config_file))

    # Start training
    trainer.train(training_data)

    # Persist the training model
    model_directory = trainer.persist(model_dir, fixed_model_name='chat')


# Training
# ------------
train('data/nlu.md', 'nlu_config.yml', 'models/nlu')
