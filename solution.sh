#!/bin/bash

echo "hello me"


# Define the source file relative to the current script's location
SOURCE_FILE="./relative/path/to/source/file"

# Define the destination directory relative to the current script's location
# or hardcode a known local path if needed
DESTINATION_DIR="/absolute/path/to/known/local/folder"

# Check if the source file exists
if [ -f "$SOURCE_FILE" ]; then
    # Move the file to the destination directory
    mv "$SOURCE_FILE" "$DESTINATION_DIR"
    echo "File moved successfully to $DESTINATION_DIR"
else
    echo "Source file does not exist."
fi


