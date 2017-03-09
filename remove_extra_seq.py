## This program takes input the peptide_o.txt and remove the duplicated seq entries. for instance TMHMM :  NAT(127) NAT(127) NXC(12)
##==> NAT(127) NXC(12)
# This file is causing the appended error

#INPUT : <identifier>\t<sequons_list/TMHMM> (peptide file)
#OUTPUT : peptide file with removed extra TMHMM

import unittest
#------------------------------------

def main() :
    input_filename,output_filename = askInput()
    remove_extra_seq(input_filename,output_filename)
    print 0

#------------------------------------
def uniquify(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if x not in seen and not seen_add(x)]

#------------------------------------    

def askInput() : 
    iFileName = raw_input("Which file ?: without .txt ")
    iFileName = iFileName + ".txt"
    iFile = open(iFileName,"r")
    oFileName = iFileName + "_remove_seq.txt"
    
    return iFileName,oFileName

#------------------------------------    

def remove_extra_seq(inputFileName,outputFileName) : 
    
    outputFile = open(outputFileName,"w")
    seq_list = ""
    for line in open(inputFileName,"r") : 
        
        frag = line.split("\t")
        identifier = frag[0]
        frag2 = frag[1].split(" ")
        frag2 = uniquify(frag2)
        print "uniq ",frag2
        
        for i in frag2 : 
            if str(i) != '\n' : 
                seq_list = seq_list + str(i) + " "
        print_this = str(identifier) + "\t" + str(seq_list) + "\n"
        print print_this
        outputFile.write(print_this)
        seq_list = ""
#------------------------------------    

class MyTest(unittest.TestCase) : 
   
    def test_remove_function(self) : 
        ifile = "peptide-v1.txt"
        ofile = "peptide-v1_uniq.txt"
        remove_extra_seq(ifile,ofile)
        print 0

#------------------------------------     
if __name__ == "__main__"  : 
    unittest.main()

