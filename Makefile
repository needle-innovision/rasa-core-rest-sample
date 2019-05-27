train-nlu:
	python -m rasa_nlu.train -c config.yml --fixed_model_name chat --data data/nlu.md -o models --project nlu --verbose

train-core:
	python -m rasa_core.train -s data/stories.md -d domain.yml -o models/dialogue --debug

train-interactive:
	python -m rasa_core.train interactive -s data/stories.md -d domain.yml -o models/dialogue --verbose

test-core:
	python -m rasa_core.test --core models/dialogue -s data/stories.md --fail_on_prediction_errors

run-core:
	python -m rasa_core.run --core models/dialogue --nlu models/nlu/chat --verbose  --endpoints endpoints.yml

run-actions:
	python -m rasa_core_sdk.endpoint --actions actions

train-interactive:
	python -m rasa_core.train interactive -s data/stories.md -d domain.yml -o models/dialogue --verbose --endpoints endpoints.yml

run:
	make run-core