#!/bin/bash

# Very simple controller script, needs to be modified depending on machine

# export PYTHONPATH="${PYTHONPATH}:/home/dk/Documents/misc_programs/gutenberg_text_analysis/src"

if [ $1 == "test" ];
then
    cd ../src
    pytest 
    cd ../scripts
fi
