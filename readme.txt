This is the readme file for the place_hash branch. Here is how the stuff goes : 

1. the txt_files contains the files (fi.txt for i=(1..7)) which are the .txt versions for the s1 worm publication. So, the format.txt file tells the format for each file (usually identifier = 1; before_residual = 6; sequence = 7; after_residual = 9)

2. run the prepare_residual_file.py, which is fi.txt ------> residual.py -------> fi_before_hash.txt. This python script convert the fi.txt to the fi_before_hash.txt (<identifier> <before_residual>.<sequence>.<after_residual>)

3. run the bash command inside the script_for_f_all_before_hash.txt to generate a f_all_before_hash.txt which contains around 2400 entries.

4. Now f_all_before_hash.txt ---------> place_hash.py -------------> f_all_after_hash.txt

5. Congratz the peptide_sequence file is ready for the next step which is 

6. fasta_file + fi_after_hash.txt  -----------> find_glyco_pep.cpp ---------------> peptide_worm_output.txt (<Identifier> <found sequences NX(!P)S/T>)