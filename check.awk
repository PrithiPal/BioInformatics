#!/usr/bin/awk -f

BEGIN{FS = "\t"}
{
if($3==0) # protein length
{count1=count1+1;}
if($15==0) #first domain in
{count2=count2+1;}
if($14==0) #first domain out
{count3=count3+1;}
if($13==0) #first domain length
{count4=count4+1;}
if($18==0) #last domain in
{count5=count5+1;}
if($17==0) #last domain out
{count6=count6+1;}
if($16==0) #last domain length
{count7=count7+1;}
}
END {

print "no. of rows with null :  \n";
print "protein length : " count1"\n";
print "first domain in : " count2"\n";
print "first domain out : " count3"\n";
print "first domain length: " count4"\n";
print "last domain in : " count5"\n";
print "last domain out: " count6"\n";
print "last domain length :" count7"\n";



}
