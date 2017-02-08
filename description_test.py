

filename = "t1[current].txt"

for lines in open(str(filename),"r") : 
    frag = lines.split("\t")
    iden = frag[0]
    desc = frag[1]
   
    if str(desc) is " " or desc is None : 
        print "Desc : ",str(desc), " in ", str(iden)