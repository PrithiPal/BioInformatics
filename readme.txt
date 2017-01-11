This is the readme file for the place_hash branch. Here is how the stuff goes : 

-1. Refering to desktop/20161012/worm_test directory, peptide files folder contains the splitted information about the peptide proteins(34 files). 

peptide files (pdf) ----> peptide files xl (excel format) --after correction --> txt_files 

1. the txt_files contains the files (fi.txt for i=(1..34)) which are the .txt versions for the s1 worm publication. So, the format.txt file tells the format for each file (usually identifier = 1; before_residual = 6; sequence = 7; after_residual = 9)

2. f_worm.txt is fi.txt for i=(1..34) and eliminiating blank spaces. beforeLines = 4589, afterLines=2654 

3. run the prepare_residual_file.py, which is f_worm.txt ------> residual.py -------> f_worm.txt_before_hash.txt. This python script convert the fi.txt to the fi_before_hash.txt (<identifier> <before_residual>.<sequence>.<after_residual> <peptide_stat> <peptide_end> <no_of_glyco_sites> <first_site> <second_site>)

4. Now f_worm.txt_before_hash.txt ---------> place_hash.py -------------> f_worm.txt_after_hash.txt . Lines = 2641

5. Run the command to eliminiate duplicate entries : 
     cat f_worm.txt_after_hash.txt | uniq > f_worm_uniq_after_hash.txt. Lines = 1868
     

6. fasta_file + f_worm_uniq_after_hash.txt -----------> find_glyco_pep.cpp ---------------> peptide_worm_output.txt (<Identifier> <found sequences NX(!P)S/T>) Lines = 809


7. peptide_worm_output.txt -----> remove_extra_seq.py -----> peptide_worm_output_after_removeextra.txt
This program has removed the duplicated sequences for each protein. Lines = 621


**---- After new place_hash changes begin from here**

8. afterwards, use the script script_for_f_all_description.txt to obtain a f_all_description file.
2
9. run this command 
    1. awk '/not_found/{print $1}' peptide_worm_output.txt > names.txt
    2. cat names.txt | xargs -n1 -I {} sed -i.txt '/{}/d' peptide_worm_output.txt 
    
    This will remove the entries in peptide_worm_output where seq is not_found

9. Now worm_loopstat_input2 + f_all_descriptions.txt -------> prepare_worm_loopstat_output1.py ----> worm_loopstat_input1.txt

10. Now we have got both worm_loopstat_input1 and worm_loopstat_input2. So the final solution is to input them in loopstat to obtain the ultimate worm output.


<---work over here for worm-------->
