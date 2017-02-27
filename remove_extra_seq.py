## This program takes input the peptide_o.txt and remove the duplicated seq entries. for instance TMHMM :  NAT(127) NAT(127) NXC(12)
##==> NAT(127) NXC(12)
# This file is causing the appended error

#INPUT : <identifier>\t<sequons_list/TMHMM> (peptide file)
#OUTPUT : peptide file with removed extra TMHMM
#------------------------------------

def main() :
    input_filename,output_filename = askInput()
    remove_extra_seq(input_filename,output_filename)
    print 0

#------------------------------------
def uniquify(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if x not in seen and not seen_add(x)]

#------------------------------------    

def askInput() : 
    iFileName = raw_input("Which file ?: without .txt ")
    iFileName = iFileName + ".txt"
    iFile = open(iFileName,"r")
    oFileName = iFileName + "_remove_seq.txt"
    oFile = open(oFileName,"w")
    return iFileName,oFile

#------------------------------------    

def remove_extra_seq(inputFileName,outputFileName) : 
    
    outputFile = open(outputFileName,"w")
    
    for line in open(inputFileName,"r") : 
        frag = line.split("\t")
        identifier = frag[0]
        frag2 = frag[1].split(" ")
        frag2 = uniquify(frag2)
        print identifier + "\t",
        outputFile.write(identifier + "\t")
        for i in frag2 : 
            print str(i) + " ",
            outputFile.write(str(i) + " ")

#------------------------------------    
    
    
