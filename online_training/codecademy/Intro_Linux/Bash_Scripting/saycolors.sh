#!/bin/bash

# Is a special variable in Bash that represents
# the number of arguments passed to the script. If it 
# equals 0, it means no arguments were provided.
if [ $# -eq 0 ] 
then 
    echo "No colors provided"
else
    # "$@" is a special variable that represents all the 
    # arguments passed to the script. The script iterates 
    # over each argument and prints it.
    for color in "$@"
    do 
        echo "Color: $color"
    done
fi
