#!/usr/bin/env python

import sys
import subprocess
import os

def main(username, password, commit_msg):
    current_folder = os.path.relpath('.', '..')
    url = "https://" + username + ":" + password + "@github.com/" + username + "/" + current_folder + ".git"

    command = "git add ."

    process = subprocess.Popen(command.split())
    output,error = process.communicate()

    command = "git commit -m"
    command = command.split()
    command.append("\"" + commit_msg + "\"")

    process = subprocess.Popen(command)
    output,error = process.communicate()


    command = "git push -u " + url

    process = subprocess.Popen(command.split())
    output,error = process.communicate()

if __name__ == '__main__':
    if(len(sys.argv) >= 4):
        username = sys.argv[1]
        password = sys.argv[2]
        commit_msg = sys.argv[3]
        main(username, password, commit_msg)
    else:
        print("please enter a commit name")
