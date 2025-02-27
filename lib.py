import subprocess
from os import chdir, getcwd, makedirs, path 

def handle_path(inputpath: str) -> str:
    """
    Normalize the given file path by ensuring consistent formatting across platforms.

    This function takes a file path as input, normalizes it using the `os.path.normpath()`
    function, and returns the correctly formatted path.

    Args:
        inputpath (str): The file or directory path to normalize. It can include 
                          forward slashes, backslashes, or a mix of both.

    Returns:
        str: The normalized file path with appropriate path separators based on the platform.

    Example:
        >>> handle_path("C:/Users/name//Documents")
        "C:\\Users\\name\\Documents"

        >>> handle_path("C:\\Users\\name\\Documents\\..\\Downloads")
        "C:\\Users\\name\\Downloads"
    """
    return path.normpath(inputpath)

# get packages from given file
def load_packages(filepath: str) -> str:
    """
    Reads a list of package names from a given file and returns them as a space-separated string.

    Args:
        filepath (str): The path to the file containing the list of packages.

    Returns:
        str: A space-separated string of packages, formatted for an npm install command.
    
    Example:
        packages = load_packages('packages.txt')
    """
    with open(filepath) as dev:
        lines = dev.readlines()
        packages = ""
        for line in lines:
            if lines[-1] == line:
                packages += line
            else:
                packages += line[0:-1]
            packages += ' '
    return packages

# install packages
def prepare_command(packages: str, dev:bool=False) -> str:
    """
    Prepares the npm install command string, adding the `-D` flag for dev dependencies if needed.

    Args:
        packages (str): A space-separated string of package names to install.
        dev (bool, optional): Whether to install packages as dev dependencies (default is False).

    Returns:
        str: The full npm install command string.
    
    Example:
        command = prepare_command('express lodash', dev=True)
    """
    cmd = "npm i "
    if dev:
        cmd += "-D "
    for package in packages:
        cmd += package
    return cmd

def move_to_workdir(workdir_path: str) -> None:
    """
    Changes the current working directory to the specified directory.

    Args:
        workdir_path (str): The path to the target directory.

    Returns:
        None

    Prints a message indicating success or failure based on whether the directory change was successful.
    
    Example:
        move_to_workdir("/path/to/your/project")
    """
    if getcwd() == workdir_path:
        print(f"💡 Already in the directory {workdir_path}")
    try:
        chdir(workdir_path)
        print(f"✅ Changed directory to {workdir_path}")
    except FileNotFoundError:
        print(f"❌ The directory {workdir_path} was not found")
    except PermissionError:
        print(f"❌ Permission denied to access {workdir_path}")
    except Exception as e:
        print(f"❌ An unknown error occurred while changing directory: {e}")

def node_init() -> None:
    """
    Initializes the Node.js environment by running `npm init -y`.

    Args:
        None

    Returns:
        None

    This creates a default `package.json` file in the current directory.
    
    Example:
        node_init()
    """
    print("💡 Setting up the NodeJS environment...")
    result = subprocess.run("npm init -y", shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print("✅ Done.")
    else:
        print("❌ NodeJS setup terminated with errors.")
        print(f"💡 Error: {result.stderr}")

def folder_structure_setup() -> None:
    """
    Creates the default folder structure and necessary files for a Node.js project.

    Args:
        None

    Returns:
        None

    This function creates the following directories:
        - logs
        - views/
        - src/css/
        - src/js/
        - src/images/
        - src/fonts/

    It also creates two files:
        - `.env` (empty)
        - `.gitignore` with basic content:
          ```
          /node_modules
          /logs
          /.env
          ```
    
    Example:
        folder_structure_setup()
    """
    # creates default directories
    directories = [
        "views",
        "src/css",
        "src/js",
        "src/images",
        "src/fonts"
    ]

    for dir in directories:
        try:
            print(f"💡 Creating \"{dir}\" folder...")
            # exist_ok prevents errors if the folder already exists
            makedirs(dir, exist_ok=True)
            print("✅ Done.")
        except PermissionError:
            print("❌ Permission denied: You do not have the necessary permissions to create directories.")
        except OSError as e:
            print(f"❌ An error occurred while creating the \"{dir}\" directory: {e}")
        except Exception as e:
            print(f"❌ An unexpected error occurred while creating the \"{dir}\" directory: {e}")
    
    print("💡 Creating \".env\" file...")
    # create .env file
    with open(".env", 'w') as envFile:
        pass
    print("✅ Done.")

    print("💡 Creating \".gitignore\" file and writing in it...")
    # create and compiles .gitignore file 
    with open(".gitignore", 'w') as gitignoreFile:
        gitignoreFile.write("/node_modules\n")
        gitignoreFile.write("/logs")
        gitignoreFile.write(".env")
        
    print("✅ Done.")

def setup_workspace() -> None:
    """
    Initializes the workspace by running Node.js initialization and folder structure setup.

    Args:
        None

    Returns:
        None

    This calls `node_init()` and `folder_structure_setup()` in sequence to set up the project.
    
    Example:
        setup_workspace()
    """
    node_init()
    folder_structure_setup()

def run_command(command: str, workdir:str="") -> None:
    """
    Runs the provided shell command in the specified working directory.

    Args:
        command (str): The shell command to run (e.g., "npm install").
        workdir (str, optional): The directory in which the command should be executed. Default is the current directory.

    Returns:
        None

    This function first changes to the provided directory (if applicable) and sets up the workspace before running the command.
    
    Example:
        run_command("npm install lodash", workdir="/path/to/project")
    """
    if workdir != "":
        # normalizes input into an absolute path
        workdir = path.abspath(workdir)
        # moves to project directory
        move_to_workdir(workdir)
        # before installing packages, prepares the environment
        setup_workspace()
    
    print(f"💡 Running command: \"{command}\" ...")
    # runs the given command and saves the output in a result object with eventual error messagges and codes
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print("✅ Done.")
    else:
        print("❌ Execution terminated with errors.")
        print(f"💡 Error: {result.stderr}")
