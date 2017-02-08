

#filename = raw_input("Which File ? ")
#file = open(str(filename),"r")


filename = "f_all_descriptions.txt"
ofile = open(str(filename)[:-4] + "_only_first.txt","w")
for line in open(str(filename),"r") : 
    frag = line.split("\t")
    identifier = frag[0]

    identifier_frag = identifier.split(" ") ##identifier_frag[1] = second/extra identifier
    
    if len(identifier_frag) > 1 : 
        print "line : ",str(line)[:-1]
        new_line = line.replace(str(identifier),identifier_frag[0])
        print "new_line : ",str(new_line)
        ofile.write(str(new_line))
