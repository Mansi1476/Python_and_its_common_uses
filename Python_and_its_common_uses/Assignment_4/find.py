import os
import sys
def find(directory, expression):
    try:
        for root,dirs,files in os.walk(directory):
            for file in files:
                path = os.path.join(root, file)
                if eval(expression):
                    print(path)
    except IsADirectoryError:
        print(f"no such file or directory")

def main ():
    directory = sys.argv[1]
    expression = sys.argv[2]
    find(directory,expression)

if __name__ == '__main__':
    main()