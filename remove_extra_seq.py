## This program takes input the peptide_o.txt and remove the duplicated seq entries. for instance NAT(127) NAT(127) NXC(12)
##==> NAT(127) NXC(12)
def uniquify(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if x not in seen and not seen_add(x)]
    


inputFileName = raw_input("Which File ? ")
outputFileName = raw_input("Which File to output ? ")
outputFile = open(outputFileName,"w")
for line in open("now_output.txt","r") : 
    frag = line.split("\t")
    identifier = frag[0]
    frag2 = frag[1].split(" ")
    frag2 = uniquify(frag2)
    print identifier + "\t",
    outputFile.write(identifier + "\t")
    for i in frag2 : 
        print str(i) + " ",
        outputFile.write(str(i) + " ")

    
    
    
