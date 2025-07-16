variable "files" {
  description = "A map of file names and contents"
  type = map(object({
    filename = string
    content  = string
  }))
}
