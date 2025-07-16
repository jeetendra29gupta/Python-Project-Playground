#!/bin/bash

# You can customize this script
echo "✅ Shell script is running from Terraform!"
echo "Message from Terraform: $1"
echo "Saving to file: $2"

# Write the message to the file
echo "$1" > "$2"
