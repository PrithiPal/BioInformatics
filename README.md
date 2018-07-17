Visit Wiki for Project Overview.

# Glycoanalysis

### Preview

Glycoanalysis is the compilation of statistics after obtaining the final Loopstat outputs.  
Below is the required format for the presentation of statistics\(One Table for each species\) 

### ![](/assets/table.jpg)

### Explanation

Non-Glycosylation statistics are obtainable from non\_glyco\_file for each species. For the rest, refer to the .awk programmes below to obtain the stats.

> $19 = FirstDomain.Glyco.Length
>
> $21 = LastDomain.Glyco.Length

Based on the values of the above fields, four categories are possible:

> onlyfirst.awk : if $19!=0 && $22==0
>
> onlylast.awk : if $19==0 && $22!=0
>
> both.awk : if $19!=0 && $22!=0
>
> none.awk : if $19==0 && $22==0
>
> overall.awk : all
>
> sequons.sh \[filename\] \[category\] : For the stastics of AvgSeq\(F&L\) and AvgSeq\(All\)

### Steps

1. Store all files mentioned above in one directory along with the firstLoopstatOutput. Make this directory as current.

2. Runs all statistics on the mouseloopstatoutput1 file.

`ls | grep ".awk" | sort | xargs -n1 -i {} sh -c './{} mouseLoopstatOutput1'`

1. Runs the sequons statistics for the mouse1loopstatoutput1 File.

`for i in {0..4};do ./sequons.sh mouseLoopstatOutput1 $i; done`

1. The Non-glycol statistics are likely to remain unchanged because only Sequons information is altered during the creation of theoretical data from experimental data.

At the end NL\(onlyfirst\) + NL\(onlylast\) + NL\(both\) + NL\(last\) = NL\(overall\)

