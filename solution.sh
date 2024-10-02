#!/bin/bash

echo "Welcome to the File Organizer!"

# Get directory name from user
echo "Enter a name for the new directory:"
read dirname

# Check if directory exists
if [ -d "$dirname" ]; then
    echo "Directory '$dirname' already exists."
else
    mkdir "$dirname"
    echo "Directory '$dirname' created."
fi

# Get filename from user
echo "Enter the filename to move into '$dirname':"
read filename

# Check if file exists
if [ -f "$filename" ]; then
    mv "$filename" "$dirname"
    echo "Moved '$filename' into '$dirname'."
else
    echo "File '$filename' does not exist."
fi

# Append text to a file
echo "Do you want to add notes to a file? (yes/no)"
read answer

if [ "$answer" = "yes" ]; then
    echo "Enter the filename to append to (it will be created if it doesn't exist):"
    read notesfile

    echo "Enter the text to append:"
    read notestext

    echo "$notestext" >> "$notesfile"
    echo "Notes added to '$notesfile'."
fi



echo "Welcome to the File Manager!"

# Prompt for operation
echo "Choose an operation: move, copy, backup"
read operation

# Get source and destination
echo "Enter the source file or directory:"
read source

echo "Enter the destination directory:"
read destination

# Check if source exists
if [ ! -e "$source" ]; then
    echo "Source '$source' does not exist."
    exit 1
fi

# Ensure destination directory exists
mkdir -p "$destination"

# Perform the chosen operation
case "$operation" in
    move)
        mv -i "$source" "$destination"
        echo "Moved '$source' to '$destination'."
        ;;
    copy)
        if [ -d "$source" ]; then
            cp -ri "$source" "$destination"
        else
            cp -i "$source" "$destination"
        fi
        echo "Copied '$source' to '$destination'."
        ;;
    backup)
        timestamp=$(date +"%Y%m%d_%H%M%S")
        backupname="$(basename "$source")_$timestamp"
        cp -r "$source" "$destination/$backupname"
        echo "Backup of '$source' created at '$destination/$backupname'."
        ;;
    *)
        echo "Invalid operation."
        ;;
esac