# py-url-shortener

This is an educational project, based on the [System Design Walkthrough by HelloInterview](https://www.hellointerview.com/learn/system-design/answer-keys/bitly).

> I follow exact Functional/Non-functional requirements and do not implement the out-of-scope features defined in the original system design walkthrough.

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


# Infrastructure

As infrastructure, we need to come up with the solutions which covers real-world scenarios, but using local Minikube:

* For Web entrypoint API we use [Sanic](https://sanic.dev/en/).

* For Observability logs, we use [Fluenbit](https://fluentbit.io/), 
together with [Opensearch](https://opensearch.org/) and [Opensearch Dashboards](https://www.opensearch.org/docs/latest/dashboards/)

* For error tracking we replace [Sentry](https://sentry.io/) with [BugSink](https://www.bugsink.com/) they are compatible. 
Btw, [GlitchTip](https://glitchtip.com/) is another alternative.
> Here I am not saying that Sentry is fully replaceable, because Sentry is more than issue tracking, but it is out of scope.

* As Load Balancer we use [HorizontalPodAutoscaler](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/) based on CPU utilization of the pods.
HPA was activated both for Nginx and URL Shortener APP.

* As API Gateway we use [Nginx](https://nginx.org/en/), basically the simplest solution came to my mind for this application.
But of course, you can play around [Kong](https://konghq.com/products/kong-gateway) or just any paid API Gateway solution.

* For Caching the original url and shortened ID data we use [Redis](https://redis.io/)

* As global counter we use again, [Redis](https://redis.io/)

* Again as rate limiter we use Nginx request limiter. [This blog post](https://ibug.io/blog/2024/01/nginx-limit-req/) did a nice job on explaining the concept.
> Here I did not play around with Nginx config to show the master class, my main goal was to show that it is possible with Nginx.

* It is also important to stress/load test the endpoints, for this I choose to go with [Locust](https://locust.io/)


# TODO:

* Add DB support
* Add more robust error handling around API and services
* Granular Logging for the services
* Metrics - success/failure rate
* Grafana Dashboards