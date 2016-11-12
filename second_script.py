fasta_file = open("mouse_human.fasta.txt","r")
peptide_file = open("peptide_o.txt","r")

fasta_lines = fasta_file.readlines()
peptide_lines = peptide_file.readlines()
count=0
for i in range(len(peptide_lines)-1) : 
    f1 = fasta_lines[i].split("\t")
    f2 = peptide_lines[i].split("\t")
    if f1[0] == f2[0] : 
        print "found %s" % (f1[0])
        count=count+1
    else : 
        print "not found %s" % (f1[0])
print "count = %d" % count