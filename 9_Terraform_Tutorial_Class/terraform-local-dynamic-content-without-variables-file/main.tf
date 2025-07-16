terraform {
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.0"
    }
  }
}

provider "local" {}

variable "content1" {
  description = "Content for file1"
  type        = string
}

variable "content2" {
  description = "Content for file2"
  type        = string
}

resource "local_file" "file1" {
  filename = "${path.module}/file1.txt"
  content  = var.content1
}

resource "local_file" "file2" {
  filename = "${path.module}/file2.txt"
  content  = var.content2
}
