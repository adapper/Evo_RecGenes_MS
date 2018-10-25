---
date: \today{}
geometry: margin=1in
header-includes:
    - \usepackage{setspace}
    - \doublespacing
    - \usepackage{lineno}
    - \linenumbers
---


**Molecular Evolution of the Meiotic Recombination Pathway in Mammals**

*Investigations*

$~$

Amy L. Dapper^1,2^* and Bret A. Payseur^1^

$~$

^1^ Laboratory of Genetics, University of Wisconsin, Madison, WI 53706, USA

^2^ Current Address: Department of Biological Sciences, Mississippi State University, Mississippi State, MS 39762, USA


\pagebreak

Running Title: Evolution of the Recombination Pathway

Keywords: (up to 5)

$~$

\* Corresponding Author : Amy L. Dapper

Address: 295 E. Lee Blvd., P.O. Box GY, Mississippi State, MS 39762

Phone: (662) 325-7575

Email: dapper@biology.msstate.edu


\pagebreak

## Abstract

Meiotic recombination, the exchange of genetic material between homologous chromosomes during meiosis, is required for successful gametogenesis in most sexually reproducing species. Recombination is also a fundamental evolutionary force, influencing the fate of new mutations and determining the genomic scale over which selection shapes genetic variation. Despite the central importance of recombination, basic questions about its evolution have yet to be addressed.  Although many genes that play roles in recombination have been identified, the molecular evolution of most of these genes remains uncharacterized.  Using a phylogenetic comparative approach, we measure rates of evolution in 32 recombination pathway genes across 16 mammalian species, spanning primates, murids, and laurasithians.  By analyzing a carefully-selected panel of genes involved in key components of recombination – spanning double strand break formation, strand invasion, the crossover/non-crossover decision, and resolution – we generate a comprehensive picture of the evolution of the recombination pathway in mammals. Recombination genes exhibit marked heterogeneity in the rate of protein evolution, both across and within genes.  We report signatures of rapid evolution and positive selection that could underlie species differences in recombination rate.  [WORK HERE]

Abstract Word Count : (< 250)


\pagebreak

## Introduction

The reciprocal exchange of DNA between homologous chromosomes during meiosis – recombination – is required for successful gametogenesis in most species that reproduce sexually [@Hassold2001]. The rate of recombination is a major determinant of patterns of genetic diversity in populations, influencing the fate of new mutations [@Hill1966], the efficacy of selection [@Felsenstein1974; @Charlesworth1993; @Comeron1999; @Gonen2017], and important features of the genomic landscape [@Begun1992; @Charlesworth1994; @Duret2008]. 

Although recombination rate is often treated as a constant, this fundamental parameter evolves over time. Genomic regions ranging in size from short sequences to entire chromosomes vary in recombination rate – both within and between species [@Burt1987; @Broman1998; @Jeffreys2005; @Coop2007; @Kong2010; @Smukowski2011; @Dumont2011B; @Comeron2012; @Segura2013; @Dapper2017; @Stapley2017].

Genome-wide association studies are beginning to reveal the genetic basis of differences in recombination rate within species. Individual recombination rates have been associated with variation in specific genes in populations of *Drosophila melanogaster* [@Hunter2016], humans [@Kong2008; @Chowdhury2009; @Fledel-Alon2011; @Kong2014], domesticated cattle [@Sandor2012; @Ma2015; @Kadri2016; @Shen2018], domesticated sheep [@Petit2017], Soay sheep [@Johnston2016], and red deer [@Johnston2018]. Variants in several of these genes correlate with recombination rate in multiple species, including: *Rnf212* [@Kong2008; @Chowdhury2009; @Fledel-Alon2011; @Sandor2012; @Johnston2016; @Kadri2016; @Petit2017], *Rnf212B* [@Johnston2016; @Kadri2016; @Johnston2018], *Rec8* [@Sandor2012; @Johnston2016; @Johnston2018], *Hei10/Ccnb1ip1* [@Kong2014; @Petit2017], *Msh4* [@Kong2014; @Ma2015; @Kadri2016; @Shen2018], *Cplx1* [@Kong2014; @Ma2015; @Johnston2016; @Shen2018] and *Prdm9* [@Fledel-Alon2011; @Sandor2012; @Kong2014; @Ma2015; @Shen2018].  

In contrast, the genetics of recombination rate variation among species remains poorly understood. Divergence at the di-cistronic gene *mei-217/mei-218* explains much of the disparity in genetic map length between *D. melanogaster* and *D. mauritiana* [@Brand2018]. *mei-217/mei-218* is the only gene known to confer a recombination rate difference between species, though quantitative trait loci that contribute to shifts in rate among subspecies of house mice have been identified [@Dumont2010; @Murdoch2010; @Balcova2016]. 

One strategy for understanding how species diverge in recombination rate is to inspect patterns of molecular evolution at genes involved in the recombination pathway. This approach incorporates knowledge of the molecular and cellular determinants of recombination and is motivated by successful examples. *mei-217/mei-218* was targeted for functional analysis based on its profile of rapid evolution between *D. melanogaster* and *D. mauritiana* [@Brand2018]. *Prdm9*, a protein that positions recombination hotspots in house mice and humans through histone methylation [@Myers2010; @Parvanov2010; @Grey2011; Paigen2018; @Grey2018], shows accelerated divergence across mammals [@Oliver2009]. The rapid evolution of *Prdm9* – which localizes to its zinc-finger DNA binding domain [@Oliver2009] – appears to be driven by selective pressure to recognize new hotpot motifs as old ones are destroyed via biased gene conversion [@Myers2010; @Ubeda2011; @Lesecque2014; @Latrille2017]. Although these examples demonstrate the promise of signatures of molecular evolution for illuminating recombination rate differences between species, patterns of divergence have yet to be reported for most genes involved in meiotic recombination.

Mammals provide a useful system for dissecting the molecular evolution of the recombination pathway for several reasons. First, the evolution of recombination rate has been measured along the mammalian phylogeny [Dumont and Payseur 2008; @Segura2013]. Second, recombination rate variation has been associated with specific genes in mammalian populations [@Kong2008; @Chowdhury2009; @Sandor2012; @Kong2014; @Ma2015; @Johnston2016; @Kadri2016; @Petit2017; @Johnston2018; @Shen2018]. Third, laboratory mice have proven to be instrumental in the identification and functional characterization of recombination genes [@deVries1999; @Yang2006; @Ward2007; @Baudat2000; @Romanienko2000; @LaSalle2012; @Schramm2011; @Bisig2012; @Bolcun-Filas2012; @Kumar2015; @Finsterbusch2016; @Stanzione2016] .

