The Terraform null resource is a resource provided by the null provider in Terraform. It's used when you need to run arbitrary actions or provisioning logic that doesn't map directly to a specific infrastructure provider, like AWS or Azure.

🧪 Run Terraform

```bash
chmod +x run_me.sh
terraform init
terraform apply
```

✅ When you run terraform apply, Terraform will call your script with the message and filename.

📝 After it's done, you should see a new file called output_from_script.txt with your message inside it.