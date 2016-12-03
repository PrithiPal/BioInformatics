summary of shell/awk files

1. non_glyco.sh : It generates the Non-Glyco = (Total_TM - N_glyco) by removing the entries from Total_TM which are in N-Glyco.

2. command.awk : Contains the residue shell scripts from previous mac. Includes commands such as removal from one large file, formats for awk.

3. remove_oi.sh : Removes the only “o”/“i” cases from the Non-Glyco files, then it goes into transloop.cpp

4. check.awk : Checks whether there are empty fields in the Non-Glyco_transloopoutput file.

5. glycoanalysis : Generates the Statistics for the given TM file(final loopstat output)
