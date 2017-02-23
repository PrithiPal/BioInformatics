#This python script prepare the first input for the worm to be put in the loopstat cpp file. The second input is worm_transloop_output2.txt

## INPUT : peptide file, f_all_descriptions.txt worm_loopstat_input2_new-v1
## OUTPUT : t1[current].txt or worm_loopstat_input1



# This is reused for the mouse first_loopstat_prepare.py
import time
print "starting..."


    
##--------------------------------------------------------------------------------

def main() : 
    
    start_time = time.time()
    
    MOUSE_DESCRIPTION_INDEX = 1
    MOUSE_PROTEIN_L_INDEX = 2
    
    
    
    
    mouse_description_filename = 'mouse_human.fasta.txt'
    mouse_peptide_filename = 'peptide-v1.txt'
    mouse_output_filename = 't1[current]-v1.txt'
    mouse_protein_l_filename = 'mouse1_loopstat.txt'
    
    prepareEntry(mouse_output_filename,mouse_description_filename,mouse_protein_l_filename,mouse_peptide_filename,MOUSE_DESCRIPTION_INDEX,MOUSE_PROTEIN_L_INDEX)


    print "done!!"
    elapsed_time = time.time() - start_time
    print "time elapsed = " + str(elapsed_time)


##--------------------------------------------------------------------------------

def prepareEntry(output_file,description_filename,protein_l_filename,peptide_filename,DESCRIPTION_INDEX,PROTEIN_L_INDEX) : 
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
        
        description = findDescription(str(description_filename),identifier,DESCRIPTION_INDEX)
        protein_length = findProteinLength(str(protein_l_filename,),identifier,PROTEIN_L_INDEX)
        
            
        print_this = str(identifier) + "\t" + str(description) + "\t" + str(protein_length)  + "\t" + str(total_seq) + "\t" + seq_list
        print print_this
        ofile.write(print_this)
    
##--------------------------------------------------------------------------------
    
def findDescription(filename,identifier,DESCRIPTION_INDEX) : 
    description = ""
    for line in open(str(filename),"r") : 
        frag = line.split("\t")
            
        if str(identifier) == str(frag[0]) : 
            description = frag[int(DESCRIPTION_INDEX)][:-1] #don't include line carriage return
            if description is "" : 
                description = "no description"
            break
    return description
    
##--------------------------------------------------------------------------------

def findProteinLength(filename,identifier,PROTEIN_L_INDEX) : 
    
    protein_length = ""
    for line in open(str(filename),"r") : 
        frag = line.split("\t")
        
        if str(identifier) == str(frag[0]) : 
            protein_length = str(frag[int(PROTEIN_L_INDEX)])
            break  
    return protein_length
    
##--------------------------------------------------------------------------------
def equal(str1, str2) : 
    if str1 == str2 : 
        return True
    else : 
        return False

##--------------------------------------------------------------------------------
if __name__ == "__main__" : 
    main()
    



