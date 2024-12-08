#!/bin/bash

terraform apply -var-file=./envs/dev.tfvars --auto-approve
