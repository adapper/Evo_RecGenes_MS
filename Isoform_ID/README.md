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

Need to do some light edits of the sequence to make sure each sequences is labeled with the common name of the species (i.e. >RAT).  Also, to make sure the name of the gene that the Makefile will recognize is in the informational header.  For example, RNF212 needs to become RNF212A.

## Re-check alignment.

There are four files in this folder:
- README.md
- Excel Spreadsheet: expression_samples_list.xlsx contains the transcripts identified in for each gene in each species on the first pass.
- transcript-master.md: contains links that download sequence data for specific set of transcripts in each species 
- ALIGNinfo.md: contains the list of transcripts identified in the second pass (used for analyses)

