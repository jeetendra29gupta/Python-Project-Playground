# 🚀 AWS CLI & AWS SAM Setup Guide (Linux)

This guide will help you install and configure **AWS CLI** and **AWS SAM CLI** on a Linux system, and authenticate using your IAM user credentials.

---

## 🔑 How to Get Your Access Key ID and Secret Access Key

1. Go to the AWS Console: https://console.aws.amazon.com/
2. On the top right, click your username, then choose **"Security credentials"**
3. Scroll to the **"Access keys"** section
4. Click **"Create access key"** and select **"Command Line Interface (CLI)"**
5. You'll see:
   - **Access Key ID**
   - **Secret Access Key**

> ⚠️ **Copy and store these securely** — you won’t be able to view the secret key again!

---

## 📥 How to Download and Install AWS CLI

    ```bash
    
    # Download the AWS CLI installer
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -Lo "aws-cli.zip"
    
    # Unzip the installer
    unzip aws-cli.zip -d aws-cli

    # Install AWS CLI
    sudo ./aws-cli/aws/install

    # Verify installation
    aws --version

    ````

---

## 📥 How to Download and Install AWS SAM CLI

    ```bash

    # Install required dependencies
    sudo apt install -y curl unzip zip python3 python3-pip docker.io

    # Download the AWS SAM CLI installer (latest stable version)
    curl -Lo aws-sam.zip https://github.com/aws/aws-sam-cli/releases/download/v1.142.1/aws-sam-cli-linux-x86_64.zip
    
    # Unzip the installer
    unzip aws-sam.zip -d aws-sam
    
    # Install SAM CLI
    sudo ./aws-sam/install
    
    # Verify installation
    sam --version

    ```

---

## ⚙️ How to Configure AWS CLI with IAM Credentials

    ```bash
    
    # Verify AWS CLI is installed
    aws --version
    
    # Configure with your IAM credentials
    aws configure

    ```

You'll be prompted for:

* **AWS Access Key ID** 🔑 (from IAM user)
* **AWS Secret Access Key** 🔒 (from IAM user)
* **Default region name** (e.g., `us-east-1`)
* **Default output format** (e.g., `json`, `yaml`, or `text`)

---

## ✅ Verify Configuration

    ```bash

    # Show stored credentials and region
    aws configure list
    
    # Test access and identity (STS = Security Token Service)
    aws sts get-caller-identity

    ```

---

## ✅ You're All Set!

You can now use `aws` and `sam` commands to manage cloud infrastructure and deploy serverless applications from your local environment.

---
