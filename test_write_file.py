from functions.write_file import write_file


HOMEPATH = "calculator"
def main():
    print(write_file(HOMEPATH, "lorem.txt", "wait, this isn't lorem ipsum"))
    print("===")
    print(write_file(HOMEPATH, "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    print("===")
    print(write_file(HOMEPATH, "/tmp/temp.txt", "should fail"))


if __name__ == "__main__":
    main()
