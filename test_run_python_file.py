from functions.run_python_file import run_python_file


HOMEPATH = "calculator"
def main():
    print(run_python_file(HOMEPATH, "main.py"))
    print("===")
    print(run_python_file(HOMEPATH, "main.py", ["3 + 5"]))
    print("===")
    print(run_python_file(HOMEPATH, "tests.py"))
    print("===")
    print(run_python_file(HOMEPATH, "../main.py"))
    print("===\nCannot execute \"../main.py\" as it is outside")
    print(run_python_file(HOMEPATH, "nonexistent.py"))
    print("===")
    print(run_python_file(HOMEPATH, "lorem.txt"))


if __name__ == "__main__":
    main()
