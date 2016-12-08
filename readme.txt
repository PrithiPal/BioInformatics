This is the readme file for the place_hash branch. Here is how the stuff goes : 

1. the txt_files contains the files (fi.txt for i=(1..7)) which are the .txt versions for the s1 worm publication. So, the format.txt file tells the format for each file (usually identifier = 1; before_residual = 6; sequence = 7; after_residual = 9)

2. run the prepare_residual_file.py, which is fi.txt ------> residual.py -------> fi_before_hash.txt. This python script convert the fi.txt to the fi_before_hash.txt (<identifier> <before_residual>.<sequence>.<after_residual>)

3. run the bash command inside the script_for_f_all_before_hash.txt to generate a f_all_before_hash.txt which contains around 2400 entries.

4. Now f_all_before_hash.txt ---------> place_hash.py -------------> f_all_after_hash.txt

5. Congratz the peptide_sequence file is ready for the next step which is 

6. fasta_file + fi_after_hash.txt  -----------> find_glyco_pep.cpp ---------------> peptide_worm_output.txt (<Identifier> <found sequences NX(!P)S/T>)

7. afterwards, use the script script_for_f_all_description.txt to obtain a f_all_description file.

8. run this command 
    1. awk '/not_found/{print $1}' peptide_worm_output.txt > names.txt
    2. cat names.txt | xargs -n1 -I {} sed -i.txt '/{}/d' peptide_worm_output.txt 
    
    This will remove the entries in peptide_worm_output where seq is not_found

9. Now worm_loopstat_input2 + f_all_descriptions.txt -------> prepare_worm_loopstat_output1.py ----> worm_loopstat_input1.txt

10. Now we have got both worm_loopstat_input1 and worm_loopstat_input2. So the final solution is to input them in loopstat to obtain the ultimate worm output.


<---work over here for worm-------->
