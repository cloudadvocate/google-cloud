#!/bin/bash

terraform init -reconfigure -var-file=./envs/dev.tfvars
terraform plan -var-file=./envs/dev.tfvars
