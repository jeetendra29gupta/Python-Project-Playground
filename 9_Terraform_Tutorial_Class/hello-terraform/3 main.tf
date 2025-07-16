provider "local" {}

resource "local_file" "counted_files" {
  for_each = { for i in range(var.file_count) : i => i }

  filename = "file_${each.key + 1}.txt"
  content  = "This is file number ${each.key + 1}"
}
