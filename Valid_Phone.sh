in=$1
if [ ${#in} -eq 14 ]; then
	if [[ ${in:0:10} == "("*") "*"-" ]]; then
		echo "True"
	else
		echo "False"
	fi
else
	echo "False"
fi
