import sys

def cat(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print(f"cat: {filename}: No such file or directory")


def main():
    if len(sys.argv) < 2:
        print("Usage: python cat.py [file1] [file2] ...")
        return

    for filename in sys.argv[1:]:
        cat(filename)

if __name__ == '__main__':
    main()
