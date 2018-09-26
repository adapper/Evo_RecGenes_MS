## Goal - Phylogenetic Analysis of Recombination Genes (Generate Figures)

GENE_REF=$(wildcard ../refA/*.fa)
PRO_ALIGN_FILES=$(patsubst ../refA/%.fa, ../Align/align/%.aa_ali.fasta, $(GENE_REF))
AA_DIV_FILES=$(patsubst ../refA/%.fa, ../Data/summary_files/%_aa_div.txt, $(GENE_REF)) 
AA_DIV_FIGS=$(patsubst ../refA/%.fa, %_aa_div.png, $(GENE_REF))

## aa_div		: Calculate Amino Acid Diversity & Plot.
.PHONY : aa_div
aa_div : $(AA_DIV_FILES) $(AA_DIV_FIGS)

../Data/summary_files/%_aa_div.txt : $(PRO_ALIGN_FILES) ../PYcode/aa_diversity.py ../Rcode/aa_div_plot.R
	python3 ../PYcode/aa_diversity.py $* > $@
	Rscript ../Rcode/aa_div_plot.R $*

## variables	: Print variables.
.PHONY : variables
variables :
	@echo GENE_REF: $(GENE_REF)
	@echo ALIGN_FILES: $(ALIGN_FILES)
	@echo PRO_ALIGN_FILES: $(PRO_ALIGN_FILES)
	@echo AA_DIV_FILES: $(AA_DIV_FILES)

## help		: Print help documentation.
.PHONY : help
help : Makefile
	@sed -n 's/^##//p' $<
