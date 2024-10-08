# Might need to change permissions to run it use this file. Open up powershell as administrator and use commands
# Set-ExecutionPolicy RemoteSigned
# Then run it with: .\submit.ps1

# This is a PowerShell script to help automate the process to add code files into the right folder and edit the README table when you submit your Leetcode solutions.
# For this to work, please put your leetcode code file in the temp folder and ensure that the Leetcode code file title is the same string as the file title and matches the problem label in the actual Leetcode URL. For example if you worked on problem: https://leetcode.com/problems/two-sum/    in python then you would put your code file in the temp folder with the name of the file as "two-sum.py". The file title "two-sum" is also refered to as the problem title. 

# User input
$leetNumber = Read-Host "Enter the Leetcode Problem Number"
$leetTitle = Read-Host "Enter the Leetcode Problem File Title (no .py ext)"
$leetLanguage = Read-Host "Enter the Language Used (e.g., python, cpp, sql)"
$leetDifficulty = Read-Host "Enter the Difficulty (e.g., Easy, Medium, Hard)"
Write-Host ""


# If-else logic for the File Extension and Language Variable
$capitalLanguage = ""
$filename = ""

if ($leetLanguage -eq "python") {
    $filename = "$leetTitle.py"
    $capitalLanguage = "Python"
}
elseif ($leetLanguage -eq "cpp") {
    $filename = "$leetTitle.cpp"
    $capitalLanguage = "C++"
}
elseif ($leetLanguage -eq "sql") {
    $filename = "$leetTitle.sql"
    $capitalLanguage = "SQL"
}
else {
    Write-Host "Unsupported language: $leetLanguage"
    exit 1  # Exit the script if the language is not supported
}

# Making the string for the title
# Replace hyphens with spaces
$modified_string = $leetTitle -replace '-', ' '
# Capitalize each word
$capitalized_string = (Get-Culture).TextInfo.ToTitleCase($modified_string)



# -------------------------------------------------------
# -------  Moving Temp Code File to Right Folder --------
# -------------------------------------------------------

# Checks to see if the problem folder already exists
$folderCheck = "algorithms/$leetLanguage/$leetNumber"

if (Test-Path $folderCheck) {
    Write-Host "Problem has already been completed: '$folderCheck'"
    exit 0  # End the script if the directory exists
}

# Creates the directory for the new problem
New-Item -ItemType Directory -Path $folderCheck -Force | Out-Null
Write-Host "Directory '$folderCheck' has been created"

# Move the file from the temp folder to the new problem folder
$tempCodeFileSource = "./temp/$filename"
$tempCodeFileDestination = "./$folderCheck/"

# Check if the source file exists
if (Test-Path $tempCodeFileSource) {
    # Move the file to the destination directory
    Move-Item -Path $tempCodeFileSource -Destination $tempCodeFileDestination
    Write-Host "Moved code successfully to $tempCodeFileDestination"
}
else {
    Write-Host "Source file does not exist."
}

# ---------------------------------------------------------
# -------  Adding the New Problem to the README.md --------
# ---------------------------------------------------------
$phrase = @"
    <tr>
        <td>$leetNumber</td>
        <td>
            <a href="https://leetcode.com/problems/$leetTitle/">
                $capitalized_string
            </a>
        </td>
        <td>
            <a href="./algorithms/$leetLanguage/$leetNumber/$filename">
                $capitalLanguage
            </a>
        </td>
        <td>$leetDifficulty</td>
    </tr>
"@

# Append the phrase to the README.md file
Add-Content -Path "README.md" -Value $phrase

# Confirmation message
Write-Host "The README.md has been updated"
