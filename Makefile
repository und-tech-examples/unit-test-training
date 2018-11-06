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

php:
	@docker-compose up -d php

down:
	@docker-compose down
