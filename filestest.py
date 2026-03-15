from get_files_info import get_files_info

home_filepath = "/home/zalea/Documents/Projects/bootdev/assignments/agent"
def main():
    output = get_files_info(home_filepath, home_filepath) 
    print(output)


if __name__ == "__main__":
    main()
