from functions.get_file_content import get_file_content


HOMEPATH = "calculator"

def main():
    print(get_file_content(HOMEPATH, "main.py"))
    print("===")
    print(get_file_content(HOMEPATH, "pkg/calculator.py"))
    print("===")
    print(get_file_content(HOMEPATH, "/bin/cat"))
    print("===")
    print(get_file_content(HOMEPATH, "pkg/not_real.py"))

if __name__ == "__main__":
    main()
