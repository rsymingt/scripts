#!/usr/bin/env python

import sys
import subprocess
import os
import json
from os.path import expanduser

credentials = expanduser("~") + "/.credentials"

def save(username, password):
    commit_msg = input("enter in commit: ")
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

def pull():
    print("test")

def help():
    print("test")

commands = {'-s': save, '-p': pull, '-h': help}

def main():
    is_cred = os.path.isfile(credentials)
    command = 0

    if len(sys.argv) < 2:
        sys.exit('please enter <option> <arguments>')

    command = sys.argv[1]
    if command not in commands:
        sys.exit("\"" + command + "\" does not exist, type -h for list of commands")

    if is_cred:
        with open(credentials) as json_data:
            creds = json.load(json_data)
            if all (key in creds for key in ("username", "password")):
                username, password = creds['username'], creds['password']
            else:
                print("error in creds in ~/.credentials")
        save(username, password)
    else:
        if(len(sys.argv) >= 4):
            username = sys.argv[1]
            password = sys.argv[2]
            commit_msg = sys.argv[3]
            # save(username, password, commit_msg)
        else:
            print("please enter <username> <password>")

if __name__ == '__main__':
    main();
