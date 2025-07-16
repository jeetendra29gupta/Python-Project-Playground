provider "local" {}

locals {
  now = timestamp()
}

resource "local_file" "timestamped_files" {
  for_each = { for i in range(var.file_count) : i => i }

  filename = "file_${each.key + 1}.txt"
  content  = <<EOT
This is file number ${each.key + 1}
Generated at: ${local.now}
EOT
}
