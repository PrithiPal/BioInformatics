import re
import time
import os 
## creates the two-dimensional array
filename = raw_input("Please enter the Output File name : ")
if filename[:-4] != ".txt" : 
    filename = filename + ".txt"
fileToWrite = open(filename,"w")

def binary_search(array, target):
    lower = 0
    upper = len(array)
    while lower < upper:   # use < instead of <=
        x = lower + (upper - lower) // 2
        val = array[x]
        if target == val:
            return x
        elif target > val:
            if lower == x:   # this two are the actual lines
                break        # you're looking for
            lower = x
        elif target < val:
            upper = x

arr = []
for i in range(0,5) : 
    arr.append([])
count=1
skipping1 = 0
skipping2 = 0
start = time.time()
## puts the ipi in the first column of the array
for line in open("peptide_o.txt","r") : 
    fragment = line.split("\t")
    arr[0].append(fragment[0])
    arr[4].append(fragment[1])
    
    for line1 in open("mouse_qualitative.txt","r") : 
        f = line1.split("\t")
        found = re.match(arr[0][count-1],f[0])
        if found : 
            arr[1].append(f[1]) ## return the description 
            skipping1 = skipping1 +1 
            print "here is a break in first loop %d " % (skipping1)
            break
    for line2 in open("mouse1_loopstat.txt","r") : 
        f = line2.split("\t")
        found = re.match(arr[0][count-1],f[0])
        if found:
            arr[2].append(f[2]) ##returns the protein length
            skipping2 = skipping2 + 1
            print "here is a break in second loop %d " % (skipping2)

            break
    seq_length = len(arr[4][count-1].split(" "))-1
    arr[3].append(seq_length) #returns the total_seq
    count=count+1;

print "time elapsed = %f"%(time.time() - start)

print "a[0] = %d, a[1] = %d, a[2] = %d, a[3] + %d, a[4] = %d" % (len(arr[0]),len(arr[1]),len(arr[2]),len(arr[3]),len(arr[4]))



    
