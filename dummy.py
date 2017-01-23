

def readPeptideFile(filename) : 
    arr = []
    for i in range(3) : 
        arr.append([])
    counter=0
    
    for lines in open(filename,'r') : 
        frag1 = lines.split("\t")
        frag2 = lines.split(" ")
        
        identifier = frag1[0]
        seq_list = frag1[1]
        total_seq = len(frag1[1].split(" "))-1
        
        arr[0].append(identifier)
        arr[1].append(seq_list)
        arr[2].append(total_seq)
    
    return arr



def readDescriptionFile(filename,identifier) : 
    arr = []
    for line2 in open("f_all_descriptions.txt","r") : 
        frag3 = line2.split("\t")
        
        if str(identifier) == " " + str(frag3[0]) : 
            description = frag3[1][:-1]
            if description is "" : 
                description = "no description"
            arr.append(description)
            break
    return arr

desc = readDescriptionFile('f_all_descriptions.txt')
for i in range(len(desc)) : 
    print desc[i]

    
   
