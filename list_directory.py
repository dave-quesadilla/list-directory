import argparse
from os import listdir, curdir
parser = argparse.ArgumentParser(description = "create text file with contents of directory")
parser.add_argument('directory', type=str, nargs = "?", help='file location relative to current directory', default = curdir)

args = parser.parse_args()

directory = args.directory
contents = listdir(directory)
prefix = f"{directory}\\"
with open("contents.txt", 'w') as file:
    file.write(prefix + f"\n{directory}\\".join(contents))
    
print(prefix + f"\n{directory}\\".join(contents))
