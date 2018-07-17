# Evolutionary Analysis

Results summarized in Excel Sheet : Evo_Analyses_Data.xlsx
Used PAML version 4.8

## Divergence (YN00) - Human/Macaque

### Format Data:
- 'make format' takes the output of the alignment software and generates the files of the format required for analysis in PAML.  
- 'PAML_format.py' is a custom python script I wrote to convert the format.

### YN00
- 'make yn00'  runs PAML YN00 for each gene to analyze pairwise divergence between the human and macaque sequences.
- 'ctl_gen.sh' is a custom shell that generates the PAML .ctl file for each gene.

## Divergence vs. Polymorphism (MK Test) - Human/Macaque


## CODEML - Species Tree

### Format Data:
- 'make format' takes the output of the alignment software and generates the files of the format required for analysis in PAML.  
- 'PAML_format.py' is a custom python script I wrote to convert the format.
- For CODEML, additional edits need to be made before running analysis.  This includes changing the number of sequences in the header of the .fa file from 2 to the appropriate number (usually 16).


## CODEML - Gene Tree

### Construction of Gene Trees:


### CODEML


## MNM Analysis

### Construct Ancestral Sequences - PAML

### Identify & Remove all putative MNM

### CODEML


