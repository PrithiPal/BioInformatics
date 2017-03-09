#This python script prepare the first input for the worm to be put in the loopstat cpp file. The second input is worm_transloop_output2.txt

## INPUT : peptide file, f_all_descriptions.txt worm_loopstat_input2_new-v1
## OUTPUT :  worm_loopstat_input1

import time
import unittest
import re 
#------------------------------------
def equal(str1, str2) : 
    if str1 == str2 : 
        return True
    else : 
        return False
#------------------------------------    

def main() : 
    
    start_time = time.time()
    print "starting..."
    
    description_filename = 'f_all-v1.txt'
    worm_loopstat_input2_filename = 'worm_loopstat_input2_new-v1.txt'
    peptide_filename = 'peptide-v1_uniq.txt'
    output_filename = 't1-v1.txt'
    
    prepareEntry(output_filename,worm_loopstat_input2_filename,description_filename,peptide_filename)
    
    print "done!!"
    elapsed_time = time.time() - start_time
    print "time elapsed = " + str(elapsed_time)

#------------------------------------

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
        
        DESCRIPTION_INDEX = 1
        PROTEIN_L_INDEX = 1
        
        description = findDescription(str(description_filename),str(identifier),DESCRIPTION_INDEX)
        protein_length = findProteinLength(str(worm_loopstat_input2_filename),identifier,PROTEIN_L_INDEX)
        
            
        print_this = str(identifier) + "\t" + str(description) + "\t" + str(protein_length) + "\t" + str(total_seq) + "\t" + seq_list
        print print_this
        ofile.write(print_this)
    

#------------------------------------

def findDescription(filename,identifier,DESCRIPTION_INDEX) : 
    description = ""
    
    for line in open(str(filename),"r") : 
        
        frag = line.split("\t")
        if str(identifier) == str(frag[0]) : 
            description = frag[int(DESCRIPTION_INDEX)][:-1] #don't include line carriage return
           # print "desc : ",description
            if description is "" or description is None  : 
                description = "no description"
            break
        else : 
            description = "no description found"
    #print "desc : ",description," for ",identifier
    return description
    
#------------------------------------

def findProteinLength(filename,identifier,PROTEIN_L_INDEX) : 
    
    protein_length = ""
    for line in open(str(filename),"r") : 
        frag = line.split("\t")
        
        if str(identifier) == str(frag[0]) : 
            protein_length = str(frag[int(PROTEIN_L_INDEX)])
            break  
    return protein_length
    

#------------------------------------

class Test(unittest.TestCase) : 
    
    def test_description(self) : 
        
        sample_file = "f_description-v1.txt"
        desc = findDescription(sample_file,"C05G5.4",1)
        #o = "Probable succinyl-CoA ligase [ADP/GDP-forming] subunit alpha, mitochondrial OS=Caenorhabditis elegans"
        print desc
        #self.assertTrue(desc == o)
        
        
    def test_prepareEntry(self) : 
        
        description_filename = 'f_all-v1.txt'
        worm_loopstat_input2_filename = 'worm_loopstat_input2_new-v1.txt'
        peptide_filename = 'peptide-v1_uniq.txt'
        output_filename = 't1-v1.txt'
        prepareEntry(output_filename,worm_loopstat_input2_filename,description_filename,peptide_filename)
    
    
    #main()
#------------------------------------

if __name__ == "__main__" : 
    unittest.main()
    
#------------------------------------
