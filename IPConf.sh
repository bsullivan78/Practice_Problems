#!/bin/bash
sp=($(echo $1 | tr '.' '\n'))
b="True"
if [[ ${#sp[@]} -ne 4 ]] || [[ $1 == *' '* ]]; then
	b="False"
fi
for i  in "${sp[@]}" ; do
	if  [ $i -ge 0 ] && [ $i -le 255 ] 
	then
		if [ ${i:0:1} -eq "0" ]
		then
			b="False"
		fi
	else
		b="False"
	fi
done
echo $b