provider "local" {}

resource "local_file" "hello" {
  content = "Hello, Terraform \n"
  filename = "hello.txt"
}
