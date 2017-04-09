# Bioinformatics - place\_hash Documentation

## **Introduction to Research**\[1\]

This interdisciplinary research study cell-surface N-glycoproteins through LC-MS based shotgun proteomic tools, an important factor in stem-cell development. The stem-cell behavior is influenced by extra-cellular microenvironment through these proteins and this study attempts to understand the phenomena.

LC-MS based shotgun proteomics uses HPLC that deliver 1 nanoliter/minute constant flow. It operates under intensive atmosphere pressure \(100-1000 C\) for high resolution separation. Following this, it takes mere few minutes to derive million peptides from thousand protein through mass spectrometry analysis. It detects and quantifies entire proteome of all biological samples and helps with systematic study of human health and diseases.

## **Repository Overview**

Pertaining to the current research comprising the subset of overall research objectives, this repository contains the raw data for analysis. It also contains the relevant files and programs required to obtain the mouse’s final loop stat output. This discourse took immense research to determine the suitable programming language, file-format and tools for data analysis. Following the successful acquisition of results, it’s important to ensure the final results reliability and overall accuracy. For the same reason, all programming scripts incorporate embedded test cases with unit tests.

The scope of intended explanation leaves the technical aspects entailing the research and discuss information relevant to obtain stastical results using programming toools.

## **Contextual Information**

In beginning, the **publication** summarizing identified peptide of mouse species \(mouse publication\) **and** glyco FASTA file for mouse was **provided**.

**Glyco protein \(.**FASTA**\):** This file uses special format to list the significant properties of glycol proteins. The FASTA format is as below:

&lt;---example of protein entry from glyco fasta file---&gt;

First line tells information for protein identification and the remainder of lines depicts protein sequence.

The standardized glyco data for indexed species can be found in online BASIC \(Basic Local Alignment Search Tool\) database.

**Mouse publication**\(.pdf\): It lists all identified peptides and associated relevant variables in the study. The mouse publication forms the basis for the information employed for the analysis. This means all piece of peptide information encountered in later parts would be inherited from this single pdf publication. The significant characteristic of each peptide sequence \(one row in publication\) are as listed below:

·CDS ID and Worm pep ID : Technical protein identifiers

·Protein description : description of protein

·Peptide position \(from\)

·Peptide position \(to\)

·Preceding residue

·Peptide sequence

·C-terminal peptide residue

·No. of potential sites

·Glycosylated site-1 and site-2

Again the definitions of these biological variables are not in scope of consideration unless their applicability arises.

Glyco FASTA file and Mouse publication becomes the 

## **Instructions**

The assurance of correctness and durability, each step of data manipulation is broken down in number of steps. Each step signifies milestone whose concrete definitions are determined through appropriate research and requires solving sets of problem statements before proceeding. For instance, first milestone or step may consist of omitting blank rows and convert to tab delimited text file. Afterwards sending the progressed files to Supervisor to receive critical feedback and readjust the methodology accordingly in case of inconsistent calculations/formatting witnessed. Below are the steps or milestone established: