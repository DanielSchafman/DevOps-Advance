#!/bin/bash

kubectl apply -f mysql-pvc.yaml && \
kubectl apply -f mysql-configmap.yaml && \
kubectl apply -f mysql-deployment.yaml && \
kubectl apply -f mysql-service.yaml && \
kubectl apply -f web-app-deployment.yaml && \
kubectl apply -f web-app-service.yaml && \
kubectl apply -f rest-api-deployment.yaml && \
kubectl apply -f rest-api-service.yaml && \
kubectl apply -f close-deployment.yaml && \
kubectl apply -f close-service.yaml && \
kubectl apply -f tests-deployment.yaml && \
kubectl apply -f tests-service.yaml