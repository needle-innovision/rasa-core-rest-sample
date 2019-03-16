## Starter pack
- https://github.com/RasaHQ/starter-pack-rasa-stack

## For tensorflow installation
- `pip3 install --upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.12.0-py3-none-any.whl`

## Using rest webhooks
- run `make run` && `make action_server`
- POST to `http://localhost:5002/webhooks/rest/webhook` 
    ```json
    {
      "sender": "Sandeep",
      "message": "tell me a joke"
    }
    ```