#!/bin/bash

path="/home/delkov/Documents/MOSCOW/ECO_COMPLETE/scp"



## MAY BE remove if condition

while true
do
	for entry in "$path"/*.txt
		do
			if [ -f "$entry" ]
			then
	  			scp "$entry" delkov@79.164.131.110:/home/delkov/Desktop/scp && rm -f "$entry"
				# echo "$file found.";
			else
				echo "No files";
			fi
		done
	sleep 1
done