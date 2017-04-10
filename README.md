# Bioinformatics - place\_hash Documentation

## **Introduction to Research**\[1\]

This interdisciplinary research study cell-surface N-glycoproteins through LC-MS based shotgun proteomic tools, an important factor in stem-cell development. The stem-cell behavior is influenced by extra-cellular microenvironment through these proteins and this study attempts to understand the phenomena.

LC-MS based shotgun proteomics uses HPLC that deliver 1 nanoliter/minute constant flow. It operates under intensive atmosphere pressure \(100-1000 C\) for high resolution separation. Following this, it takes mere few minutes to derive million peptides from thousand protein through mass spectrometry analysis. It detects and quantifies entire proteome of all biological samples and helps with systematic study of human health and diseases.

## **Repository Overview**

Pertaining to the current research comprising the subset of overall research objectives, this repository contains the raw data for analysis. It also contains the relevant files and programs required to obtain the mouse’s final loop stat output. This discourse took immense research to determine the suitable programming language, file-format and tools for data analysis. Following the successful acquisition of results, it’s important to ensure the final results reliability and overall accuracy. For the same reason, all programming scripts incorporate embedded test cases with unit tests.

The scope of intended explanation leaves the technical aspects entailing the research and discuss information relevant to obtain stastical results using programming tools.

## **Contextual Information**

In beginning, the **publication** summarizing identified peptide of mouse species \(mouse publication\) **and** glyco FASTA file for mouse was **provided**.

#### **Glyco protein \(.**FASTA**\)**

This file uses special format to list the significant properties of glyco proteins. The FASTA format is as below:

> &gt;sp\|P31946\|1433B\_HUMAN 14-3-3 protein beta/alpha OS=Homo sapiens GN=YWHAB PE=1 SV=3
>
> MTMDKSELVQKAKLAEQAERYDDMAAAMKAVTEQGHELSNEERNLLSVAYKNVVGARRSS
>
> WRVISSIEQKTERNEKKQQMGKEYREKIEAELQDICNDVLELLDKYLIPNATQPESKVFY
>
> LKMKGDYFRYLSEVASGDNKQTTVSNSQQAYQEAFEISKKEMQPTHPIRLGLALNFSVFY
>
> YEILNSPEKACSLAKTAFDEAIAELDTLNEESYKDSTLIMQLLRDNLTLWTSENQGDEGD
>
> AGEGEN

First line tells information for protein identification and the remainder of lines depicts protein sequence.

The standardized glyco data for indexed species can be found in online BASIC \(Basic Local Alignment Search Tool\) database.

#### **Mouse publication**\(.pdf\)

It lists all identified peptides and associated relevant variables in the study. The mouse publication forms the basis for the information employed for the analysis. This means all piece of peptide information encountered in later parts would be inherited from this single pdf publication. The significant characteristic of each peptide sequence \(one row in publication\) are as listed below:

* CDS ID and Worm pep ID : Technical protein identifiers
* Protein description : description of protein
* Peptide position \(from\)
* Peptide position \(to\)
* Preceding residue
* Peptide sequence
* C-terminal peptide residue
* No. of potential sites
* Glycosylated site-1 and site-2

Again the definitions of these biological variables are not in scope of consideration unless their applicability arises.

Glyco FASTA file and Mouse publication becomes the starting resources for the data analysis. The primary objective is deriving loopstat files which attains special attentions due to the information it encloses.

#### **Find\_glyco\_pep**\(.cpp\)

This C++ program finds the occurring sequence$$NX(!P)S|T$$ where first character is N, second is anything except P and last is either S or T. The FASTA sequence is used as search source and all instances with respective positions of above combinations are reported.

`Usage : ./find_glyco_pep - -fasta=[FASTA FILE] - -human=[PEPTIDE FILE]`

## **Instructions**

The assurance of correctness and durability, each step of data manipulation is broken down in number of steps. Each step signifies milestone whose concrete definitions are determined through appropriate research and requires solving sets of problem statements before proceeding. For instance, first milestone or step may consist of omitting blank rows and convert to tab delimited text file. Afterwards sending the progressed files to Supervisor to receive critical feedback and readjust the methodology accordingly in case of inconsistent calculations/formatting witnessed. Below are the steps or milestone established.

* The pdf version of mouse publication is converted and dispersed into 34 different excel Sheets. The original intentions was to obtain files in text file format. The arousal of formatting error during conversion from pdf needs to be first corrected in excel Sheets. Excel is used to correct the inconsistent formatting which included overlapping of column entries into adjacent row proteins data. After the assurance of correction, excel sheet is converted back to 34 discrete text files\(from 34 pages pdf\)

* Now, the extraction of certain columns from corresponding text file is done. The reason for it would be clear in later steps where the extracted information for each protein identifier is utilized. The format is

> &lt;Identifier&gt;&lt;before residual&gt;.&lt;peptide sequence&gt;.&lt;after residual&gt;&lt;peptide start\(from\)&gt;&lt;peptide end\(to\)&gt;&lt;no of potential sites&gt;&lt;first site position&gt;&lt;second site position&gt;.

* Prepare\_residual\_file.py provides the means for this particular extraction. Basically it accepts mouse publication text files and save the extracted columns in file

> &lt;input file&gt;\_before\_hash.txt

* The peptide sequence possess two variables; peptide start and peptide end index which locates sequence’s position within overall protein sequence in FASTA file. Each peptide sequence have one or two glycoanalysis sites and the next step includes insertion of hash \(“\#”\) character in sequence at identified glycoanalysis sites. This functionality is achieved by place\_hash.py which accepts before\_hash text files. The insertion is determined through below calculation :


$$
{i_1 = p_{from} - g_{1} + 3 ; i_2 = p_{from} - g_{2} + 4}
$$


where $$i_{1}, i_{2}$$ are index for hash insert ,  $$g_{1} , g_{2}$$ are index or glyco. sites and $$p_{from}$$ peptide position \(start\)

> &lt;input file&gt;\_after\_hash.txt

* To enhance the format, the removal of secondary identifier such as “CE22235” from “Y49E10.20 CE22235 ” is recommended because it adds one more column and causes inconsistency. The correct\_identifier.py will accept any \_after\_hash files and outputs entries less than secondary identifier.

> &lt;input file&gt;\_only\_first.txt

* To remove complete duplicated entries and sort accordingly, write the bash script:

`cat f_worm.txt_after_hash_only_first.txt | uniq | sort > f_worm_uniq_after_hash_only_first.txt`

* The final output file is named with prefix “uniq” for reader convenience and can be renamed. After that, find\_glyco\_pep.cpp helps extract the position of all occurring expression $$NX(!P)S|T$$ in fasta file. The input are FASTA and \_after\_hash file.

> &gt;&gt; peptide.txt \(FORMAT : &lt;protein identifier&gt;&lt;List of found NX\(!P\)S\|T&gt;\)

## To be continued 

Until now, the acquisition of mouse peptide file is successfully done which acts as output in subsequent steps to obtain Transloop results. Further documentation to continue with data processes steps will come in existence as soon as the eminent bugs are located and fixed. Following the fixation of bugs, writing of tests also forms integral part of each enclosing python codes for data analysis. 

## Contribution

Please feel independent to contribute the source code in order to achieve effciency, robustness and overall durability. Many python modules requires refractoring for the purpose of for instance speeding up search algorithm. In addition, more testing modules can be added to supporting python framework for unittesting.  

## Citations/References 

\[1\].[ Sun lab Research Page](http://www.sfu.ca/chemistry/groups/bingyun_sun/research.html)

\[2\]. [Gitbook.com](/www.gitbook.com) used for documentation







