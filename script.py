import re
## creates the two-dimensional array
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
count=0
## puts the ipi in the first column of the array
for line in open("peptide_o.txt","r") : 
    fragment = line.split("\t")
    arr[0].append(fragment[0])
    arr[1].append(fragment[1])
    
    for line2 in open("mouse_qualitative.txt","r") : 
        f = line2.split("\t")
        found = re.match(arr[0][count-1],f[0])
        if found : 
            arr[1][count-1] = f[1] ## return the description 


for line in open("mouse1_loopstat.txt","r") : 
    f = line.split("\t")
    print f[0]