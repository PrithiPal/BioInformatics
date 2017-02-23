#This python script prepare the first input for the worm to be put in the loopstat cpp file. The second input is worm_transloop_output2.txt

## INPUT : peptide file, f_all_descriptions.txt worm_loopstat_input2_new-v1
## OUTPUT : t1[current].txt or worm_loopstat_input1

import time



def equal(str1, str2) : 
    if str1 == str2 : 
        return True
    else : 
        return False
    
def main() : 
    
    start_time = time.time()
    print "starting..."
    
    description_filename = 'f_all-v1.txt'
    worm_loopstat_input2_filename = 't2.txt'
    peptide_filename = 'peptide-v1.txt'
    output_filename = 't1-v1.txt'
    
    prepareEntry(output_filename,worm_loopstat_input2_filename,description_filename,peptide_filename)
    
    print "done!!"
    elapsed_time = time.time() - start_time
    print "time elapsed = " + str(elapsed_time)


def prepareEntry(output_file,worm_loopstat_input2_filename,description_filename,peptide_filename) : 
    arr = []
    for i in range(5) : 
        arr.append([]) ## creates the 5 columns for the data 
    identifier = ""
    descr_identifier = ""
    description = ""
    protein_length = ""

    ofile = open(str(output_file),"w")
    
    for lines in open(str(peptide_filename),"r") : 
    
        frag1 = lines.split("\t")
        frag2 = lines.split(" ")
        identifier = frag1[0]
        seq_list = frag1[1]
        total_seq = len(frag1[1].split(" "))-1
        
        description = findDescription(str(description_filename),identifier)
        protein_length = findProteinLength(str(peptide_filename),identifier)
        
            
        print_this = str(identifier) + "\t" + str(description) + "\t" + str(protein_length)[:-1]  + "\t" + str(total_seq) + "\t" + seq_list
        print print_this
        ofile.write(print_this)
    




    
def findDescription(filename,identifier) : 
    description = ""
    for line in open(str(filename),"r") : 
        frag = line.split("\t")
            
        if str(identifier) == str(frag[0]) : 
            description = frag[1][:-1] #don't include line carriage return
            if description is "" : 
                description = "no description"
            break
    return description
    
def findProteinLength(filename,identifier) : 
    
    protein_length = ""
    for line in open(str(filename),"r") : 
        frag = line.split("\t")
        
        if str(identifier) == str(frag[0]) : 
            protein_length = str(frag[1])
            break  
    return protein_length
    

    
if __name__ == "__main__" : 
    main()


