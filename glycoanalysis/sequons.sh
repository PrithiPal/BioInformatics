#!/bin/bash
filename=$1;
category=$2; #1 = onlyfirst,2 = onlylast, 3 = both, 4 = none

awk1=$(awk -v category=$2 'BEGIN{FS = "\t";count=0;}{
  if(category == 1){if($19!=0 && $22==0 && NR > 1){cat="onlyfirst";print $6;}}
else if(category == 2){if($19==0 && $22!=0 && NR > 1){cat="onlylast";print $6;}}
else if(category == 3){if($19!=0 && $22!=0 && NR > 1){cat="both";print $6;}}
else if(category == 4){if($19==0 && $22==0 && NR > 1){cat="none";print $6;}}
else if(category ==0){cat="overall";print $6;}
}END{print cat}' $filename > field6.txt);

awk2=$(awk 'BEGIN{FS = " ";RS = "\n";total1 = 0;total2 = 0;count1 = 0;count2 = 0;element=0;total=0;count=0;}
{
    if(substr($1,length($1))!=0)
    {
      element1 = substr($1,length($1));
      total1=total1+element1;
      count1=count1+1;
    }
    if(substr($(NF),length($(NF)))!=0)
    {
      element2 = substr($(NF),length($(NF)));
      total2=total2+element2;
      count2=count2+1;
    }
    for(i =1;i<=NF;i++)
    {
      if(substr($i,length($(i))) != 0)
      {
        element = substr($i,length($(i)));
        total=total+element;
        count=count+1;
      }

    }


}

END{
if(count1!=0){firstavg = total1/count1;} 
if(count2!=0){secavg = total2/count2;}
firstandlastavg = (firstavg + secavg)/2; 
all = total/count; 
if(category == 1){cat = "OnlyFirstGlyco"}
else if(category == 2){cat = "OnlyLastGlyco"}
else if(category == 3){cat = "BothGlyco"}
else if(category == 4){cat = "NoneGlyco"}
else if(category == 0){cat = "Overall"}
print $cat"\n"
print "Avg. No. of Seq(F&L) = " firstandlastavg;
print "Avg. No. of Seq.(All) = " all;
}' field6.txt);


echo $awk2
