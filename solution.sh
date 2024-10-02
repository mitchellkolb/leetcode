#!/bin/bash

echo "hello me"



# User input
read -p "Enter the Leetcode Problem Number: " leetNumber
read -p "Enter the Leetcode Problem Title: " leetTitle
read -p "Enter the Language Used: " language
echo $leetNumber 
echo $leetTitle
echo $language

# File Extension Language Variables
textCpp=".cpp"
textPython=".py"
textSql=".sql"


# Hardcoded variable for the folder name
FOLDER_NAME="myfolder"

# Check if the folder exists
if [ -d "$FOLDER_NAME" ]; then
    echo "Folder '$FOLDER_NAME' exists."
    exit 0  # End the script if the folder exists
else
    echo "Folder '$FOLDER_NAME' does not exist."
fi

# Continue with the script if the folder does not exist
echo "ALRIGHT"

# # Define the source file relative to the current script's location
# SOURCE_FILE="./temp/test.py"

# # Define the destination directory relative to the current script's location
# # or hardcode a known local path if needed
# DESTINATION_DIR="./algorithms/python/other/"

# # Check if the source file exists
# if [ -f "$SOURCE_FILE" ]; then
#     # Move the file to the destination directory
#     mv "$SOURCE_FILE" "$DESTINATION_DIR"
#     echo "File moved successfully to $DESTINATION_DIR"
# else
#     echo "Source file does not exist."
# fi


