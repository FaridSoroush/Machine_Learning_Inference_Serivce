IMAGE?=ghcr.io/faridsoroush/ml-service
TAG?=$(shell git describe --tags --always --dirty)

.PHONY: install dev test lint run docker build push helm deploy rollback

install:
	python -m venv .venv && . .venv/Scripts/activate && pip install -r requirements.txt

dev:
	. .venv/Scripts/activate && pip install -r requirements-dev.txt

test:
	. .venv/Scripts/activate && pytest -q

lint:
	. .venv/Scripts/activate && ruff check app tests

run:
	uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload

docker:
	docker build -t $(IMAGE):$(TAG) .

push:
	docker push $(IMAGE):$(TAG)

helm:
	helm lint charts/ml-service

deploy:
	helm upgrade --install ml-service charts/ml-service \
	  --set image.repository=$(IMAGE) --set image.tag=$(TAG)

rollback:
	kubectl rollout undo deployment/ml-service
