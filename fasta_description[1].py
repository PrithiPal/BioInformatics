import re
import unittest
import os
import time
# This code gathers the description for corresponding IPI/identifier from a fasta file

# INPUT : fasta_file.txt
# OUTPUT : fasta_file_description.txt ( format : <identifier>\t<description> )

#-------------------------------
def main() : 
    
    input_filename = ask_input()
    process(input_filename)
    print 0
#------------------------------------

def ask_input() : 
        ifilename = raw_input("Which file ? ") # input fasta file
        return ifilename
#------------------------------------

def process(ifilename) : 
    
    ofilename = str(ifilename)[:-4] + "_description.txt"  # file with format <identifier>\t<description>
    ofile = open(str(ofilename),'w')
    try : 
        for lines in open(str(ifilename),"r") : 
            if lines[0] == ">" : 
                iden,desc = findDetails(lines)
                if iden != "" : 
                    print_this = str(iden) + "\t" + str(desc) + "\n"
                    print "print_this = ",print_this
                    ofile.write(str(print_this))
    except  : 
        print "Error"
    ofile.close()
    # done with processing lines            
    time.sleep(1)
    bash_command = "cat " + str(ofilename) + " | sort | uniq > " + str(ofilename) + "_uniq.txt"
    os.system(bash_command)
    

    
#------------------------------------

def findDetails(line) : 
    
    REGEX = "\w (.*) GN=([A-Z0-9\.]*)"
    information = re.findall(REGEX,str(line))
    description = information[0][0]
    identifier = information[0][1]
    return identifier,description

    
# -----------------------------------    
    

class MyTest(unittest.TestCase) : 
    

    def test_description(self) :
        line = ">sp|Q10122|YSM1_CAEEL Uncharacterized WD repeat-containing protein F52C9.1 OS=Caenorhabditis elegans GN=F52C9.1 PE=4 SV=2"
        a,b = findDetails(line)
        print "findDescriptionString desc: ",str(b)    
        print "findDescription id: ",str(a)
        
    def test_regex(self) : 
        line1 = ">sp|P41932|14331_CAEEL 14-3-3-like protein 1 OS=Caenorhabditis elegans GN=par-5 PE=1 SV=2"

        
        a,b = findDetails(line1)
        
        print "a : ",a
        print "b : ",b

    def test_particular_file(self) : 
        filename = "worm_fasta.txt"
        process(filename)
        
#------------------------------------

if __name__ == "__main__" : 
    unittest.main()
    
#------------------------------------