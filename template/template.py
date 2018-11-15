#!/usr/bin/env python

import sys
import os

loc = ""

def main(command):
    try:
        with open(loc + "templates/" + command) as file:
            print(file.read())
    except(IOError) as e:
        print("template does not exist")

if __name__ == '__main__':
    if len(sys.argv) <= 2:
        sys.exit("please enter template name or --help")

    command = 0
    if len(sys.argv) >= 3:
        command = sys.argv[2]
        loc = sys.argv[1]
    else:
        command = sys.argv[1]

    if command == "-h":
        files = os.listdir(loc + "templates")
        print("TEMPLATES\n---------")
        for file in files:
            print(file)
    else:
        main(command)