Work in mice indicates that the mammalian recombination pathway is roughly divided into five major steps, each of which is regulated by a handful of genes. The first step is the formation of hundreds of double strand breaks (DSBs) throughout the genome [@Keeney1997; @Bergerat1997; @Baudat2000; @Romanienko2000; @Baudat2007; @Finsterbusch2016; @Lange2016]. After formation, DSBs are identified, processed, and paired with their corresponding location on the homologous chromosome through the processes of homology search and strand invasion [@Keeney2007; @Cloud2012; @Brown2014; @Oh2016; @Kobayashi2016; @Finsterbusch2016; @Xu2017]. The pairing of homologous chromosomes is then stabilized by a proteinaceous structure referred to as the synaptonemal complex (SC) [@Meuwissen1992; @Schmekel1995; @Costa2005; @deVries2005; @Hamer2006; @Yang2006; @Schramm2011; @Fraune2014; @Hernandez2016]. The SC also forms a substrate on which the eventual crossover events will take place [**citations**].  It is at this point that a small subset of DSBs is designated to mature into crossovers, leaving the majority of DSBs to be resolved as non-crossovers [@Snowden2004; @Yang2008; @Reynolds2013; @Finsterbusch2016; @Rao2017].  Finally, this designation is followed, and each DSB is repaired as a crossover or a non-crossover [@Baker1996; @Edelmann1996; @Lipkin2002; @Rogacheva2014; @Xu2017].  

In this article, we examine the molecular evolution of 32 key recombination genes, evenly distributed across each major step in the recombination pathway, in 16 mammalian species spanning Primates, Rodents and Laurasiatherians. In addition to revealing patterns of divergence across diverse mammalian species, we leverage human polymorphism data to make robust evolutionary inferences. Our results provide a comprehensive picture of evolution in the recombination pathway in mammals and identify steps of the pathway most likely to contribute to differences in recombination rate between species.  

## Materials and Methods

### Data Acquisition & Processing

We selected a focal panel of 32 recombination genes (See Table1). The panel was constructed to: (1) cover each major step in the recombination pathway as evenly as possible, (2) contain genes that have integral functions in each step, and (3) include genes that have been associated with inter-individual differences in recombination rate within mammalian populations. Reference sequences were downloaded for each gene from both NCBI and Ensembl (Release-89)[@Wheeler2016; @Zerbino2017].

Alternative splicing is widespread and presents a challenge for molecular evolution studies [@Pan2008; @Barbosa2012]. To focus our analyses on coding sequences that are transcribed during meiosis and to validate the computational annotations for each gene in each species, we used available testes expression datasets. We downloaded raw testes expression data for each mammalian species from NCBI Gene Expression Omnibus (GEO) (Table S1)[@Barrett2012]. We converted the SRA files into FASTQ files using SRAtoolkit [@Leinonen2010]. The reads were mapped to an indexed reference genome (Table S2,3) (Bowtie2, [@Langmead2012]) using TopHat [@Trapnell2009]. The resulting bam files were sorted using Samtools [@Li2009] and visualized using IGV 2.4.10 [@Thorvaldsdottir2013]. This allowed us to: (1) identify the transcript expressed in testes, (2) check the reference transcript for errors, and (3) revise the reference transcript based upon the transcript data.

We compared expression data to annotations from both Ensembl and NCBI [@Wheeler2016; @Zerbino2017]. When both transcripts were identical, we selected the NCBI transcript.  The Ensembl transcript was used instead when: (1) the NCBI reference sequences was not available for a given gene in a given species, (2) when none of the NCBI transcripts matched the expression data, or (3) when there were sequence differences between the two transcripts and the Ensembl transcript was more parsimonious - i.e. had the fewest differences when compared to the rest of sequences in the alignment.  **The use of testes expression data was a key data processing step and the inclusion of species in this study was primarily determined by the availability of testes expression data.**

###  Phylogenetic Comparative Approach in Mammals

For each gene, we used phylogenetic analysis by maximum likelihood (PAML 4.8) to measure the rate of evolution across the mammalian phylogeny and to search for molecular signatures indicative of positive selection (Table 2) [@Yang1997; @Yang2007]. This approach requires a sequence alignment and a phylogenetic tree.  For each gene, sequences were aligned using Translator X, a codon-based alignment tool, powered by MUSCLE v3.8.31 [@Edgar2004; @Abascal2010]. Each alignment was examined by hand and edited as necessary. We used a species tree that reflects current understanding of the phylogenetic relationships of the species included in our study (Figure 1)[@Prasad2008; @Perelman2011; @Fan2013; @Chen2017].

Due to the ambiguity in the relationship between Laurasithians and the placement of tree shrews, we also inferred gene trees using MrBayes [@Ronquist2012; @Fan2013; @Chen2017]. This approach also allowed us to control for effects of incomplete lineage sorting (ILS) [@Pamilo1988; @Rosenberg2002; @Scornavacca2017].  Using gene trees and using the consensus species tree produced highly similar results (Table S4).

For the majority of genes, transcripts from all 16 species were used (19 genes). However, for a number of genes, the chimpanzee and bonobo sequences were identical, in which case only the chimpanzee sequence was included in the analyses (11 genes). In one case, the chimpanzee, bonobo and human sequences were all identical, in which case only the human sequence was included in the analyses. In only a small number of instances, a suitable reference sequence could not be identified for a given species. 

We estimated rates of synonymous and non-synonymous substitutions per site using the CODEML program in PAML4.8 [@Yang2007]. This program considers multiple substitutions per site, different rates of transitions and transversions, and effects of codon usage [@Yang2007]. Rates of substitution were computed for 6 different models of molecular evolution (Table 2). The fit of each model was compared using a likelihood ratio test. Reported substitution rates assume the best-fit model for each gene.

### Identifying Signatures of Selection

To test for positive selection, we compared the fit of models including a class of sites with omega greater than 1 to the fit of models in which all classes of sites have omega values equal to, or less than, 1.  **Specifically, we focused on three comparisons: M1 vs. M2, M7 vs. M8, M8 vs. M8a.** 

### Multinucleotide Mutations

Multi-nucleotide mutations (MNMs) occur when two mutations happen simultaneously in close proximity [@Schrider2011, @Besenbacher2016]. MNMs violate the PAML assumption that the probability of two simultaneous mutations in the same codon is 0 [@Yang2007; @Venkat2018]. Recent work has shown that MNMs can falsely detect positive selection when using branch-site tests in PAML [@Venkat2018]. Although we did not use branch-site tests, it is possible that MNMs contributed to some of the signatures of positive selection we observed. We could not directly identify MNMs in our dataset. Instead, we identified codons with multiple differences (CMDs) that likely arose on a single branch of the phylogeny.  We used PAML to reconstruct the ancestral sequence at each node in the phylogeny [@Yang2007]. For the reconstruction, Model 8 was chosen because we specifically re-analyzed genes that showed evidence for positive selection when comparing Model 7 with Model 8.  From the ancestrally reconstructed sequences, we identified any codons in which PAML inferred more than 1 substitution on a single branch.  All identified CMDs were removed from the sequences in which they occurred. For example, if a CMD was identified in an external branch, that codon was replaced with ‘---’ only in the sequence of that species. If a CMD was inferred on an internal branch, the codon was replaced with ‘---’ in all species descended from that internal branch.  For each gene that showed evidence of positive selection using the unedited sequences, we also conducted PAML analyses using sequences from which all CMDs were removed.

###  Polymorphism & Divergence in the Primate Lineage

To further examine evidence for selection on recombination genes, we compared divergence between humans and macaque to polymorphism within humans.

