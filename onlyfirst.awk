#!/usr/bin/awk -f

BEGIN{FS = "\t";print "Only First Glyco Domain ";print "";}
{
  if($19!=0 && $22==0)
    {
    # These conditional statements are to ensure that no entry is zero because It will distort the calculation of average by adding t$

    count=count+1;
    total=total+$3;
    fincount=fincount+$15;if($15!=0){fintotal=fintotal+1;}
    foutcount=foutcount+$14;if($14!=0){fouttotal=fouttotal+1;}
    flength=flength+$13;if($13!=0){flengthtotal=flengthtotal+1;}
    lincount=lincount+$18;if($18!=0){lintotal=lintotal+1;}
    loutcount=loutcount+$17;if($17!=0){louttotal=louttotal+1;}
    llength=llength+$16;if($16!=0){llengthtotal=llengthtotal+1;}

    }
}

END{
#To prevent the miscalculation, the ideal formula for avg. should be = (SUM of FIELD VALUES)/(TOTAL - TIMES ZEROES OCCURS FOR FIELD)
    print "Total Count = " count-1 "\n";
    print "Average Length = " total/(count-1) "\n";
    print "Average First Domain Length = " flength/(flengthtotal-1) "\n";
    print "Average First Domain In = " fincount/(fintotal-1) "\n";
    print "Average First Domain Out = " foutcount/(fouttotal-1)"\n";
    print "Average Last Domain Length = " llength/(llengthtotal-1)"\n";
    print "Average Last Domain In = " lincount/(lintotal-1)"\n";
    print "Average Last Domain Out = " loutcount/(louttotal-1)"\n";
    print "FD/LENGTH = " ((flength/(flengthtotal-1))/(total/(count-1)))*100"\n";
    print "LD/LENGTH = " ((llength/(llengthtotal-1))/(total/(count-1)))*100"\n";

  }
