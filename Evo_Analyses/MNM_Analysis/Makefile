## Goal - Phylogenetic Analysis of Recombination Genes (Remove MNM)

GENE_REF=$(wildcard refC/*.fa)
ALIGN_FILES=$(patsubst refC/%.fa, MNM_Removal/%_ancestral.fa, $(GENE_REF))
OUT_FILES=$(patsubst refC/%.fa, MNM_Removal/%_MNM.fa, $(GENE_REF))

## remove		: Remove all putatitve MNM from sequences.
.PHONY : remove
remove : $()

.fa : $(OUT_FILES) Scripts/step2.sh
	./Scripts/step2.sh $* > $@


## format		: Format alignments for MNM identification.
.PHONY : format
format : $(OUT_FILES) 

MNM_Removal/%_MNM.fa : $(ALIGN_FILES) Scripts/MNM_format.sh
	./Scripts/MNM_format.sh $* > $@

## variables	: Print variables.
.PHONY : variables

variables :
	@echo GENE_REF: $(GENE_REF)
	@echo ALIGN_FILES: $(ALIGN_FILES)
	@echo OUT_FILES: $(OUT_FILES)

## help		: Print help documentation.
.PHONY : help

help : Makefile
	@sed -n 's/^##//p' $<