# Setup-Project

This project provides a set of Python scripts that automate the process of setting up a Node.js workspace, installing necessary packages, and managing project paths. It simplifies the environment setup by creating essential directories, initializing Node.js, and running package installations, all while ensuring that file paths are handled properly across different platforms.

## Files

1. **library.py**: Contains helper functions for handling paths, loading package lists from files, preparing npm install commands, changing directories, and setting up a Node.js project.
2. **main.py**: The main file that uses the functions from `library.py` to set up a Node.js project, install development and production dependencies, and handle workspace setup.

## Features

- **Path Handling**: Automatically normalizes file paths across platforms.
- **Package Management**: Reads package names from files and constructs `npm install` commands for both development and production dependencies.
- **Workspace Setup**: Initializes a Node.js project and sets up essential folders and files for a smooth development environment.
- **Command Execution**: Executes npm commands from within the specified directory.
  
---

## Setup Instructions

### Prerequisites

Make sure you have Python 3.x and Node.js installed on your system.

1. **Python**: [Download Python](https://www.python.org/downloads/)
2. **Node.js**: [Download Node.js](https://nodejs.org/)

Create a virtual environment called setupProject via the following:
`python -m venv setupProject `
to activate it, run one of the following commands, based on the OS of your machine:
`setupProject\Scripts\Activate` on Windows
`source setupProject/bin/activate` on MacOS/UNIX

then run the following to download all dependencies for the project:
`pip install -r requirements.txt`