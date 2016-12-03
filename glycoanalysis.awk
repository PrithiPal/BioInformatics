#!/usr/bin/awk -f

BEGIN{FS = "\t";print "Only First Glyco Domain : ";}
{
  if($19==0 && $22==0)
    {
    # These conditional statements are to ensure that no entry is zero because It will distort the calculation of average by adding to total.


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
#To prevent the miscalculation, the ideal formula for avg. should be = (SUM of FIELD VALUES)/(TOTAL - TIMES ZEROES OCCURS FOR FIELD)
    print "Total Count = " (NR-1)"\n";
    print "Average Length = " total/(NR-1)"\n";
    print "Average First Domain Length = " flength/(NR-1)"\n";
    print "Average First Domain In = " fincount/(NR-1) "\n";
    print "Average First Domain Out = " foutcount/(NR-1)"\n";
    print "Average Last Domain Length = " llength/(NR-1)"\n";
    print "Average Last Domain In = " lincount/(NR-1)"\n";
    print "Average Last Domain Out = " loutcount/(NR-1)"\n";
    print "FD/LENGTH = " ((flength/(NR-1))/(total/(NR-1)))*100"\n";
    print "LD/LENGTH = " ((llength/(NR-1))/(total/(NR-1)))*100"\n";

    }
