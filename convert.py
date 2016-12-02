ofile = open("f1_hash.txt","w")
for line in open("before_f1.txt","r") : 
    frag = line.split("\t")
    seq = frag[1]
    frag2 = frag[0].split(" ")
    identifier = frag2[0]
    toPrint = identifier + "\t" + seq
    print toPrint
    ofile.write(toPrint)
    
