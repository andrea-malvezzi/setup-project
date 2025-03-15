from lib import check_ts, setup_ts, handle_bundled_path, handle_path, load_packages, prepare_command, run_command

def main():
    # ask for ts or js
    # ts flag or just another function? (or both)
    paths = handle_bundled_path()

    PROJECT_PATH = handle_path(input("Enter the absolute path to get to the project folder: "))

    ts_flag = check_ts()
    if (ts_flag):
        setup_ts(paths[2], PROJECT_PATH)

    # prepare commands to install packages
    dev_command = prepare_command(load_packages(paths[0]), True)
    prod_command = prepare_command(load_packages(paths[1]))

    # run commands
    if (ts_flag):
        run_command(dev_command)
    else:
        run_command(dev_command, PROJECT_PATH)
    run_command(prod_command)

    input("Press ENTER to exit the terminal. Happy coding! 👋")

if __name__ == "__main__":
    main()