Human polymorphism data was downloaded from ExAC database.

Not available for 3 genes.
Issues with ExAC data for: RNF212, MEI4 (and REC8)?

Pairwise divergence between humans and macaques was calculated using YN00 package in PAML.

Compared polymorphism within humans to divergence between human and macaques using the McDonald-Kreitman test.

### Identifying Evolutionary Patterns

Statistical Analysis

ERC Analysis

\pagebreak

## Results

Heterogeneity in the rate of evolution of recombination genes, spanning a range of 0.0268 – 0.8483 (Figure 2A).
Mean omega = 0.3275, SD = 0.1971, median = 0.30945
4 genes have omega values more than 1 SD above mean: SYCP2, TEX11, SHOC1, IHO1.
5 genes have omega values more than 1 SD below mean: BRCC3, HEI10, DMC1, RAD51, RAD50.

Do genes that have been associated with inter-individual differences in recombination rate have higher evolutionary rates? Or more likely to show signature of positive selection?
Mean omega value trends higher (0.3943 vs. 0.2925), but not significantly so. (p = 0.2381, Mann-Whitney U Test) (p = 0.1787, t-test)
Higher frequency of genes with a positive signature of selection (45.5% vs. 28.6%), but not significantly so.  (p = 0.4424, Fisher’s Exact Test)

Do the evolutionary rates of genes in different steps of the pathway have different evolutionary rates?  
Yes, but not significantly so (p = 0.1422, Kruskal-Wallis Test) (p = 0.101, ANOVA) (Figure 3).

How about before vs. after synapsis?
Mean omega value is higher for genes that function after synapsis (0.3762 v. 0.2723), but not significantly so (p = 0.1425, Mann-Whitney U Test). (p = 0.1392, t-test)
Significantly higher proportion of genes that function after synapsis have signature of positive selection (53.3% v. 12.5%) (p = 0.0233, Fisher’s Exact Test).

10 genes (31.25%) have a signature of positive selection at some fraction of sites.  These genes include: IHO1, MRE11, SYCP1, SYCP2, REC8, RAD21L, RNF212, TEX11, MSH4, SHOC1.

After removing CMDs, 1 gene (TEX11) retains a robust signature of positive selection.

In general, there is very high concordance between evolutionary rate across mammals and pairwise divergence between humans and macaques (Figure S1).
Mean omega = 0.3301, SD = 0.2370, median = 0.30925
6 genes have omega values more than 1 SD above mean: CNTD1, TEX11, SHOC1, IHO1, MEI4, RAD21L.
6 genes have omega values more than 1 SD below mean: HORMAD1, MRE11, RAD50, DMC1, RAD51, MLH1.

Compared the omega values of recombination genes to a whole-genome distribution of omega values between human & macaque (Gradnigo et al. 2016).
When randomly sampling 32 omega values from the genome-wide distribution, you get a mean as high (or higher) than the value observed among recombination genes less than 1% of the time (p = 0.075, N = 10,000).

Do genes that have been associated with inter-individual differences in recombination rate have higher evolutionary rates (human-macaque)? Or more likely to show signature of positive selection?
Mean omega value trends higher (0.4181 vs. 0.2839), but not significantly so. (p = 0.08816, Mann-Whitney U Test). (p = 0.1123, t-test)

Do the evolutionary rates of genes in different steps of the pathway have different evolutionary rates?
Yes, but not significantly so (p = 0.2682, Kruskal-Wallis Test) (Figure S2). (p = 0.279, ANOVA).

Did you compare rates for genes acting before vs. after synapsis as above?
Mean omega value is higher for genes that function after synapsis (0.3994 v. 0.2514), but not significantly so (p = 0.05827, Mann-Whitney U Test). (p = 0.07783, t-test).

Comparing polymorphism (humans) and divergence (human-macaque) revealed a general pattern of negative/purifying selection.
16 of the 29 genes had a significant MK Test – but, all in the direction of negative (purifying) selection (Fisher’s Exact Test).  None had a significant MK test in the direction of positive selection.
Only one gene (TEX11) had a positive alpha score (alpha = 0.2929) and a corresponding neutrality index less than 1 (NI = 0.7071) – in the direction of positive selection.  

Evidence for correlated evolution of genes in the recombination pathway (mean ERC = 0.134, p = 0.000358, perms = 100,000).  
Among recombination genes, strong signature of correlated evolution between three genes of interest: SHOC1, TEX11, SYCP2 (mean ERC =  0.42369, p = 0.025, perms = 1,000).

\pagebreak

## Discussion

### Heterogeneous rates of evolution of recombination genes across the mammalian phylogeny

Do we observe elevated rates of evolution in certain steps in the recombination pathway?
No - No significant difference in mean omega values among genes that function (*p* = 0.09767, Kruskal-Wallis rank sum test).  

