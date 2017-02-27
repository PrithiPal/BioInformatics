import unittest
import re
#this files checks for the appended Error for ex, : E04F6.4	NST(249) F01D4.4 F01E11.1	NLT(368) i.e identifiers E04F6.4,F01D4.4 and  F01E11.1 are in same line.
## INPUT : <identifier>\t<sequons_list> (peptide file)
## OUTPUT : Lines with the Error


#------------------------------------
def main() : 
    
    ask_input()
    print 0
#------------------------------------
def ask_input() : 
    
    try : 
        filename = raw_input("Which file ? ")
        for lines in open(str(filename),"r") : 
            response  = check(lines)
            if not response : 
                print(lines)
            
    except Exception as e : 
        print "Error : ", str(e)
#------------------------------------  
 
def check(line) : 
    result = False

    line_list = re.split("\t| ",line)
    result =   find_identifiers(line_list)
  
    return result
    
#------------------------------------

def find_identifiers(line) : 
    identifier = [elem for elem in enumerate(line) if str(elem).find(".") > 0]
    
    if len(identifier) > 1 : #more than one identifier found
        return False
    else : 
        return True
#------------------------------------    

class Tests(unittest.TestCase) : 
    
    def test_first_sample(self) : #should be true
        string = "E04F6.4	NST(249) NST(249)"
        
        result = check(string) 
        self.assertTrue(result)
        
    def test_second_sample(self) : #should be false
        string = "E04F6.4	NST(249) NST(249) F01D4.4	NGT(385) NVT(428)"
        result = check(string)
        self.assertFalse(result)

    
    
    main()
#------------------------------------

if __name__ == "__main__" : 
    unittest.main()
    
    