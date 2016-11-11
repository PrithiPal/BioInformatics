import re
import time
import os 
import os.path


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
counter=0
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
            
            # print "here is a break in first loop %d " % (skipping1)
            
            break
    for line2 in open("mouse1_loopstat.txt","r") : 
        f = line2.split("\t")
        found = re.match(arr[0][count-1],f[0])
        if found:
            arr[2].append(f[2]) ##returns the protein length
            
            # print "here is a break in second loop %d " % (skipping2)
            break
    if not found : 
       # print "%s not found" % (fragment[0])
        arr[2].append("X")
        counter=counter+1
            
    seq_length = len(arr[4][count-1].split(" "))-1
    arr[3].append(seq_length) #returns the total_seq
    count=count+1;



print "time elapsed = %f"%(time.time() - start)
#print "a[0] = %d, a[1] = %d, a[2] = %d, a[3] = %d, a[4] = %d" % (len(arr[0]),len(arr[1]),len(arr[2]),len(arr[3]),len(arr[4]))
#print "not found number = %d" % (counter)


filename = raw_input("Please enter the Output File name : ")
print "Writing to the file."
if filename[:-4] != ".txt" : 
    filename = filename + ".txt"
fileToWrite = open(filename,"w")

for i in range(len(arr[0])-1) :
    if arr[2][i] != "X" : 
        data = str(arr[0][i]) + "\t" + str(arr[1][i]) + "\t" + str(arr[2][i]) + "\t" + str(arr[3][i]) + "\t" + str(arr[4][i])
        fileToWrite.write(data)
        
fileToWrite.close()


    
