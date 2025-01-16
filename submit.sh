#!/bin/bash

# This is a script to help automate the process to add code files into the right folder and edit the readme table when I submit my leetcodes solutions. 
# For this to work, please put your leetcode code file in the temp folder and ensure that the Leetcode code file title is the same string as the file title and matches the problem label in the actual Leetcode URL. For example if you worked on problem: https://leetcode.com/problems/two-sum/    in python then you would put your code file in the temp folder with the name of the file as "two-sum.py". The file title "two-sum" is also refered to as the problem title. 
# When running the script here is some test input assume abc.py is put in the temp folder:
# leetcode % ./submit.sh  
# Enter the Leetcode Problem Number: 999
# Enter the Leetcode Problem Title: abc
# Enter the Language Used: python
# Enter the Difficulty: Hard
# Directory 'algorithms/python/999' has been created
# Moved Code successfully to ./algorithms/python/999/
# The README.md is updated


# User input
read -p "Enter the Leetcode Problem Number: " leetNumber
read -p "Enter the Leetcode Problem Title: (no .py ext)" leetTitle
read -p "Enter the Language Used: (e.g., python, cpp, sql)" leetLanguage
read -p "Enter the Difficulty: (e.g., Easy, Medium, Hard)" leetDifficulty

# If-else tree for the File Extension Language Variable
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


# # Printing the Variables for testing
# echo $leetNumber 
# echo $leetTitle
# echo $leetLanguage
# echo $leetDifficulty
# echo $capitalized_string
# echo $filename
# echo $capitalLanguage



# -------------------------------------------------------
# -------  Moving Temp Code File to Right Folder --------
# -------------------------------------------------------

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
# -------  Adding the New Problem to the README.md --------
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




