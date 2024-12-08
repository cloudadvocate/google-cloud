
provider "google" {
  project = var.project_id
  region  = "us-central1"
  zone    = "us-central1-a"
}

terraform {
  required_version = ">= 1.0.0"
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 3.0"
    }
  }
  backend "gcs" {
    bucket = "cloudadv-terraform-state-bucket"
    prefix = "terraform/sample"
  }
}

/*
  backend "gcs" {
    bucket = " test-bucket-124452323"
    prefix = "terraform/sample"
  }
*/

module "vpc" {
  source = "./modules/vpc"
  project_id = var.project_id
  vpc_name = var.vpc_name
}

/*
module "compute" {
  source = "./modules/compute"
  project_id = var.project_id
  network_id = module.vpc.network_id
}*/