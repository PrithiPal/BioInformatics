##this scripts finds the format (i.e which columns represent what type of data. for example column1 = identifier, column3 = description etc..)
##the input file is of name fi.txt for i in (1..34) and the output file is formatting.txt


ofile = open("formating.txt","w") ## output file

for i in range(1,35) : 
    count=1
    ofile.write("----------------------\n")
    ofile.write("-----***filename = f"+ str(i) + ".txt ***-----"  + "\n")
    filename = "f" + str(i) + ".txt"
    for lines in open(filename,"r") : ##input file
        frag = lines.split("\t")
        if count==1 : 
            for j in range(len(frag)) : 
                ofile.write("frag[" + str(j) + "] =" + str(frag[j]) + "\n")
        count=count+1
    ofile.write("----------------------\n")