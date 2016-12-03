##Documentation check the readme file 
## for f1. identifier = $1$0, before_residual = $4, seq = $5, after_residual = $7 
## for f2. identifier = $1, before_residual = $5, seq = $6, after_residual = $8 
## for f3. identifier = $1$0, before_residual = $4, seq = $5, after_residual = $7 
## for f4. identifier = $1$0, before_residual = $4, seq = $5, after_residual = $7 
## for f5. identifier = $1$0, before_residual = $5, seq = $6, after_residual = $8 
## for f6. identifier = $1$0, before_residual = $4, seq = $5, after_residual = $7 
## for f7. identifier = $1$0, before_residual = $4, seq = $5, after_residual = $7 

ofile = open("f7_before_hash.txt","w") ## output file

for lines in open("f7.txt","r") : ##input file
    frag = lines.split("\t")
    frag2 = frag[1].split(" ")
    
    #print frag[7]
    identifier = frag2[0]
    before_residual = frag[4]
    sequence = frag[5]
    after_residual = frag[7]
    print_this = identifier + "\t" + before_residual + "." + sequence + "." + after_residual + "\n"
    print print_this
    ofile.write(print_this)