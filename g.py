#!/usr/bin/python3

import sys

# my files
import init
import add

if __name__ == '__main__':
	arg = sys.argv[1]

	if arg == "init":
		init.init();
	if arg == "add":
		filename = sys.argv[2]
		add.add(filename);
