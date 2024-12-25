# py-url-shortener

This is an educational project, based on the [System Design Walkthrough by HelloInterview](https://www.hellointerview.com/learn/system-design/answer-keys/bitly).

The ultimate goal is to show the full implementation of the project, in a small iterations using Python.

This will close the gap between theoretical System Design and the real implementation - and will show how the decisions are changing with each iteration.

## Setup

Create virtualenv in the project root directory named ".venv"

### Commands

`make install-flit`

`make install-dev`

`make run` or `make test`

### Start

We can use docker compose for local testing:

`docker compose -f docker-compose.local.yml up`

# Helm charts

Local Build images for Minikube:

- `eval $(minikube docker-env)`
- `cd ci`
- `docker build -t url_shortener:latest -f ./Dockerfile_app ../`
- `docker build -t custom_nginx:latest -f ./Dockerfile_nginx ./`

Install using HELM:

- `cd ci/kubernetes`
- `helm install py-url-shortener .`

For autoscaling we need to enable kubernetes metrics in minikube:

`minikube addons enable metrics-server`

If you want to see the local Minikube Dashboard and the statuses of the deployments, then in separate terminal, activate the dashboard:

`minikube dashboard`