#!/usr/bin/awk -f

BEGIN{FS = "\t";print "Only First Glyco Domain : ";}
{
  if($19==0 && $22==0)
    {
    # These conditional statements are to ensure that no entry is zero because It will distort the calculation of average by adding to total.
    if(total==0){ab1=ab1+1;}
    if(fincount==0){ab2=ab2+1;}
    if(foutcount==0){ab3=ab3+1;}
    if(flength==0){ab4=ab4+1;}
    if(lincount==0){ab5=ab5+1;}
    if(loutcount==0){ab6=ab6+1;}
    if(llength==0){ab7=ab7+1;}

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
    print "Average Length = " total/(NR-1-ab1)"\n";
    print "Average First Domain Length = " flength/(NR-1-ab4)"\n";
    print "Average First Domain In = " fincount/(NR-1-ab2) "\n";
    print "Average First Domain Out = " foutcount/(NR-1-ab3)"\n";
    print "Average Last Domain Length = " llength/(NR-1-ab7)"\n";
    print "Average Last Domain In = " lincount/(NR-1-ab5)"\n";
    print "Average Last Domain Out = " loutcount/(NR-1-ab6)"\n";
    print "FD/LENGTH = " ((flength/(NR-1-ab4))/(total/(NR-1)))*100"\n";
    print "LD/LENGTH = " ((llength/(NR-1-ab7))/(total/(NR-1)))*100"\n";

    }
