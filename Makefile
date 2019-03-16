help:
	@echo "**** Running the script ****"

train_nlu:
	python train_nlu.py

train_dialog:
	python train_dialog.py

run:
	python -m rasa_core.run -d models/dialogue -u models/nlu/default/chat --port 5002 --endpoints endpoints.yml

action_server:
	python -m rasa_core_sdk.endpoint --actions actions