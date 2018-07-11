## Goal - Phylogenetic Analysis of Recombination Genes (Evolutionary Analyses)

GENE_REF=$(wildcard ../refA/*.fa)
GENE_FILES=$(patsubst ../refA/%.fa, ../Data/gene/%.fa, $(GENE_REF))
ALIGN_FILES=$(patsubst ../refA/%.fa, ../Align/align/%.nt_ali.fasta, $(GENE_REF))
ALIGN_PW_FILES=$(patsubst ../refA/%.fa, ../Align/align_pw/%.nt_ali.fasta, $(GENE_REF))
YN00_FILES=$(patsubst ../refA/%.fa, Yn00/%.YN00.fasta, $(GENE_REF))
yn00_FILES=$(patsubst ../refA/%.fa, Yn00/%_yn, $(GENE_REF))
CODEML_FILES=$(patsubst ../refA/%.fa, Codeml/%.CODEML.fasta, $(GENE_REF))

## yn00		: Calculate pairwise divergence.
.PHONY : yn00
yn00 : $(yn00_FILES)

Yn00/%_yn : $(YN00_FILES)
	./ctl_gen.sh $* > Yn00/$*_yn00.ctl
	paml4.8/src/yn00 Yn00/$*_yn00.ctl

## format		: Format pairwise alignments for use with PAML.
.PHONY : format
format : $(YN00_FILES) $(CODEML_FILES)

Yn00/%.YN00.fasta : $(ALIGN_PW_FILES) ../PYcode/PAML_format.py
	python3 ../PYcode/PAML_format.py $* ../Align/align_pw > $@

Codeml/%.CODEML.fasta : $(ALIGN_FILES) ../PYcode/PAML_format.py
	python3 ../PYcode/PAML_format.py $* ../Align/align > $@

## variables	: Print variables.
.PHONY : variables

variables :
	@echo GENE_REF: $(GENE_REF)
	@echo GENE_FILES: $(GENE_FILES)
	@echo ALIGN_FILES: $(ALIGN_FILES)
	@echo ALIGN_PW_FILES: $(ALIGN_PW_FILES)
	@echo YN00_FILES: $(YN00_FILES)
	@echo CODEML_FILES: $(CODEML_FILES)

## help		: Print help documentation.
.PHONY : help

help : Makefile
	@sed -n 's/^##//p' $<