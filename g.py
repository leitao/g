#!/usr/bin/python3

import sys

# my files
import init
import add

if __name__ == '__main__':
    arg = sys.argv[1]

    if arg == "init":
        init.init();
    elif arg == "add":
        filename = sys.argv[2]
        add.add(filename);
    elif arg == "diff":
        print("diff: Diff files")
    else:
        print(sys.argv[0], "Usage:")
        print("Options:\n")
        print("\tinit: Initiate a bare repository")
        print("\tadd: Add a file")
        print("\tTBD")
