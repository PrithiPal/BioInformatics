This is the readme file for the place_hash branch. Here is how the stuff goes : 

1. get the files (fi.txt for i=(1..7)) which are the .txt versions for the s1 worm publication. 

2. Now these fi.txt files are required to be get in the format <Identifier> <before_residual>.<--peptide_sequence-->.<after_residual>. So write the code in add_residual.py to bring the file to this format.

3. When done write the documentation at top of the add_residual.py explaining which column is used for identifier,before_residual etc..

4. The output file should be named as fi_before_hash.txt

5. Now fi_before_hash.txt ---------> place_hash.py -------------> fi_after_hash.txt

6. then concatenate the fi_after_hash.txt for i in (1..7) to f_all_after_hash.txt

7. Congratz the peptide_sequence file is ready for the next step which is 

 fasta_file + fi_after_hash.txt  -----------> find_glyco_pep.cpp ---------------> peptide_worm_o.txt (<Identifier> <found sequences NX(!P)S/T>)