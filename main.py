from lib import handle_path, load_packages, prepare_command, run_command

def main():
    DEV_PACKAGES_PATH = "./packages/dev.txt"
    PROD_PACKAGES_PATH = "./packages/prod.txt"
    PROJECT_PATH = handle_path(input("Enter the absolute path to get to the project folder: "))

    # prepare commands to install packages
    dev_command = prepare_command(load_packages(DEV_PACKAGES_PATH), True)
    prod_command = prepare_command(load_packages(PROD_PACKAGES_PATH))

    # run commands
    run_command(dev_command, PROJECT_PATH)
    run_command(prod_command)

    input("Press ENTER to exit the terminal. Happy coding! 👋")

if __name__ == "__main__":
    main()