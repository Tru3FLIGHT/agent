from functions.get_files_info import get_files_info

seperator = "===="

home_filepath = "/home/zalea/Documents/Projects/bootdev/assignments/agent/calculator"
def main():
     
    print(get_files_info(home_filepath, "."))
    print(seperator)
    print(get_files_info(home_filepath, "pkg"))
    print(seperator)
    print(get_files_info(home_filepath, "/bin"))

if __name__ == "__main__":
    main()
