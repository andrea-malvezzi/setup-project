from lib import handle_bundled_path, handle_path, load_packages, prepare_command, run_command

def main():
    paths = handle_bundled_path()
    PROJECT_PATH = handle_path(input("Enter the absolute path to get to the project folder: "))

    # prepare commands to install packages
    dev_command = prepare_command(load_packages(paths[0]), True)
    prod_command = prepare_command(load_packages(paths[1]))

    # run commands
    run_command(dev_command, PROJECT_PATH)
    run_command(prod_command)

    input("Press ENTER to exit the terminal. Happy coding! 👋")

if __name__ == "__main__":
    main()