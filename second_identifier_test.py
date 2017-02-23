


def second_identifier_test() : 
    filename = raw_input("Which file ? ")
    count=0
    for line in open(str(filename),"r") : 
        if count > 1 : 
            frag = line.split("\t")
            identifier = frag[0]
            identifier_frag = identifier.split(" ")
            
            if len(identifier_frag) > 1 : 
                print_this = str(identifier_frag[1]) + " in " + str(identifier)
                print print_this
        count=count+1


    