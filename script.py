def correctWormFastaInput(wormfile,outputfile) : 
    arr = []
    count = 0
    for line in open(wormfile,"r") : 
        if line[0] == ">" : 
            
            fragments = line.split("\t")
            line = line.replace("\t"," ")
            initial = fragments[0]
            fragments[0] = fragments[0].replace(">",">sp|")
            fragments[0] = fragments[0] + "|" + fragments[1]
            rep = fragments[0]
            line = line.replace(fragments[1],"")
            line = line.replace(initial,rep)
           # print line
            arr.append(line)
            count=count+1
        else : 
          #  print line
            
            arr.append(line)
    
    
    
    file = open(outputfile,"w")
    
    for i in range(len(arr)-1) : 
       
        file.write(arr[i])
        
    counter=1
    for line in open(outputfile) : 
        print str(counter) + " line = " + str(len(line))
        counter=counter+1
        
## function ends here

correctWormFastaInput("original_worm.fasta","worm_output.fasta")