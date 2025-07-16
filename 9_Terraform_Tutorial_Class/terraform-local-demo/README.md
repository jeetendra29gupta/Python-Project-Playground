### ✅ Step 1: Create Your First Project.

```bash
mkdir terraform-local-demo
cd terraform-local-demo
```

### ✅ Step 2: Create a Terraform File (main.tf)

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
  content  = "Hello, Terraform!"
}

```

### ✅ Step 3: Initialize Terraform

📦 This downloads the required provider (local) and prepares Terraform.

```bash
terraform init
```

### ✅ Step 4: See What Will Happen

🔍 Output will show that Terraform plans to create a file called hello.txt.

```bash
terraform plan
```

### ✅ Step 5: Apply the Changes

📄 Terraform will create a file named hello.txt in your folder with the text:

```bash
terraform apply # Type yes when prompted.
```

### ✅ Step 6: Clean Up

To remove the file and reset (The file will be deleted.):

```bash
terraform destroy # Type yes when prompted.
```

### 🎯 Step 7: Play Around!

Try changing the content in main.tf:

```bash
content = "Terraform is amazing!"
```

Then run:

```bash
terraform apply
```

It will update the file with new content.