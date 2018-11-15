#!/usr/bin/env python

import sys
import os

def main(command):
    try:
        with open("templates/" + command) as file:
            print(file.read())
    except(IOError) as e:
        print("template does not exist")

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        sys.exit("please enter template name or --help")
    command = sys.argv[1]
    if command == "--help":
        files = os.listdir("templates")
        print("TEMPLATES\n---------")
        for file in files:
            print(file)
    else:
        main(command)