Do we observe more genes with signatures of positive selection in certain steps in the recombination pathway?
Values too small to compare all 5 groups.  Compared earlier steps (N = 15) to later steps (N=17).  Signifcantly more genes with signatures of positve selection in the second half of the recombination pathway (*p* = 0.0457, Pearson's Chi-squared test)

### Evidence of positive selection - PAML

Of the 9 genes with significant signatures of positive selection (7vs8), only one (TEX11) retained the significant signature of selection after removing all CMDs.  Two additional genes (REC8, RAD21L), also showed that model 8 was a significantly better fit than model 7.  However, this is because models that allow a class of sites with a dN/dS of 1 are preferred over models that require all sites to have dN/dS values < 1.  There is limited to no support for a class of sites with dN/dS > 1.  

### Polymorphism & Divergence Data


The rate of meiotic recombination shapes major features of the genomic landscape and influences the efficacy of selection [@hill1966; @felsenstein1974; @begun1992; @charlesworth1993; @charlesworth1994; @comeron1999; @duret2008].  

Recombination rate varies between species [@burt1987; @dumont2011; @smukowski2011], between populations [@koehler2002; @kong2010; @comeron2012], within populations [@broman1998; @cullen2002; @jeffreys2005A], and between the sexes [@burt1991; @ma2015; @johnston2016].  

Ample evidence indicates that phenotypic variation in recombination rate has a genetic component. 

Recombination rate shows resemblance among relatives in human pedigrees [77,106,107], differs among lines raised in a common environment [74,83,85,96,108,109], and responds to artificial selection in Drosophila melanogaster and other insects.  

Broad-sense or narrow-sense heritability estimates from humans, mice, insects, and maize range from 0.08 to 0.69 [73,106,107,110–115].  

A host of experiments using insects attempted to increase and/or decrease the recombination rate [71,73,110,111,115,145–157], demonstrating the potential for recombination rate to respond to directional selection in nature. 

Phylogenetic comparative methods suggest that the genome-wide recombination rate has increased during mammalian evolution [97]. 

PRDM9, a protein that helps determine the position of crossovers in mice and humans, possesses one of the most rapidly evolving (zinc-finger) domains in mammals [163,164]. 

Fecundity and recombination rate may be positively correlated in human mothers [77,165,166]. 

Finally, cellular needs to avoid nondisjunction (by generating at least one crossover per chromosome or chromosome arm) and to minimize costs of double-strand break repair should impose selective bounds on the genome-wide crossover rate in nature [1–4].

There is limited empirical evidence for a role of selection in the evolution of recombination rate.

1.  Recombination rate evolves.
2.  There is a genetic basis.
3.  The same few genes pop up over and over again, suggesting there may be a relatively simple genetic basis to variation in recombination rate.
4.  There has recently been an accelleration in our understanding of the genes involved in the recombination pathway.
5.  Divergence in a subset of these genes is very likely to underlie trait differences.
6.  This should be true whether or not those trait differences are generated by selection or drift.  
7.  Motivates a phylogenetic comparative study of genes in the recombination pathway among mammals.
8.  Analyzing these genes from a pathway perspective may provide insight into which genes, or steps of the pathway, are most likely to be contributing to variation in recombination rate in mammals.
9.  Also provides the opportunity to look for molecular signatures of adaptive evolution.

Meiotic recombination begins with the generation of 100's of double strand breaks (DSB) across the genome.  **SPO11** directly produces the DSBs, but is recruited and activated by a handful of other proteins.  The location of DSB are non-randomly distributed across the genome.  **PRDM9** lays down methylation patterns via sequence-specific DNA binding.

 Recombination rate shows resemblance among relatives in human pedigrees [citations], differs among lines raised in a common environment [citations], and responds to artificial selection [citations].  Artifical selection experiments to increase and/or decrease the recombination rate [citations], demonstrate the potential for recombination rate to respond to directional selection in nature. Beyond the lab, comparisons between species and between populations have uncovered pervasive, and in some cases, rapid evolution of recombination rate [citations].  There is limited direct, empirical evidence for a role of selection in the evolution of recombination rate.  Indirect evidence includes the observation via phylogenetic comparative methods that the genome-wide recombination rate appears to have increased during mammalian evolution [citation] and the observation that fecundity and recombination rate may be positively correlated in human mothers [citations].  However, due to the importance of recombination rate in shaping the genome and response to evolution, the value of understanding its evolution is not strictly tied to the role of selection in shaping the trait. 
 
 While Prdm9 clearly plays a major role in the positioning of recombination events within the genome, it is less clear that Prdm9 significantly impacts the total number of recombination events in the genome [citations].  Prdm9 plays an very early role in the patterning of recombination events. 

\pagebreak

**Table 1** : Recombination Genes

**Gene** | **Function** | **Meiosis-Specific?** 
---|---|---|---|---
**A)** | **DSB Formation** |  |  
*HORMAD1* | chromosome axis, promotes DSB formation | Yes |
*HORMAD2* | chromosome axis | Yes | 
*MEI4* | promotes DSB formation (*MCD recombinosome*) | Yes | 
*REC114* | promotes DSB formation (*MCD recombinosome*) | Yes | 
*IHO1* | promotes DSB formation (*MCD recombinosome*) | Yes |
*SPO11* | transesterase, catalyzes the formation of DSBs | Yes |
**B)** | **DSB Processing/Strand Invasion** |  |
*MRE11* | nuclease, required for DSB formation & processing (*MRN Complex*) | No
*NBS1* |  phosphopeptide binding, required for DSB formation  | No |
 ---  | & processing (*MRN Complex*) |  | 
*RAD50* | ATPase/DNA binding protein,  required for DSB formation | No |
 ---  | & processing (*MRN Complex*) |  | 
*BRCC3* | deubiquitinase, DSB processing | No | 
*DMC1* |  recombinase, strand invasion & homologous pairing | Yes |
*RAD51* |  recombinase, strand invasion & homologous pairing | No |
*SPATA22* | strand invasion & homologous pairing | Yes |
*MEIOB* | oligonucleotide binding, strand invasion & homologous pairing | Yes |
*MCMDC2* | helicase, stabilizes homologous pairing | Yes |
**C)** | **Homologous Pairing** |
*REC8* | cohesion core | Yes |
*RAD21L* | cohesion core | Yes |
*SYCP1* | synaptonemal complex - transverse filament |  |
*SYCP2* | synaptonemal complex - axial element |  | 
*TEX12* | synaptonemal complex - central element | | 
**D1)** | **Crossover vs. Non-Crossover - MutS Recruitment** |
*TEX11* |  |  |
*SHOC1* |  |  |
*CNTD1* |  |  |  
*RNF212* |  |  |
*RNF212B* |  |  |
*MSH4* | recombination crossover control |  |
*MSH5* | recombination crossover control |  |
**D2)** | **Crossover vs. Non-Crossover - MutL Recruitment** |
*MER3* |  |  | 
*HEI10* |  |  |
*MLH1* | promotion of meiotic crossing over |  |
*MLH3* | promotion of meiotic crossing over  |  |
*MUS81* |  |  |

\pagebreak

## Results

\pagebreak

**Table 2**: PAML analysis of 32 recombination genes in mammals [@Yang2007].  

