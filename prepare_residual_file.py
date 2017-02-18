#This file also contains the information about the peptide_positions. It will help finding the position to place hash in place_hash.
# INPUT : fi.txt file
# OUTPUT : file with format <index> <before_residual>.<peptide_seq>.<after_residual> <peptide_start> <peptide_end> <total_sites> <first_site_position> <second_site_postion>; output filename = fi_before_hash.txt


def prepareResidualFile() : 
    
    iFileName = raw_input("Which file ?: without .txt ")
    iFileName = iFileName + ".txt"
    iFile = open(iFileName,"r")
    oFileName = iFileName + "_before_hash.txt"
    oFile = open(oFileName,"w")
    
    for line in open(iFileName,"r") : 
            first_glyco_pos = 0
            second_glyco_pos = 0
            frag = line.split("\t")
            identifier = frag[1]
            if len(identifier) != 0 : 
                peptide_start = frag[4]
                peptide_end = frag[5]
                before_residual = frag[6]
                after_residual = frag[9]
                peptide_seq = frag[7]
                
                no_of_sites = frag[22]
                first_glyco_pos = frag[23]
                #second_glyco_pos =   frag[24]
                if no_of_sites == "1" : 
                    second_glyco_pos = None
                elif no_of_sites == "2" :
                    second_glyco_pos = frag[24]
                
                
                print_this  = identifier + "\t" + before_residual + "." + peptide_seq + "." + after_residual + "\t" + peptide_start + "\t" + peptide_end + "\t" + no_of_sites + "\t" + str(first_glyco_pos) + "\t" + str(second_glyco_pos) + "\n"
                print print_this
                oFile.write(print_this)

    
prepareResidualFile()
