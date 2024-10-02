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

# Create the directory
echo "Creating directory '$directory_path'"
mkdir -p "$directory_path"
if [ $? -ne 0 ]; then
    echo "Failed to create directory '$directory_path'."
    exit 1
fi

# Change to the directory
cd "$directory_path" || { echo "Failed to enter directory '$directory_path'"; exit 1; }

# Create the solution file and the solution description file
touch "$solution_file" solution.md
if [ $? -ne 0 ]; then
    echo "Failed to create files '$solution_file' and 'solution.md'."
    exit 1
fi
echo "Directory '$directory
