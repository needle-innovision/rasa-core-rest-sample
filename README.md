## How to run this application
- Train the model `make train_nlu`
- Train the dialog `make train_dialog`
- If you want to train the dialog online `make train_online`
- Run the custom action server `make action_server`
- Run the bot `make run`


## Using rest webhooks
- run `make run` && `make action_server`
- POST to `http://localhost:5002/webhooks/rest/webhook` 
    ```json
    {
      "sender": "Sandeep",
      "message": "tell me a joke"
    }
    ```

## Resources

#### Starter packs
- https://github.com/RasaHQ/starter-pack-rasa-stack    

#### For tensorflow installation
- `pip3 install --upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.12.0-py3-none-any.whl`
