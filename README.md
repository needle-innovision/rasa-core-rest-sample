## Installation
- `pip install rasa_core`
- `pip install spacy`
- `pip install sklearn-crfsuite`
- `python -m spacy download en`

## How to run this application
- Train the model `make train-nlu`
- Train the core `make train-core`
- If you want to train the dialog online `make train-interactive`
- Run the custom action server `make run-actions`
- Run the bot `make run`


## Using rest webhooks
- run `make run` && `make run-actions`
- POST to `http://localhost:5005/webhooks/rest/webhook` 
    ```json
    {
      "sender": "Sandeep",
      "message": "tell me a joke"
    }
    ```

## Resources
- Dummy images api `https://api.tenor.com/v1/trending`.

#### Starter packs
- https://github.com/RasaHQ/starter-pack-rasa-stack    

#### For tensorflow installation
- `pip3 install --upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.12.0-py3-none-any.whl`
