## Align testes expression data to the reference genome for each species.

Data downloaded from NCBI Geo (SRA).

Alignment performed on Deepthought:
- dapper(at)deepthought.genetics.wisc.edu

Information about the alignment, including reference genome, SRA files, and mapping can be found in the README and Makefiles for each species on Deepthought.

## Use the expression data to identify the correct isoform/transcript for each gene.

Use IGVtools (2.4.2 & 2.3.92) to visualize alignments using both NCBI & Ensembl data.

- IGVtools in Programs folder on Desktop.
- Select reference genome from dropdown menu (.fa) and load annotation file (.gff3), and alignment files (.sorted.bam).  Files stored on red external hard drive due to size.
- Sashimi plots are very helpful for this step.

Information about transcripts from this step can be found in expression_samples_list.xlsx.

## Download sequences. 

Links that will download the sequences for each species can be found in the transcript-master.md file.  The raw data is in the Data folder by species.
- gen_speN.fa : sequences from NCBI
- gen_speE.fa : sequences from Ensembl
- gen_spe_GENE.fa : edited sequences by gene

Need to do some light edits of the sequence to make sure each sequences is labeled with the common name of the species (i.e. >RAT).  
- Make sure the name of the gene that the Makefile will recognize is in the informational header.  For example, RNF212 needs to become RNF212A.  
- Make sure that the name of one gene isn't in the description of another (i.e. CCDC36).
- Make sure that each file ends on a new line to prevent problems at 'cat' steps.

## Align the sequences for each gene.

1. Enter the command 'make' in the 'Data' folder:

- The command 'make species' takes the raw data in the 'data' folder and makes a single file for each species (species.fa).
- The command 'make master' combines all the species files (species.fa) into one large master file (master.fa).
- The command 'make gene' takes the master file and makes a single file for each gene (gene.fa).

Needs two custom python scripts: gene.py, pairwise.py

Alternative - 'make gene_pw' makes pairwise alignments of two species designated in the Makefile.

2. Enter the command 'make' in the 'Align' folder.

Needs two programs: translatorX & muscle

## Re-check alignment.

There are four files in this folder:
- README.md
- Excel Spreadsheet: expression_samples_list.xlsx contains the transcripts identified in for each gene in each species on the first pass.
- transcript-master.md: contains links that download sequence data for specific set of transcripts in each species 
- ALIGNinfo.md: contains the list of transcripts identified in the second pass (used for analyses)

