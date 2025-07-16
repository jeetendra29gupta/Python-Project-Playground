## 📁 variables.tf vs terraform.tfvars

| File               | Purpose                                                     | Required?                  |
|--------------------|-------------------------------------------------------------|----------------------------|
| `variables.tf`     | **Declares** the variables: their name, type, default, etc. | ❌ Optional but recommended |
| `terraform.tfvars` | **Assigns values** to variables declared in `variables.tf`  | ❌ Optional                 |

## ✅ Summary: Who does what?

| Action                                 | File               |
|----------------------------------------|--------------------|
| Declare a variable’s name/type/default | `variables.tf`     |
| Provide values for those variables     | `terraform.tfvars` |

## 🧠 Analogy: Think of it like a function in programming:

- variables.tf is the function definition with parameters.
- terraform.tfvars is the function call with actual arguments.

## ⚠️ What happens if you skip either?

- No variables.tf: Terraform will still work if you reference variables in main.tf and provide values (via
  terraform.tfvars or -var), but you'll lose type safety and validation.
- No terraform.tfvars: Terraform will prompt you for any variable values that don’t have defaults or CLI values.

---

## 📄 Example without variables.tf and terraform.tfvars

```bash
mkdir terraform-local-dynamic-content-without-variables-file
cd terraform-local-dynamic-content-without-variables-file
```

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


```

## 🔹 terraform.tfvars

```bash
content1 = "This is the content of file1.\n"
content2 = "This is the content of file2.\n"
```

## 🧪 Run Terraform Commands

```bash
  terraform init
```

```bash
  terraform apply
```