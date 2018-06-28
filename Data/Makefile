## Goal - Phylogenetic Analysis of Recombination Genes

SP_REF=$(wildcard ../refB/*.txt)
SP_FILES=$(patsubst ../refB/%.txt, master/%.fa, $(SP_REF))

GENE_REF=$(wildcard ../refA/*.fa)
GENE_FILES=$(patsubst ../refA/%.fa, gene/%.fa, $(GENE_REF))
GENE_PW_FILES=$(patsubst ../refA/%.fa, gene_pw/%.fa, $(GENE_REF))

## gene         : Generate lists of fastq sequences by gene.
.PHONY : gene
gene : $(GENE_FILES)

gene/%.fa : ../PYcode/gene.py master/master.fa
	python3 $< $* > $@

## gene_pw      : Generate lists of fastq sequences by gene for a pair of species.
.PHONY : gene_pw
gene_pw : $(GENE_PW_FILES)

gene_pw/%.fa : ../PYcode/pairwise.py master/master.fa
	python3 $< $* HUMAN MACAQUE > $@

## master       : Generate a master list of fastq sequences for all species.
.PHONY : master
master : master/master.fa

master/master.fa : $(SP_FILES)
	cat $^ > $@

## species      : Concatenate files by species.
.PHONY : species
species: $(SP_FILES)

master/bat.fa : data/ept_fus.fa data/ept_fus_MEI4.fa data/ept_fus_TEX11.fa data/ept_fus_SYCP2.fa data/ept_fus_REC8.fa
	cat $^ > $@

master/bonobo.fa : data/pan_pan.fa data/pan_pan_CCDC36.fa
	cat $^ > $@

master/chimpanzee.fa : data/pan_troN.fa data/pan_troE.fa data/pan_tro_TEX11.fa
	cat $^ > $@

master/cow.fa : data/bos_tauN.fa data/bos_tauE.fa data/bos_tau_MLH3.fa data/bos_tau_SYCP2.fa data/bos_tau_SYCP1.fa data/bos_tau_MEIOB.fa
	cat $^ > $@

master/dog.fa : data/can_famN.fa data/can_famE.fa data/can_fam_CNTD1.fa data/can_fam_MSH4.fa data/can_fam_MSH5.fa
	cat $^ > $@

master/gorilla.fa : data/gor_gorN.fa data/gor_gorE.fa data/gor_gor_SYCP1.fa
	cat $^ > $@

master/horse.fa : data/equ_cabN.fa data/equ_cabE.fa data/equ_cab_RNF212.fa data/equ_cab_REC114.fa
	cat $^ > $@

master/human.fa : data/hom_sapN.fa data/hom_sapE.fa
	cat $^ > $@

master/macaque.fa : data/mac_mul.fa data/mac_mul_RNF212.fa data/mac_mul_TEX11.fa
	cat $^ > $@

master/marmoset.fa : data/cal_jacN.fa data/cal_jacE.fa data/cal_jac_RNF212.fa data/cal_jac_TEX11.fa
	cat $^ > $@

master/mouse.fa : data/mus_musN.fa data/mus_musE.fa data/mus_mus_CNTD1.fa data/mus_mus_MSH4.fa
	cat $^ > $@

master/orangutan.fa : data/pon_pygN.fa data/pon_pygE.fa data/pon_pyg_RNF212.fa data/pon_pyg_SPO11.fa data/pon_pyg_CCNB1IP1.fa
	cat $^ > $@

master/pig.fa : data/sus_scrN.fa data/sus_scrE.fa data/sus_scr_RNF212.fa data/sus_scr_CNTD1.fa data/sus_scr_HORMAD2.fa data/sus_scr_RAD21L.fa data/sus_scr_MSH4.fa data/sus_scr_MEIOB.fa
	cat $^ > $@

master/rat.fa : data/rat_norN.fa data/rat_norE.fa data/rat_nor_SYCP1.fa
	cat $^ > $@

master/sheep.fa : data/ovi_ariN.fa data/ovi_ariE.fa
	cat $^ > $@

master/treeshrew.fa : data/tup_chi.fa data/tup_chi_RNF212.fa data/tup_chi_MSH4.fa data/tup_chi_MEIOB.fa data/tup_chi_SYCP1.fa
	cat $^ > $@

## variables    : Print variables.
.PHONY : variables

variables :
	@echo SP_REF: $(SP_REF)
	@echo SP_FILES: $(SP_FILES)
	@echo GENE_REF: $(GENE_REF)
	@echo GENE_FILES: $(GENE_FILES)
	@echo GENE_PW_FILES: $(GENE_PW_FILES)
        
## help         : Print help documentation.
.PHONY : help

help : Makefile
	@sed -n 's/^##//p' $<