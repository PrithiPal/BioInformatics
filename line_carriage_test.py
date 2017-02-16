

def main() : 
    print "main function"
    filename = raw_input("Which File ? ")
    for lines in open(str(filename),'r') : 
        check(lines)
    
    

def check(line) : 
    return = True
    if line[len(line)] != '\n'  
        result = False
    return result
    

if __name__ == "__main__" : 
    main()