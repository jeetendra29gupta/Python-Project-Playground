## ✅ Step-by-step Installation Instructions for Terraform (Linux Mint/Debian-based):

### 1. Install required packages

```bash
sudo apt-get update && sudo apt-get install -y gnupg software-properties-common curl
```

### 2. Add the HashiCorp GPG key

```bash
curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
```

### 3. Add the official HashiCorp Linux repository

```bash
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com bookworm main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
```

### 4. Update and install Terraform

```bash
sudo apt-get update && sudo apt-get install terraform
```

### 5. Verify the installation

```bash
terraform -v
```