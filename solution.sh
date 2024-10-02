#!/bin/bash

# This is a script to help automate the process to add code files into the right folder and edit the read when I submit my leetcodes solutions


# User input
read -p "Enter the Leetcode Problem Number: " leetNumber
read -p "Enter the Leetcode Problem Title: " leetTitle
read -p "Enter the Language Used: " leetLanguage
read -p "Enter the Difficulty: " leetDifficulty

# If-else treeFile Extension Language Variables
capitalLanguage=""
filename=""
if [ "$leetLanguage" == "python" ]; then
    filename="$leetTitle.py"
    capitalLanguage="Python"
elif [ "$leetLanguage" == "cpp" ]; then
    filename="$leetTitle.cpp"
    capitalLanguage="C++"
elif [ "$leetLanguage" == "sql" ]; then
    filename="$leetTitle.sql"
    capitalLanguage="SQL"
else
    echo "Unsupported language: $leetLanguage"
    exit 1  # Exit the script if the language is not supported
fi

# Making the string for the title
# Replace hyphens with spaces
modified_string=$(echo "$leetTitle" | sed 's/-/ /g')
# Capitalize each word
capitalized_string=$(echo "$modified_string" | awk '{ for(i=1;i<=NF;i++) $i=toupper(substr($i,1,1)) tolower(substr($i,2)); print }')


# # Output the result
# echo $leetNumber 
# echo $leetTitle
# echo $leetLanguage
# echo $leetDifficulty
# echo $capitalized_string
# echo $filename
# echo $capitalLanguage



# --------------------------------------------
# -------  Moving Code File to folder --------
# --------------------------------------------

# Checks to see if .../langauge/problem/ folder is created
folderCheck="algorithms/$leetLanguage/$leetNumber"

if [ -d "$folderCheck" ]; then
    echo "Problem has already been completed: '$folderCheck'"
    exit 0  # End the script if the directory exists
fi

# Creates the directory for the new problem
mkdir -p "$folderCheck"
echo "Directory '$folderCheck' has been created"

# Move the file from the temp folder to the new problem folder
tempCodeFileSource="./temp/test.py"
tempCodeFileDestination="./algorithms/python/other/"

tempCodeFileSource="./temp/$filename"
tempCodeFileDestination="./$folderCheck/"
# Check if the source file exists
if [ -f "$tempCodeFileSource" ]; then
    # Move the file to the destination directory
    mv "$tempCodeFileSource" "$tempCodeFileDestination"
    echo "Moved Code successfully to $tempCodeFileDestination"
else
    echo "Source file does not exist."
fi



# ---------------------------------------------------------
# -------  Adding the new problem to the README.md --------
# ---------------------------------------------------------
phrase="    <tr>
        <tr>
        <td>$leetNumber</td>
        <td>
            <a href=\"https://leetcode.com/problems/$leetTitle/\">
                $capitalized_string
            </a>
        </td>
        <td>
            <a href=\"./algorithms/$leetLanguage/$leetNumber/$filename\">
                $capitalLanguage
            </a>
        </td>
        <td>$leetDifficulty</td>
    </tr>"

# Append the phrase to the README.md file
echo "$phrase" >> README.md

# Confirmation message
echo "The README.md is updated"




