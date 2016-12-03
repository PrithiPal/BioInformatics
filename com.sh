#!/bin/bash

filename=$1; #input file name

Total_fields=$(wc -l $filename); #total number of proteins in species file.
echo Total_fields = $Total_fields;
echo
echo Non-GlycoSylated :
echo

cmd=$(awk 'BEGIN{FS = "\t"}
{
  if($19==0 && $22==0)
    {
    count=count+1;
    total=total+$3;
    fincount=fincount+$15;
    foutcount=foutcount+$14;
    flength=flength+$13;
    lincount=lincount+$18;
    loutcount=loutcount+$17;
    llength=llength+$16

    }
}
END{
    print "Total Count = " count;print "\n";print "Average Length = " total/count ;print "Average First Domain In = " fincount/NR "\n";print "Average First Domain Out = " foutcount/NR "\n";print "Average First Domain Length = " flength/NR "\n";print "Average Last Domain In = " lincount/NR "\n";print "Average Last Domain Out = " loutcount/NR "\n";print "Average Last Domain Length = " llength/NR "\n";}' $filename);
echo $cmd;
