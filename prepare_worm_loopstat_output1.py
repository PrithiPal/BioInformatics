#This python script prepare the first input for the worm to be put in the loopstat cpp file. The second input is worm_transloop_output2.txt

## INPUT : peptide file, f_all_descriptions.txt mouse_loopstat_input2
## OUTPUT : t1[current].txt or worm_loopstat_input1



# This is reused for the mouse first_loopstat_prepare.py
import time
import unittest
print "starting..."
import os
import re


global mouse_output_filename   
##--------------------------------------------------------------------------------

def main() : 
    
    start_time = time.time()
    
    MOUSE_DESCRIPTION_INDEX = 1
    MOUSE_PROTEIN_L_INDEX = 2
    
    mouse_description_filename = 'mouse_qualitative.txt'
    mouse_peptide_filename = 'peptide-v1.txt'
    mouse_protein_l_filename = 'mouse_loopstat_input1_theo.txt'
    mouse_output_filename = 't1[current]-v1.txt'
    
    prepareWormLoopstatInput1(mouse_output_filename,mouse_description_filename,mouse_protein_l_filename,mouse_peptide_filename,MOUSE_DESCRIPTION_INDEX,MOUSE_PROTEIN_L_INDEX)
    
    identify_blank_description(mouse_output_filename)
    

    print "done!!"
    elapsed_time = time.time() - start_time
    print "time elapsed = " + str(elapsed_time)
    
    return mouse_output_filename

##--------------------------------------------------------------------------------

def prepareWormLoopstatInput1(output_file,description_filename,protein_l_filename,peptide_filename,DESCRIPTION_INDEX,PROTEIN_L_INDEX) : 
    arr = []
    for i in range(5) : 
        arr.append([]) ## creates the 5 columns for the data 
    identifier = ""
    descr_identifier = ""
    description = ""
    protein_length = ""

    ofile = open(str(output_file),"w")
    
    for lines in open(str(peptide_filename),"r") : 
        
        
         # if not_found or "0" as the return value of inspect_notfound in entry then don't accept it.
        
        if eligible_line(str(lines[:-1])) == True : 
            print lines
            frag1 = lines.split("\t")
            frag2 = lines.split(" ")
            
            identifier = frag1[0]
            seq_list = frag1[1]
            total_seq = len(frag1[1].split(" "))-1
            
            description = findDescription(str(description_filename),identifier,DESCRIPTION_INDEX)
            protein_length = findProteinLength(str(protein_l_filename,),identifier,PROTEIN_L_INDEX)
            
                
            print_this = str(identifier) + "\t" + str(description) + "\t" + str(protein_length)  + "\t" + str(total_seq) + "\t" + seq_list
            #print print_this
            ofile.write(print_this)
    
##--------------------------------------------------------------------------------
## Determine whether the line argument contains only not_found. If yes then it is not eligible.
def eligible_line(line) : 
    
    eligible = inspect_notfound(str(line))
    if eligible == "0" or eligible == '0' : 
        return False
    return True

##-------------------------------------------------------------------------------   
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

def identify_blank_description(filename) : # identifies whether the description is null or empty ("") in file
    print "Blank Description Test : "
    response = os.system("awk \'BEGIN{FS = \"\t\"}{if($2 == \"\"){print $0}}\' " + str(filename))

##--------------------------------------------------------------------------------

def inspect_notfound(line) : # inspects the peptide file for not_found lines
    
    
    found_seq = re.split("\t",str(line))
    identifier = found_seq[0]
    found_seq = found_seq[1].split(" ")
    modified_seq = [x for x in found_seq if x != "not_found"]
   # print modified_seq
    if modified_seq == [''] or modified_seq == [] : 
        return "0"
    return identifier + "\t" + ' '.join(modified_seq)
    
## -------------------------------------------------------------------------------

class MyTest(unittest.TestCase) : 
    
    def test_inspect_notfound_function_partial(self) : 
        #allowed_line
        sample = "IPI00113480	NRS(365) not_found "
        l = inspect_notfound(sample)
        # print l
        o = "IPI00113480	NRS(365) "
        self.assertTrue(l==o)
        
    
    def test_inspect_notfound_function_full(self) : 
        #allowed_line
        sample = "IPI00114265	NTT(142) NQS(242) "
        l = inspect_notfound(sample)
       # print l
        o = "IPI00114265	NTT(142) NQS(242) "
        self.assertTrue(l==o)
    
    def test_inspect_notfound_function_none(self) :
        #not allowed_line
        sample1 = "IPI00114348	not_found not_found "
        sample2 = "IPI00122737	not_found "
        sample3 = "IPI00118851	not_found not_found not_found not_found"
        l1 = inspect_notfound(sample1)
        l2 = inspect_notfound(sample2)
        l3 = inspect_notfound(sample3)
        print l3
        #print l
        o="0"
        self.assertTrue(l1==o)
        self.assertTrue(l2==o)
        self.assertTrue(l3==o)  
        
    def test_eligbile_function(self) : 
        sample1 = "IPI00114348	not_found not_found "
        sample2 = "IPI00607976	not_found "
        sample3 = "IPI00118851	not_found not_found not_found not_found"
        sample4 = "IPI00114265	NTT(142) NQS(242) "
        
        el1 = eligible_line(sample1)
        el2 = eligible_line(sample2)
        el3 = eligible_line(sample3)
        el4 = eligible_line(sample4)
       
        self.assertTrue(el1==False)
        self.assertTrue(el2==False)
        self.assertTrue(el3==False)
        self.assertTrue(el4==True)
        print el3
        print el4
        
    main()
   
## -------------------------------------------------------------------------------
if __name__ == "__main__" : 
    unittest.main()
    