***Gene*** | ***bp*** | ***N*** | ***$\omega$*** | ***M*** | ***M1-M2*** | ***p-value*** | ***M7-M8*** | ***p-value*** | ***M8a-M8*** | ***p-value*** 
---|---|---|---|---|---|---|---|---|---|---
**A)** | | | | | | | | | | | | 
*HORMAD1* | 1212 | 16 | 0.3036 | 7 | 0 | *1.000* | 1.795 | *0.4076* | --- | --- 
*HORMAD2* | 981 | 15 | 0.3153 | 7 | 0 | *1.000* | 3.650 | *0.1612* | --- | --- 
*MEI4* | 1170 | 16 | 0.4332 | 7 | 0 | *1.000* | 0.005 | *0.9976* | --- | --- 
*REC114* | 870 | 15 | 0.4003 | 7 | 0 | *1.000* | 5.384 | *0.0677* | --- | --- 
*IHO1* | 1824 | 16 | 0.7095 | **8** | 13.061 | ***0.0015*** | 17.571 | ***0.0002*** | 14.527 | ***0.0001*** 
*SPO11* | 1188 | 15 | 0.1654 | 7 | 0 | *1.000* | 4.648 | *0.0980* | --- | --- |
**B)** | | | | | | | | | | | | 
*MRE11* | 2136 | 16 | 0.1688 | **8** | 0.363 | *0.8342* | 11.931 | ***0.0026*** | 4.706 | ***0.0301***
*NBS1* | 2289 | 15 | 0.4183 | **8** | 0 | *1.000* | 12.763 | ***0.0017*** | 4.087 |  ***0.0432***
*RAD50* | 3936 | 16 | 0.1006 | 7 | 0 | *1.000* | 0.301 | *0.8605* | --- | ----
*BRCC3* | 954 | 15 | 0.0602 | 7 | 0 | *1.000* | 0.250 | *0.8826* | --- | --- 
*DMC1* | 1020 | 15 | 0.0351 | 1 | 0.488 | *0.7835* | 5.000 | *0.0821* | --- | --- 
*RAD51* | 1017 | 16 | 0.0268 | 7 | 0 | *1.000* | 0 | *1.000* | --- | ---
*SPATA22* | 1101 | 16 | 0.4893 | 7 | 0 | *1.000* | 0.429 | *0.8070* | --- | --- 
*MEIOB* | 1425 | 16 | 0.2341 | 7 | 0 | *1.000* | 0.665 | *0.7172* | --- | ---
*MCMDC2* | 2052 | 16 | 0.2239 | 7 | 0 | *1.000* | 0.628 | *0.7307* | --- | ---
**C)** | | | | | | | | | | | | 
*REC8* | 1833 | 16 | 0.3698 | **8** | 0 | *1.000* | 14.690 | ***0.0006*** | 5.927 | ***0.0149*** |  
*RAD21L* | 1686 | 15 | 0.503 | **8** | 12.124 | ***0.0023*** | 32.050 | ***>0.0001*** | 12.049 | ***0.0005*** | 
*SYCP1* | 3015 | 16 | 0.4337 | **8** | 8.711 | ***0.0128*** | 26.860 | ***>0.0001*** | 9.243 | ***0.0024*** | 
*SYCP2* | 4650 | 16 | 0.5572 | **8**| 11.584 | ***0.0031*** | 37.200 | ***>0.0001*** | 15.838  | ***0.0001*** |  
*TEX12* | 369 | 14 | 0.2297 | 7 | 0.0565 | *0.9721* | 1.549 | *0.4610* | --- | ---
**D1)** | | | | | | | | | | | | 
*TEX11* | 2844 | 15 | 0.8483 | **8** | 60.872 | ***>0.0001***  | 82.665 | ***>0.0001***  | 61.141 | ***>0.0001***  | 
*SHOC1* | 4644 | 16 | 0.6113 | **8** | 12.447 | ***0.0020*** | 30.561 | ***>0.0001*** | 15.645 | ***0.0001*** |
*CNTD1* | 1026 | 15 | 0.2496 | 7 | 0 | *1.000* | 0.936 | *0.6263* | --- | ---  
*RNF212* | 948 | 16  | 0.5014 | **8** | 0 | *1.000* | 16.366 | ***0.0003*** | 5.202 | ***0.0226*** |
*RNF212B* | 906 | 14 | 0.4066 | 7 | 0 | *1.000* | 0.500 | *0.7788* | --- | ---
*MSH4* | 2814 | 16 | 0.2132 | **8** | 16.608 | ***0.0002*** | 39.447 | ***>0.0001*** | 23.238 | ***>0.0001*** | 
*MSH5* | 2565 | 15 | 0.1642 | 7 | 0 | *1.000* | 4.214 | *0.1216* | --- | ---
**D2)** | | | | | | | | | | | |
*MER3* | 4458 | 16 | 0.3633 | 8a | 0 | *1.000* | 12.838 | ***0.0016*** | 3.109 | *0.0779* |  
*HEI10* | 831 | 15 | 0.1226 | 7 | 0 | *1.000* | 0.250 | *0.8826* | --- | ---
*MLH1* | 2313 | 15 | 0.1652 | 8a | 0 | *1.000* | 12.221 | ***0.0022*** | 0.280 | *0.5970* | 
*MLH3* | 4419 | 16 | 0.4444 | 7 | 0 | *1.000* | 3.757 | *0.1528* | --- | ---
*MUS81* | 1665 | 16 | 0.2124 | 7 | 0 | *1.000* | 0.628 | *0.7304* | --- | ---

\pagebreak

**Table 3**: PAML - MNM Analysis

***Gene*** | ***bp*** | ***N*** | ***$\omega$*** | ***M*** | ***M1-M2*** | ***p-value*** | ***M7-M8*** | ***p-value*** | ***M8a-M8*** | ***p-value*** 
---|---|---|---|---|---|---|---|---|---|---
*IHO1* | 1824 | 16 | 0.6104 | 7 | 0 | *1.000* | 0.258 | *0.8789* | --- | ---
*MRE11* | 2136 | 16 | 0.1330 | 7 | 0.226 | *0.8930* | 3.056 | *0.2169* | --- | ---
*NBS1* | 2289 | 15 | 0.3413 | 7 | 0 | *1.000* | 1.956 | *0.3761* | --- | ---
*REC8* | 1833 | 16 | 0.2905 | 7 | 0 | *1.000* | 5.321 | *0.0699* | --- | --- 
*RAD21L* | 1686 | 15 | 0.4271 | 8a | 2.329 | *0.3121* | 9.497 | ***0.0087*** | 1.620 | *0.2031* 
*SYCP1* | 3015 | 16 | 0.3731 | 8a | 3.328 | *0.1893* | 13.440 | ***0.0012*** | 2.122 | *0.1452* 
*SYCP2* | 4650 | 16 | 0.4752 | 7 | 0 | *1.000* | 1.758 | *0.4151* | --- | ---  
*TEX11* | 2844 | 15 | 0.7287 | **8** | 9.989 | ***0.0068***  | 18.776 | ***0.0001***  | 10.656 | ***0.0011***  | 
*SHOC1* | 4644 | 16 | 0.5519 | 8a | 0 | *1.000* | 7.439 | ***0.0242*** | 0.292| *0.5887* |
*RNF212* | 948 | 16  | 0.3685 | 7 | 0 | *1.000* | 0 | *1.000* | --- | --- 
*MSH4* | 2814 | 16 | 0.1509 | 7 |  0 | *1.000* | 2.079 | *0.3536* | --- | ---  

\pagebreak

**Table 4**: Polymorphism & Divergence Data

