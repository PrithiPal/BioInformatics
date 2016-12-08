# This file works as follows fi.txt ----> prepareResidualFile(fi.txt) ------> fi_before_hash.txt

# Input : fi.txt file
# Output : file with format <index> <before_residual>.<peptide_seq>.<after_residual>; output filename = fi_before_hash.txt
def prepareResidualFile() : 
    
    iFileName = raw_input("Which file ? ")
    iFileName = iFileName + ".txt"
    iFile = open(iFileName,"r")
    oFileName = iFileName + "_before_hash.txt"
    oFile = open(oFileName,"w")
    
    for line in open(iFileName,"r") : 
            
            frag = line.split("\t")
            identifier = frag[1]
            if len(identifier) != 0 : 
                before_residual = frag[6]
                after_residual = frag[9]
                peptide_seq = frag[7]
                print_this  = identifier + "\t" + before_residual + "." + after_residual + "." + peptide_seq + "\n"
                print print_this
                oFile.write(print_this)

for i in range(1,35) : 
    
    prepareResidualFile()
