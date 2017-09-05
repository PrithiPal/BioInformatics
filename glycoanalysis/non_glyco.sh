#!/bin/bash
filename=$1;
initial_lines=$(wc -l ~/desktop/real/$filename);
lines_in_glyco=$(wc -l ~/desktop/N-glyco/$filename);
echo "initial_lines = " $initial_lines;
command=$(awk '{print $1}' ~/desktop/N-glyco/$filename | xargs -I {} sed -i.txt '/{}/d' ~/desktop/real/$filename);
echo $command;
final_lines=$(wc -l ~/desktop/real/$filename);
echo "final_lines = (original)" $final_lines;
echo "lines_in_glyco = " $lines_in_glyco;