***Gene*** | ***bp*** | ***Pn*** | ***Ps*** | ***Pn/Ps*** | ***Dn*** | ***Ds*** | ***Dn/Ds*** | ***MK Test*** | ***$\alpha$*** | ***NI*** |  |
---|---|---|---|---|---|---|---|---|---|---|---|
**A)** | | | | | | | | | |
*HORMAD1* | XXX | 84 | 35 | 2.4000 | 5 | 12 | 0.4167 | ***0.0018*** | -4.7600 | 5.7600 | Neg. 
*HORMAD2* | XXX | 80 | 31 | 2.5806 | 7 | 9 | 0.7778 | ***0.0404*** | -2.3180 | 3.3180 | Neg. 
*MEI4* | XXX | 15 | 7 | 2.1429 | 24 | 9 | 2.6667 | *0.7679* | 0.1964 | 0.8036 | ---
*REC114* | XXX | 76 | 37 | 2.0541 | 11 | 14 | 0.7857 | ***0.0392*** | -1.6143 | 2.6143 | Neg.
*IHO1* | XXX | 130 | 64 | 2.0313 | 36 | 19 | 1.8947 | *0.8718* | -0.0720 | 1.0720 | ---
*SPO11* | XXX | 118 | 52 | 2.2692 | 11 | 22 | 0.5000 | ***0.0001*** | -3.5385 | 4.5385 | Neg.
**B)** | | | | | | | | | |
*MRE11* | XXX | 211 | 86 | 2.4535 | 5 | 35 | 0.1429 | ***>0.0001*** | -16.1744 | 17.1744 | Neg.
*NBS1* | XXX | 221 | 93 | 2.3763 | 34 | 25 | 1.3600 | *0.0666* | -0.7473 | 1.7473 | ---
*RAD50* | XXX | 303 | 118 | 2.5678 | 8 | 43 | 0.1860 | ***>0.0001*** | -12.8019 | 13.8019 | Neg.
*BRCC3* | XXX | 13 | 21 | 0.6190 | 2 | 6 | 0.3333 | 0.6888 | -0.8571 | 1.8571 | ---
*DMC1* | XXX | 72 | 42 | 1.7143 | 0 | 11 | 0.0000 | ***>0.0001*** | --- | --- | Neg.
*RAD51* | XXX | 50 | 48 | 1.0417 | 0 | 13 | 0.0000 | ***>0.0001*** | --- | --- | Neg.
*SPATA22* | XXX | 114 | 45 | 2.5333 | 21 | 10 | 2.1000 | *0.6700* | -0.2063 | 1.2063 | ---
*MEIOB* | XXX | 91 | 40 | 2.2750 | 20 | 22 | 0.9091 | ***0.0200*** | -1.5025 | 2.5025 | Neg. 
*MCMDC2* | XXX | 165 | 54 | 3.0556 | 16 | 26 | 0.6154 | ***>0.0001*** | -3.9653 | 4.9653 | Neg.
**C)** | | | | | | | | | |
*REC8* | XXX | 147 | 76 | 1.9342 | 38 | 31 | 1.2258 | *0.1164* | -0.5779 | 1.5779 | ---
*RAD21L* | XXX | 51 | 17 | 3.000 | 27 | 13 | 2.0769 | *0.5051* | -0.4444 | 1.4444 | ---
*SYCP1* | XXX | 213 | 100 | 2.1300 | 33 | 37 | 1.2222 | *0.0546* | -0.7427 | 1.7427 | ---
*SYCP2* | XXX | 429 | 154 | 2.8506 | 74 | 53 | 1.3962 | ***0.0005*** | -1.0417 | 2.0417 | Neg.
*TEX12* | XXX | 31 | 16 | 1.9375 | 2 | 4 | 0.5000 | 0.1836 | -2.875 | 3.875 | ---
**D1)** | | | | | | | | | |
*TEX11* | XXX | 126 | 81 | 1.5556 | 55 | 25 | 2.200 | *0.2234* | 0.2929 | 0.7071 | ---
*SHOC1* | XXX | 368 | 124 | 2.9677 | 85 | 37 | 2.2973 | *0.2521* | -0.2918 | 1.2918 | ---
*CNTD1* | XXX | 81 | 47 | 1.7234 | 13 | 8 | 1.6250 | *1.0000* | -0.0606 | 1.0606 | ---
*RNF212* | XXX | --- | --- | --- | 17 | 18 | 0.9444 | --- | --- | --- | ---
*RNF212B* | XXX | 368 | 124 | 2.9677 | 8 | 12 | 0.6667 | ***0.0013*** | -3.4516 | 4.4516 | Neg.
*MSH4* | XXX | 260 | 94 | 2.7660 | 24 | 29 | 0.8276 | ***>0.0001*** | -2.3422 | 3.3422 | Neg.
*MSH5* | XXX | 197 | 104 | 1.8942 | 19 | 33 | 0.5758 | ***0.0002*** | -2.2900 | 3.2900 | Neg.
**D2)** | | | | | | | | | |
*MER3* | XXX | 402 | 143 | 2.8112 | 54 | 44 | 1.2273 | ***0.0004*** | -1.2906 | 2.2906 | Neg.
*HEI10* | XXX | 73 | 33 | 2.2121 | 4 | 5 | 0.8000 | *0.1541* | -1.7652 | 2.7652 | ---
*MLH1* | XXX | 255 | 90 | 2.8333 | 9 | 29 | 0.3103 | ***>0.0001*** | -8.1296 | 9.1296 | Neg.
*MLH3* | XXX | 437 | 167 | 2.6168 | 77 | 57 | 1.3509 | ***0.0012*** | -0.9370869 | 1.937087 | Neg.
*MUS81* | XXX | 208 | 81 | 2.5679 | 17 | 40 | 0.4250 | ***>0.0001*** | -5.0421 | 6.0421 | Neg.

## Acknowledgements 

A.L.D. was supported by NHGRI Training Grant to the Genomic Sciences Training Program
5T32HG002760. B.A.P. was supported by NIH grant R01 GM100426A and NSF grant DEB
1353737.

\pagebreak

**Table R1**: Testes Expression Datasets

***Species*** | **GEO Accession** | **Reference** 
---|---|---
*Bos taurus* | GSM1020728 & GSM1020746 | @Merkin2012 
*Callithrix jacchus* | GSM1227961, GSM1227962 & GSM1227963 | @Cortez2014
*Canis lupus familiaris* | GSM747469 & GSM1359286 | @Derti2012, @Vandewege2016 
*Eptesicus fuscus* | GSM1359287 | @Vandewege2016 
*Equus caballus* | GSM1139276 & GSM1359288 | @Coleman2013, @Vandewege2016
*Gorilla gorilla* | GSM752663 | @Brawand2011
*Homo sapiens* | GSM752707 & GSM752708 | @Brawand2011
*Macaca mulatta* | GSM752642 & GSM752643 | @Brawand2011
*Mus musculus* | GSM752629 & GSM752630 | @Brawand2011
*Ovis aries* | GSM1666944 & GSM1666936 | @Guan2017
*Pan paniscus* | GSM752690 | @Brawand2011
*Pan troglodytes* | GSM752678 | @Brawand2011
*Pongo pygmaeus* | GSM1858310 & GSM1858311 | @Carelli2016
*Rattus norvegicus* | GSM1278058 | @Cortez2014 
*Sus scrofa* | GSM1902350, GSM2033157 & GSM2033163 | @Li2016, @Yang2017
*Tupaia chinensis* | GSM957062 | @Fan2013

**Table R2**: Reference Genomes [@OLeary2015]

***Species*** | **Assembly** | **RefSeq Accession** | **WGS Project Reference**
---|---|---|---
*Bos taurus* | Bos_taurus_UMD_3.1.1 | GCF_000003055.6 | @Zimin2009 
*Callithrix jacchus* | Callithrix_jacchus-3.2 | GCF_000004665.1 | -
*Canis lupus familiaris* | CanFam3.1 | GCF_000002285.3 | @Lindblad2005 
*Eptesicus fuscus* | EptFus1.0 | GCF_000308155.1 | -
*Equus caballus* | EquCab2.0 | GCF_000002305.2 | @Wade2009
*Gorilla gorilla* | gorGor4 | GCF_000151905.2 | @Scally2012
*Homo sapiens* | GRCh38.p10 | GCF_000001405.36 | -
*Macaca mulatta* | Mmul_8.0.1 | GCF_000772875.2 | @Zimin2014
*Mus musculus* | GRCm38.p5 | GCF_000001635.25 | -
*Ovis aries* | Oar_v4.0 | GCF_000298735.2 | @Sheep2010
*Pan paniscus* | panpan1.1 | GCF_000258655.2 | @Prufer2012
*Pan troglodytes* | Pan_tro_3.0 | GCF_000001515.7 | @TCsequencing2005
*Pongo abelii* | P_pygmaeus_2.0.2 | GCF_000001545.4 | @Locke2011
*Rattus norvegicus* | Rnor_6.0 | GCF_000001895.5 | @Rat2004
*Sus scrofa* | Sscrofa11.1 | GCF_000003025.6 | -
*Tupaia chinensis* | TupChi_1.0 | GCF_000334495.1 | @Fan2013

