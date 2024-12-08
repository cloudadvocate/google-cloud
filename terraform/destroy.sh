#!/bin/bash

terraform apply -destroy -var-file=./envs/dev.tfvars --auto-approve
