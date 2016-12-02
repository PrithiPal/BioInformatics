oFileName = raw_input("Please enter the output file name <Identifier> <peptide_seq with hash> : ")
oFile = open(oFileName,"w")


## credits for this function : Elenasys on stack overflow ##
def insertChar(mystring, position, chartoinsert ): 
    longi = len(mystring)
    mystring   =  mystring[:position] + chartoinsert + mystring[position:] 
    return mystring


##function to place hash in second position to found sequence, format : N#XS/T
num_seq=0

for line in open("f1_output.txt","r") : 
    frag = line.split("\t") ## frag[1] = peptide_seq
    peptide_seq = frag[1]
    num_seq=0
    for i in range(2,len(peptide_seq)) : 
        if (peptide_seq[i-2] == "N") and (peptide_seq[i-1]!="P" and (peptide_seq[i] == "S" or peptide_seq[i] == "T")):
            num_seq=num_seq+1
            print "seq = " + str(peptide_seq[i-2]) + str(peptide_seq[i-1]) + str(peptide_seq[i]),
            peptide_seq = insertChar(peptide_seq,i-1,'#')
            oFile.write(frag[0] +"\t" + peptide_seq)
            i=i+3
    if num_seq == 0 : 
        print "seq not found",
    print "peptide = " + peptide_seq,
    print ""    
    
    

