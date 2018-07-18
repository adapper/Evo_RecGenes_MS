# Evolutionary Analysis

- Results summarized in Excel Sheet : Evo_Analyses_Data.xlsx
- Used PAML version 4.8

## Divergence (YN00) - Human/Macaque

### Format Data:
- 'make format' takes the output of the alignment software and generates the files of the format required for analysis in PAML.  
- 'PAML_format.py' is a custom python script I wrote to convert the format.

### YN00
- 'make yn00'  runs PAML YN00 for each gene to analyze pairwise divergence between the human and macaque sequences.
- 'ctl_gen.sh' is a custom shell that generates the PAML .ctl file for each gene.

## Divergence vs. Polymorphism (MK Test) - Human/Macaque


## CODEML - Species Tree
Primary Dataset
### Format Data:
- 'make format' takes the output of the alignment software and generates the files of the format required for analysis in PAML.  
- 'PAML_format.py' is a custom python script I wrote to convert the format.
- For CODEML, additional edits need to be made before running analysis.  This includes changing the number of sequences in the header of the .fa file from 2 to the appropriate number (usually 16).


## CODEML - Gene Tree
Looks for spurious results produced by Incomplete Lineage Sorting (ILS).
### Construction of Gene Trees - MrBayes:
1.  Generate NEXUS files ('.nex') for the alignments of interest.
- One way to do this is to use the align files 'Align/GENE.nt_ali.fasta' and the site: http://sequenceconversion.bugaco.com/converter/biology/sequences/fasta_to_nexus.php
2. Run MrBayes
- 'mb' - opens MrBayes in Terminal
- 'execute GENE.nexus' - loads data into MrBayes
- 'lset nst=6 rates=invgamma' - sets the evolutionary model
- 'mcmc ngen=200000 samplefreq=1000 printfreq=1000 diagnfreq=10000' - run model until standard deviation of split frequencies is below 0.01.
- 'sump' - summarize the parameter values. Make sure the potential scale reduction factor (PSRF) is reasonably close to 1.0 for all parameters.
- 'sumt' - summarize the tree.

### CODEML


## MNM Analysis
Looks for spurious results produced by Multi-Nucleotide Mutations (MNM).
### Construct Ancestral Sequences - PAML

### Identify & Remove all putative MNM

### CODEML


