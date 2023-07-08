import sys
def sort(filename):
    try:
        with open(filename,'r') as file:
            lines = file.readlines()
            sorted_lines = sorted(lines)
            for line in sorted_lines:
                print(line)
    except FileNotFoundError:
        print(f"{filename}: no such file or directory")

def main ():
    filename = sys.argv[1]
    sort(filename)

if __name__ == '__main__':
    main()
