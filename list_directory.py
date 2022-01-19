import argparse
from os import listdir, curdir, scandir
parser = argparse.ArgumentParser(description = "create text file with contents of directory")

parser.add_argument('directory', type=str, nargs = "?", help='file location relative to home directory', default = curdir)

parser.add_argument('home', type=str, nargs = "?", help='lists paths relative to this directory', default = "")

args = parser.parse_args()

directory = args.directory
home = args.home
#contents = listdir(home + directory)
prefix = f"{directory}/"

with open("contents.txt", 'w') as file:
    for path in scandir(home + directory):
        filename = path.name
        #maybe change this in the future to check for other extensions
        if filename.partition(".")[-1] == "jpg":
            file.write(prefix + filename + "\n")

