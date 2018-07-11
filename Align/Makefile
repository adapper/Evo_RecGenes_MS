## Goal - Phylogenetic Analysis of Recombination Genes (Align Sequences)

GENE_REF=$(wildcard ../refA/*.fa)
GENE_FILES=$(patsubst ../refA/%.fa, ../Data/gene/%.fa, $(GENE_REF))
GENE_PW_FILES=$(patsubst ../refA/%.fa, ../Data/gene_pw/%.fa, $(GENE_REF))
ALIGN_FILES=$(patsubst ../refA/%.fa, align/%.nt_ali.fasta, $(GENE_REF))
ALIGN_PW_FILES=$(patsubst ../refA/%.fa, align_pw/%.nt_ali.fasta, $(GENE_REF))

## align        : Use translator X to align sequeneces (codon-based).
.PHONY : align
align : $(ALIGN_FILES)

align/%.nt_ali.fasta : $(GENE_FILES) translatorx_vLocal.pl
	perl translatorx_vLocal.pl -i ../Data/gene/$*.fa -o align/$* 

## align_pw     : Use translator X to align sequences - pairwise (codon-based).
.PHONY : align_pw
align_pw : $(ALIGN_PW_FILES)

align_pw/%.nt_ali.fasta : $(GENE_PW_FILES) translatorx_vLocal.pl
	perl translatorx_vLocal.pl -i ../Data/gene_pw/$*.fa -o align_pw/$*

## variables    : Print variables.
.PHONY : variables

variables :
	@echo GENE_REF: $(GENE_REF)
	@echo GENE_FILES: $(GENE_FILES)
	@echo ALIGN_FILES: $(ALIGN_FILES)
	@echo ALIGN_PW_FILES: $(ALIGN_PW_FILES)
        
## help         : Print help documentation.
.PHONY : help

help : Makefile
	@sed -n 's/^##//p' $<