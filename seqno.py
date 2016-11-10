import os

filename = raw_input("filename : ")
if str(filename[:-4]) != ".txt" : 
    filename = filename + ".txt"
os.system("touch " + filename)
file = open(filename,"w")

file.write("chacha chaudhary")