**Table R3**: Ensembl Annotations

***Species*** | **Assembly** | **RefSeq Accession** | **WGS Project Reference**
---|---|---|---
*Bos taurus* | Bos_taurus_UMD_3.1 | GCF_000003055.3 | @Zimin2009  
*Callithrix jacchus* | Callithrix_jacchus-3.2 | GCF_000004665.1 | -
*Canis lupus familiaris* | CanFam3.1 | GCF_000002285.3 | @Lindblad2005 
*Eptesicus fuscus* | - | - | -
*Equus caballus* | EquCab2.0 | GCF_000002305.2 | @Wade2009
*Gorilla gorilla* | gorGor3.1 | GCF_000151905.1 | -
*Homo sapiens* | GRCh38.p10 | GCF_000001405.36 | -
*Macaca mulatta* | Mmul_8.0.1 | GCF_000772875.2 | @Zimin2014
*Mus musculus* | GRCm38.p5 | GCF_000001635.25 | -
*Ovis aries* | Oar_v3.1 | GCF_000298735.1 | @Sheep2010
*Pan paniscus* | panpan1.1 | GCF_000258655.2 | @Prufer2012
*Pan troglodytes* | CHIMP2.1.4 | GCF_000001515.6 | @TCsequencing2005
*Pongo abelii* | PPYG2 | GCF_000001545.4 | @Locke2011
*Rattus norvegicus* | Rnor_6.0 | GCF_000001895.5 | @Rat2004 
*Sus scrofa* | Sscrofa11.1 | GCF_000003025.6 | -
*Tupaia chinensis* | - | - | -

**Table S1**: Sequence divergence between Human (*Homo sapiens*) and Rhesus Macaque (*Macaca mulatta*) [@Yang2000,@Yang2007].  Steps: A - double strand break (DSB) formation, B - DSB processing & Strand Invasion, C - Homologous Pairing, D1 - crossover (CO) vs. non-crossover (NCO) step1 - MutS, D2 - CO vs. NCO step 2 - MutL.

***Gene*** | ***bp*** | ***$\omega$*** | ***S*** | ***N*** | ***t*** | ***$\kappa$*** | ***dN*** | ***dS*** | 
---|---|---|---|---|---|---|---|---|---|
**A)** | | | | | | | | | |
*HORMAD1* | XXX | **0.0901** | 273.9 | 908.1 | 0.0443 | 3.8819 | 0.0044 +- 0.0022 | 0.0490 +- 0.0137
*HORMAD2* | XXX | **0.295** | 256.7 | 664.3 | 0.0531 | 4.2164 | 0.0106 +- 0.0040 | 0.0360 +- 0.0121
*MEI4* | XXX | **0.7252** | 331 | 824 | 0.0822 | 4.6295 | 0.0247 +/- 0.0056 | 0.0341 +/- 0.0104 
*REC114* | XXX | **0.3239** | 237.2 | 557.8 | 0.0974 | 2.9455 | 0.0200 +/- 0.0061 | 0.0618 +/- 0.0168 
*IHO1* | XXX | **0.6608** | 509 | 1273 | 0.0951 | 3.6035 | 0.0276 +- 0.0047 | 0.0418 +- 0.0094
*SPO11* | XXX | **0.1434** | 291.2 | 896.8 | 0.0872 | 2.5317 | 0.0118 +/- 0.0036 | 0.0823 +/- 0.0178 
**B)** | | | | | | | | | |
*MRE11* | XXX | **0.0392** | 479.4 | 1644.6 | 0.0597 | 2.6154 | 0.0030 +- 0.0014 | 0.0778 +- 0.0135
*NBS1* | XXX | **0.4155** | 553.7 | 1705.3 | 0.0804 | 5.0955 | 0.0199 +- 0.0035 | 0.0480 +- 0.0097
*RAD50* | XXX | **0.0714** | 1118.7 | 2817.3 | 0.0401 | 5.0903 | 0.0028 +- 0.0010 | 0.0399 +- 0.0062
*BRCC3* | XXX | **0.0979** | 264 | 609 | 0.028 | 4.6 | 0.0025 +- 0.0020 | 0.0252 +- 0.0100
*DMC1* | XXX | **0.0000** | 273.7 | 746.3 | 0.0335 | 5.1279 | 0.0000 +- 0.0000 | 0.0416 +- 0.0127
*RAD51* | XXX | **0.0000** | 306.5 | 710.5 | 0.0398 | 6.7467 | 0.0000 +- 0.0000 | 0.0441 +- 0.0124
*SPATA22* | XXX | **0.4523** | 247.8 | 841.2 | 0.0879 | 3.6505 | 0.0230 +- 0.0053 | 0.0508 +- 0.0150
*MEIOB* | XXX | **0.2462** | 348.9 | 1064.1 | 0.0927 | 4.3887 | 0.0176 +- 0.0041 | 0.0715 +- 0.0151
*MCMDC2* | XXX | **0.2108** | 534 | 1509 | 0.0635 | 7.8547 | 0.0107 +- 0.0027 | 0.0507 +- 0.0101
**C)** | | | | | | | | | |
*REC8* | XXX | **0.477** | 497 | 1138 | 0.1293 | 2.8869 | 0.0323 +- 0.0054 | 0.0678 +- 0.0122
*RAD21L* | XXX | **0.6334** | 427.5 | 1237.5 | 0.0735 | 5.6876 | 0.0213 +- 0.0042 | 0.0337 +- 0.0091
*SYCP1* | XXX | **0.3676** | 761.6 | 2166.4 | 0.0628 | 4.8307 | 0.0145 +- 0.0026 | 0.0393 +- 0.0074
*SYCP2* | XXX | **0.3873** | 1070.7 | 3519.3 | 0.0854 | 5.994 | 0.0208 +- 0.0025 | 0.0537 +- 0.0074
*TEX12* | XXX | **0.1349** | 80.2 | 288.8 | 0.05 | 1.9678 | 0.0070 +- 0.0049 | 0.0516 +- 0.0260
**D1)** | | | | | | | | | |
*TEX11* | XXX | **0.9068** | 805.9 | 1933.1 | 0.0897 | 7.8022 | 0.0290 +- 0.0040 | 0.0320 +- 0.0064
*SHOC1* | XXX | **0.7225** | 1203 | 3129 | 0.0865 | 9.5737 | 0.0261 +- 0.0029 | 0.0361 +- 0.0057
*CNTD1* | XXX | **0.6803** | 335.3 | 651.7 | 0.065 | 8.0721 | 0.0187 +- 0.0054 | 0.0274 +- 0.0092
*RNF212* | XXX | **0.387** | 243.2 | 572.8 | 0.1342 | 4.996 | 0.0304 +- 0.0074 | 0.0785 +- 0.0189
*RNF212B* | XXX | **0.2566** | 255.6 | 644.4 | 0.0685 | 3.4122 | 0.0125 +- 0.0044 | 0.0488 +- 0.0143
*MSH4* | XXX | **0.2635** | 731.3 | 2073.7 | 0.058 | 7.5194 | 0.0112 +- 0.0023 | 0.0425 +- 0.0079
*MSH5* | XXX | **0.2106** | 728.7 | 1770.3 | 0.0643 | 3.9993 | 0.0102 +- 0.0024 | 0.0486 +- 0.0085
**D2)** | | | | | | | | | |
*MER3* | XXX | **0.3247** | 987.6 | 3317.4 | 0.0703 | 7.0099 | 0.0159 +- 0.0022 | 0.0488 +- 0.0074
*HEI10* | XXX | **0.3235** | 241.5 | 589.5 | 0.0329 | 5.9591 | 0.0068 +- 0.0034 | 0.0211 +- 0.0095
*MLH1* | XXX | **0.0924** | 602.3 | 1665.7 | 0.0522 | 2.4752 | 0.0048 +- 0.0017 | 0.0521 +- 0.0097
*MLH3* | XXX | **0.4919** | 1209.8 | 3149.2 | 0.0949 | 6.4296 | 0.0246 +- 0.0028 | 0.0500 +- 0.0067
*MUS81* | XXX | **0.1299** | 465.8 | 1187.2 | 0.1106 | 5.7915 | 0.0128 +- 0.0033 | 0.0983 +- 0.0158

