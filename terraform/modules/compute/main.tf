provider "google" {
  project = var.project_id
  region  = "us-central1"
  zone    = "us-central1-a"
}

resource "google_compute_instance" "default" {
  name         = "terraform-test"
  machine_type = "e2-medium"
  zone         = "us-central1-a"

  tags = ["terraform"]

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  network_interface {
    network = var.network_id
  }

  metadata_startup_script = "echo hi > /test.txt"
  
}
