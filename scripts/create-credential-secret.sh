#!/bin/bash
kubectl create secret generic env --dry-run=client -o yaml --from-env-file=.env > secrets.yaml

kubeseal --cert https://sealed-secrets.k8s-dev.hpc.uidaho.edu/v1/cert.pem -f secrets.yaml -w secrets.yaml --scope=cluster-wide