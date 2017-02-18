## this file take input the file with format <index> <before_residual>.<peptide_seq>.<after_residual> and outputs with hashes placed in peptide_seq.

## INPUT : <index> <before_residual>.<peptide_seq>.<after_residual> <peptide_start> <peptide_end> <total_sites> <first_site_position> <second_site_postion>
## OUTPUT : <index> <before_residual>.<peptide_seq_with_hash>.<after_residual> 

## credits for insertChar function : Elenasys on stack overflow ##
def main() : 
    iFileName = raw_input("Please enter the input file name <Identifier> <peptide_seq> : ")
    iFile = open(iFileName,"r")
    oFileName = raw_input("Please enter the output file name <Identifier> <peptide_seq with hash> : ")
    oFile = open(oFileName,"w")
    
    
    placeHash(iFileName,oFile)







def insertChar(mystring, position, chartoinsert ): 
    longi = len(mystring)
    mystring   =  mystring[:position] + chartoinsert + mystring[position:] 
    return mystring


##function to place hash in second position to found sequence, format : N#XS/T
def placeHash(idxFile,outputFile) : 
    count=0
    num_seq=0
    for line in open(idxFile,"r") : 
        
        frag = line.split("\t") ## frag[1] = peptide_seq
        peptide_seq = frag[1]
        peptide_start = frag[2]
        no_of_sites = frag[4]
        first_site_position = frag[5]
        first_index= int(first_site_position) -  int(peptide_start) + 3
        peptide_seq = insertChar(peptide_seq,first_index,"#")

            
        if no_of_sites == "2" : 
            second_site_postion = frag[6]
            second_index = int(second_site_postion) - int(peptide_start)+ 4
            peptide_seq = insertChar(peptide_seq,second_index,"#")
            count=count+1
        print peptide_seq
        outputFile.write(frag[0] + "\t" + peptide_seq + "\n")
        
        


if __name__ == "__main__" : 
    main()
