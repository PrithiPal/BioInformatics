count=0
for line in open("worm_output.fasta","r") : 
    if count <=2 : 
        if line[0][0] == ">" : 
            count=count+1
        print line + " len = " + str(len(line))
    
