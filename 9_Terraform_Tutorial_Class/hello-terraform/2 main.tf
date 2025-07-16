provider "local" {}

resource "local_file" "greetings" {
  for_each = var.files

  filename = each.value.filename
  content  = each.value.content
}