\pagebreak

**Table S2**: PAML - Gene Trees 

***Gene*** | ***bp*** | ***N*** | ***$\omega$*** | ***M*** | ***M1-M2*** | ***p-value*** | ***M7-M8*** | ***p-value*** | ***M8a-M8*** | ***p-value*** 
---|---|---|---|---|---|---|---|---|---|---
**A)** | | | | | | | | | | | | 
*HORMAD1* | 1212 | 16 | 0.3037 | 7 | 0 | *1.000* | 3.135 | *0.2086* | --- | --- 
*HORMAD2* | 981 | 15 | 0.3290 | 1 | 0 | *1.000* | 3.881 | *0.1436* | --- | --- 
*MEI4* | 1170 | 16 | 0.4310 | 7 | 0 | *1.000* | 0.058 | *0.9715* | --- | --- 
*REC114* | 870 | 15 | 0.4237 | 7 | 0 | *1.000* | 4.1874 | *XXXX* | --- | --- 
*IHO1* | 1824 | 16 | 0.7099 | **8** | 13.384 | ***0.0012*** | 17.714 | ***0.0001*** | 14.707 | ***0.0001*** 
*SPO11* | 1188 | 15 | 0.1701 | 7 | 0 | *1.000* | 4.697 | *0.0955* | --- | --- |
**B)** | | | | | | | | | | | | 
*MRE11* | 2136 | 16 | 0.1686 | **8** | 0.636 | *0.7277* | 12.014 | ***XXXX*** | 4.822 | ***XXXX***
*NBS1* | 2289 | 15 | 0.4185 | **8** | 0 | *1.000* | 12.899 | ***XXXX*** | 4.298 |  ***XXXX***
*RAD50* | 3936 | 16 | XXXX | XXXX | XXXX | *XXXX* | XXXX | *XXXX* | --- | ----
*BRCC3* | 954 | 15 | 0.0601 | 7 | 0 | *1.000* | 0.573 | *XXXX* | --- | --- 
*DMC1* | 1020 | 15 | 0.0365 | 7 | 0 | *1.000* | 4.288 | *0.1172* | --- | --- 
*RAD51* | 1017 | 16 | 0.0322 | 1 | 0 | *1.000* | 0.562 | *XXXX* | --- | ---
*SPATA22* | 1101 | 16 | 0.4932 | 7 | 0 | *1.000* | 0.200 | *XXXX* | --- | --- 
*MEIOB* | 1425 | 16 | 0.2340 | 7 | 0 | *1.000* | 0.221 | *XXXX* | --- | ---
*MCMDC2* | 2052 | 16 | 0.2242 | 7 | 0 | *1.000* | 0.610 | *0.7370* | --- | ---
**C)** | | | | | | | | | | | | 

*REC8* | 1833 | 16 | 0.3698 | **8** | 0 | *1.000* | 14.690 | ***0.0006*** | 5.927 | ***0.0149*** |  
*RAD21L* | 1686 | 15 | 0.503 | **8** | 12.124 | ***0.0023*** | 32.050 | ***>0.0001*** | 12.049 | ***0.0005*** | 
*SYCP1* | 3015 | 16 | 0.4337 | **8** | 8.711 | ***0.0128*** | 26.860 | ***>0.0001*** | 9.243 | ***0.0024*** | 
*SYCP2* | 4650 | 16 | 0.5572 | **8**| 11.584 | ***0.0031*** | 37.200 | ***>0.0001*** | 15.838  | ***0.0001*** |  
*TEX12* | 369 | 14 | 0.2297 | 7 | 0.0565 | *0.9721* | 1.549 | *0.4610* | --- | ---
**D1)** | | | | | | | | | | | | 
*TEX11* | 2844 | 15 | 0.8483 | **8** | 60.872 | ***>0.0001***  | 82.665 | ***>0.0001***  | 61.141 | ***>0.0001***  | 
*SHOC1* | 4644 | 16 | 0.6113 | **8** | 12.447 | ***0.0020*** | 30.561 | ***>0.0001*** | 15.645 | ***0.0001*** |
*CNTD1* | 1026 | 15 | 0.2496 | 7 | 0 | *1.000* | 0.936 | *0.6263* | --- | ---  
*RNF212* | 948 | 16  | 0.5014 | **8** | 0 | *1.000* | 16.366 | ***0.0003*** | 5.202 | ***0.0226*** |
*RNF212B* | 906 | 14 | 0.4066 | 7 | 0 | *1.000* | 0.500 | *0.7788* | --- | ---
*MSH4* | 2814 | 16 | 0.2132 | **8** | 16.608 | ***0.0002*** | 39.447 | ***>0.0001*** | 23.238 | ***>0.0001*** | 
*MSH5* | 2565 | 15 | 0.1642 | 7 | 0 | *1.000* | 4.214 | *0.1216* | --- | ---
**D2)** | | | | | | | | | | | |
*MER3* | 4458 | 16 | 0.3633 | 8a | 0 | *1.000* | 12.838 | ***0.0016*** | 3.109 | *0.0779* |  
*HEI10* | 831 | 15 | 0.1226 | 7 | 0 | *1.000* | 0.250 | *0.8826* | --- | ---
*MLH1* | 2313 | 15 | 0.1652 | 8a | 0 | *1.000* | 12.221 | ***0.0022*** | 0.280 | *0.5970* | 
*MLH3* | 4419 | 16 | 0.4444 | 7 | 0 | *1.000* | 3.757 | *0.1528* | --- | ---
*MUS81* | 1665 | 16 | 0.2124 | 7 | 0 | *1.000* | 0.628 | *0.7304* | --- | ---

## References


