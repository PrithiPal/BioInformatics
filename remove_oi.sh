#!/bin/bash
#This file removes the lines from transloop_input files which have topologies "o" or "i".

filename=$1; #input file name
path=$(pwd);
ofilename=$2; #output file name
initial_lines=$(wc -l path/$filename);
echo Initially $filename has $initial_lines lines.

cmd1=$(grep -vw "o\|i" $filename > path/$ofilename);

echo $cmd;
final_lines=$(wc -l path/$ofilename);
echo Finally $ofilename has $final_lines lines.
echo The output is in $ofilename
