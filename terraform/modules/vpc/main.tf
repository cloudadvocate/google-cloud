provider "google" {
  project = local.project_id
  region  = "us-central1"
  zone    = "us-central1-a"
}

resource "google_compute_network" "vpc" {
  name                    = var.vpc_name
  auto_create_subnetworks = true
  mtu                     = 1460
}


locals {
  project_id = var.project_id
}