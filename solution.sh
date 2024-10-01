#!/bin/bash

# Prompt the user for the problem name
read -p "Name of problem: " problem_name

# Ask for the solution type (Python, C++, or SQL)
echo "What is the type of your solution? (Enter 'python', 'cpp', or 'sql')"
read -r solution_type

# Determine the directory path and file extension based on the solution type
case "$solution_type" in
    python)
        directory_path="algorithms/python/$problem_name"
        solution_file="solution.py"
        ;;
    cpp)
        directory_path="algorithms/cpp/$problem_name"
        solution_file="solution.cpp"
        ;;
    sql)
        directory_path="algorithms/sql/$problem_name"
        solution_file="solution.sql"
        ;;
    *)
        echo "Invalid solution type. Please enter 'python', 'cpp', or 'sql'."
        exit 1
        ;;
esac

# Check if the directory already exists, and exit if it does
if [ -d "$directory_path" ]; then
    echo "Directory '$directory_path' already exists."
    exit 1
fi

# Create the directory and move into it
mkdir -p "$directory_path"
cd "$directory_path" || exit

# Create the solution file and the solution description file
touch "$solution_file" solution.md
echo "Directory '$directory_path' and files '$solution_file' and 'solution.md' have been created."

# Read the solution content and save it to the appropriate file
echo "Please paste your solution content below. Press Ctrl+D when you're done:"
solution_content=$(cat)
if [ -n "$solution_content" ]; then
    echo "$solution_content" > "$solution_file"
    echo "Content has been written to '$solution_file'."
else
    echo "No solution content provided. '$solution_file' is empty."
fi

# Read the problem description and save it to solution.md
echo "Please paste your problem description below. Press Ctrl+D when you're done:"
problem_content=$(cat)
if [ -n "$problem_content" ]; then
    echo "$problem_content" > solution.md
    echo "Content has been written to 'solution.md'."
else
    echo "No problem description provided. 'solution.md' is empty."
fi
