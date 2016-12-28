#!/bin/bash

list()
{
	list=($(curl -u $1 https://api.github.com/user/repos))
	
	for (( i = 0; i < ${#list[*]}; ++ i ));
	do
		if echo "${list[$i]}" | grep -q "full_name"; then
		  echo ${list[$i+1]};
		fi
	done
	
	# "name":
}

create()
{
	read -p "what would you like the name of your new repository to be? " NAME
	if [ ! -z $NAME ];
	then
		curl -u $1 https://api.github.com/user/repos -d "{\"name\":\"$NAME\"}" >/dev/null
	fi
}

remove()
{
	read -p "what repo are you trying to remove? " NAME
	if [ ! -z $NAME ];

	token=$(</home/ryan/useful_stuff/token)
	echo $token
	then
		curl -X DELETE -H 'Authorization: token '$token https://api.github.com/repos/rsymingt/$NAME
	fi
}

main()
{
	read -p "enter your github username: " USER
	
	while true
	do	
		read -p "type 'list', 'create', 'remove' or 'q': " choice
		if [ ${choice:=nothing} = list ];
			then 
			# grab information from github
			list $USER;

			elif [ $choice = create ]
			then
			#create repo
			create $USER;

			elif [ $choice = remove ]
			then
			#remove repo
			remove $USER;
			elif [ $choice = q ]
			then
			break;
		fi
	done
}

main;
