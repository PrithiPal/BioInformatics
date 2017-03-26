#!/usr/bin/awk -f

BEGIN{FS = "\t";print " Non- Glycosylation :  ";print "";}
{
count=count+1;
total=total+$2;
fincount=fincount+$10;if($10!=0){fintotal=fintotal+1;}
foutcount=foutcount+$9;if($9!=0){fouttotal=fouttotal+1;}
flength=flength+$8;if($8!=0){flengthtotal=flengthtotal+1;}
lincount=lincount+$13;if($13!=0){lintotal=lintotal+1;}
loutcount=loutcount+$12;if($12!=0){louttotal=louttotal+1;}
llength=llength+$11;if($11!=0){llengthtotal=llengthtotal+1;}



}
END{
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
