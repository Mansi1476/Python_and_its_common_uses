import re
import sys
def grep(filename):
    pattern = "hello"
    try:
        with open(filename,'r') as file:
            for line in file:
                if re.search(pattern, line):
                    print(line)
    except FileNotFoundError:
        print(f"{filename}: no such file or directory")

def main():
    for filename in sys.argv[1:]:
        grep(filename)


if __name__ == '__main__':
    main()