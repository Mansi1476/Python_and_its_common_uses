import re
import sys
def awk(filename,pattern,action):
    try:
        with open(filename,'r') as file:
            for line in file:
                if re.search(pattern,line):
                    eval(action)
    except FileNotFoundError:
        print(f"{filename}: no such file or directory")

def main ():
    filename = sys.argv[1]
    pattern = sys.argv[2]
    action = sys.argv[3]
    awk(filename,pattern,action)
 
if __name__ == '__main__':
    main()