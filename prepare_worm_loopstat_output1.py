#This python script prepare the first input for the worm to be put in the loopstat cpp file. The second input is worm_transloop_output2.txt


#format in arr : <identifer> <description> <length> <total_seq.> <seq.list>
arr = []
for i in range(5) : 
    arr.append([]) ## creates the 5 columns for the data 

identifer = ""
description = ""

for lines in open("peptide_worm_o.txt","r") : 
    frag1 = lines.split("\t")
    frag2 = lines.split(" ")
    identifier = frag1[0]
    seq_list = frag2[1]
    print seq_list
    
    
    
    #for line2 in open("f_all_descriptions.txt","r") : 
    #    frag2 = line2.split("\t")
    #    if (identifer == frag2[0]) : 
    #        description =  frag2[1]
            
    
