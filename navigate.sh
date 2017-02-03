#!/bin/bash

if [ $# -eq 0 ];
then
	echo "please enter in a command-line argument"
elif [ $1 = notes ]
then
	cd /mnt/c/Users/rsymi/OneDrive\ -\ mail.uoguelph.ca/University\ of\ Guelph/Year\ 2/Winter\ 2017/Notes;
elif [ $1 = programming ]
then
	cd /mnt/c/Programming
fi
