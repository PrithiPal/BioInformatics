
#input is the peptide[current]_sorted.txt 
#tests for the appended error for ex, : E04F6.4	NST(249) F01D4.4 F01E11.1	NLT(368) 

#filename = raw_input("Which File ? ")
filename = "ou1.txt"
for lines in open(str(filename),"r") : 
    frag = lines.split("\t")
    iden = frag[0]
    whole_seq = frag[1].split(" ")
    for seq in whole_seq[:-1] : 
        if "(" not in seq : 
            print seq, " in ", whole_seq
    