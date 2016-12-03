#!/bin/bash
file=$1
c1=$(awk '{if(substr($1,1,1) == ">"){print substr($1,6,13)}}' $file | wc -l)
echo $c1
