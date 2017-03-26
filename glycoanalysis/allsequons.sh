#!/bin/bash
filename=$1;
category=$2; #1 = onlyfirst,2 = onlylast, 3 = both, 4 = non_glyco

awk1=$(awk -v category=$2 'BEGIN{FS = "\t"}{
  if(category == 1){if($19!=0 && $22==0){print $6;}}
else if(category == 2){if($19==0 && $22!=0){print $6;}}
else if(category == 3){if($19!=0 && $22!=0){print $6;}}
else if(category == 4){if($19==0 && $22==0){print $6;}}
else if(category ==0){print $6;}
}' $filename > field6.txt);

awk2=$(awk 'BEGIN{FS = " ";RS = "\n";element =0;total =0;count=0;}
{
    for(i = 1;i<=NF;i++)
    {
      if(substr($i,length($i)) != 0)
      {
      element = substr($i,length($i));
      total=total+element;
      count=count+1;
      }


    }


}
END{
print "total = " total "\n";
print "count = " count "\n";
print "avg. all sequons = " count/total "\n";
}' field6.txt);


echo $awk2
