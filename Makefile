start:
	poetry run flask --app hexlet_flask.app --debug run --port 8010

lint:
	poetry run flake8 hexlet_flask