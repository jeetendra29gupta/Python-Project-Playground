## 🧪 Goal: Generate a local file where the content comes from a variable

```bash
mkdir terraform-local-dynamic-content
cd terraform-local-dynamic-content
```

---

## 🔹 main.tf

```bash
terraform {
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.0"
    }
  }
}

provider "local" {}

resource "local_file" "example" {
  filename = "${path.module}/hello.txt"
  content  = var.file_content
}

```

## 🔹 variables.tf

```bash
variable "file_content" {
  description = "Content to write to the file"
  type        = string
  default     = "This is the default content."
}

```

## 🔹 terraform.tfvars

```bash
file_content = "Hello from terraform.tfvars (dynamic content)!\n"
```

---

## ✅ Step 1: Initialize the Project

```bash 
terraform init
```

## ✅ Step 2: Preview and Auto Apply:

```bash
terraform apply -auto-approve
```

## ✅ Step 3: Test Different Inputs

```bash
terraform apply -var="file_content=Dynamic content via CLI"
```

---
