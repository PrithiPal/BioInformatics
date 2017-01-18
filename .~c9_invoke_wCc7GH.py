#This python script prepare the first input for the worm to be put in the loopstat cpp file. The second input is worm_transloop_output2.txt
#format in arr : <identifer> <description> <length> <total_seq.> <seq.list>
import time
print "starting..."


def equal(str1, str2) : 
    if str1 == str2 : 
        return True
    else : 
        return False
    

start_time = time.time()
arr = []
ofile = open("t1.txt","w")
for i in range(5) : 
    arr.append([]) ## creates the 5 columns for the data 
#identifer = ""
identifier = ""
descr_identifier = ""
description = ""
protein_length = ""
for lines in open("peptide_worm_output_after_removeextra.txt","r") : 

    frag1 = lines.split("\t")
    frag2 = lines.split(" ")
    identifier = frag1[0]
    seq_list = frag1[1]
    total_seq = len(frag1[1].split(" "))-1
    
    for line2 in open("f_all_descriptions.txt","r") : 
        frag3 = line2.split("\t")
        
        if str(identifier) == " " + str(frag3[0]) : 
            description = frag3[1][:-1]
            if description is "" : 
                description = "no description"
            break
    
    for line3 in open("t2.txt","r") : 
        frag4 = line3.split("\t")
        
        if str(identifier) == " " + str(frag4[0]) : 
            protein_length = frag4[1]
            break
        
    print_this = str(identifier[1:]) + "\t" + str(description) + "\t" + str(protein_length)  + "\t" + str(total_seq) + "\t" + seq_list
    print print_this
    ofile.write(print_this)
    
print "done!!"
elapsed_time = time.time() - start_time
print "time elapsed = " + str(elapsed_time)


