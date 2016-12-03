#!/bin/bash
input_file=$1
output_file=$2
if [ $# != 2 ]; then
  print "Usage: ./replace_with_hash.sh [inputfile] [outputfile]"
fi

c1 = $(awk '{gsub(/\*/,"#");print }' $input_file > $output_file)
echo "output in " $output_file "."
