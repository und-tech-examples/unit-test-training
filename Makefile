build-python:
	@docker-compose build python

build-nodejs:
	@docker-compose build nodejs

build-php:
	@docker-compose build php

api:
	@docker-compose up -d api

python:
	@docker-compose up -d python

nodejs:
	@docker-compose up -d nodejs

php:__init__.cpython-35.pyc
	@docker-compose up -d php

down:
	@docker-compose down


example-pytest: api
	@docker run --name test_container --network unit-test-training_default -d -w /python unit-test-training_python
	@docker cp $(PWD)/examples/python test_container:/python
	@docker exec -it test_container pytest
	@docker rm -f test_container
	@make down
