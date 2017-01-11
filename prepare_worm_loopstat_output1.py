#This python script prepare the first input for the worm to be put in the loopstat cpp file. The second input is worm_transloop_output2.txt
#format in arr : <identifer> <description> <length> <total_seq.> <seq.list>

arr = []
ofile = open("worm_loopstat_input1.txt","w")
for i in range(5) : 
    arr.append([]) ## creates the 5 columns for the data 
#identifer = ""
#description = ""
#protein_length = ""
for lines in open("peptide_worm_output.txt","r") : 
    description = ""
    protein_length = ""
    frag1 = lines.split("\t")
    frag2 = lines.split(" ")
    identifier = str(frag1[0])
    seq_list = frag1[1]
    total_seq = len(frag1[1].split(" "))-1
    
    for line2 in open("f_all_descriptions.txt","r") :  ## retrieval of description from this file 
        frag3 = line2.split("\t")
        
        if identifier == frag3[0] : 
            print "first conditional true"
            description =  frag3[1][:-1] # cuts of the end "\n" character 
            break
    for line3 in open("worm_loopstat_input2.txt","r") :  ## retreival of protein length from 
        frag4 = line3.split("\t")
        if identifier == frag4[0] : 
            print "second conditional true"
            protein_length = frag4[1]
            break
    print_this = str(identifier) + "\t" + str(description) + "\t" + str(protein_length)  + "\t" + str(total_seq) + "\t" + seq_list
    print print_this
    ofile.write(print_this)
    
