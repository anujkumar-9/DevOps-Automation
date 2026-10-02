#!/bin/bash

set -e

echo "Starting deployment..."

echo "Building Docker image..."
docker build -t my-app:latest .

echo "Applying Kubernetes manifests..."
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml

echo "Checking deployment status..."
kubectl get deployments
kubectl get pods
kubectl get services

echo "Deployment completed successfully!"


Simple flow
deploy.sh
   ↓
Docker Build
   ↓
Kubernetes Deployment
   ↓
Kubernetes Service
   ↓
Check Pods
   ↓
Check Service
Interview mein important:

# #!/bin/bash
# → Script Bash shell mein execute hogi.

# set -e
# → Agar koi command fail hoti hai, script wahi stop ho jayegi.

# docker build
# → Docker image build karta hai.

# kubectl apply
# → Kubernetes resources create/update karta hai.

# kubectl get pods
# → Running Pods ki information deta hai.