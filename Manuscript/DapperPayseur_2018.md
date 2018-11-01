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

^2^ Department of Biological Sciences, Mississippi State University, Mississippi State, MS 39762, USA


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

Meiotic recombination, the exchange of genetic material between homologous chromosomes during meiosis, is required for successful gametogenesis in most sexually reproducing species. Recombination is also a fundamental evolutionary force, influencing the fate of new mutations and determining the genomic scale over which selection shapes genetic variation. Despite the central importance of recombination, basic questions about its evolution have yet to be addressed.  Although many genes that play roles in recombination have been identified, the molecular evolution of most of these genes remains uncharacterized.  Using a phylogenetic comparative approach, we measure rates of evolution in 32 recombination pathway genes across 16 mammalian species, spanning primates, murids, and laurasithians.  By analyzing a carefully-selected panel of genes involved in key components of recombination – spanning double strand break formation, strand invasion, the crossover/non-crossover decision, and resolution – we generate a comprehensive picture of the evolution of the recombination pathway in mammals. Recombination genes exhibit marked heterogeneity in the rate of protein evolution, both across and within genes.  We report signatures of rapid evolution and positive selection that could underlie species differences in recombination rate.  **[NEEDS WORK HERE]**

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

We selected a focal panel of 32 recombination genes (See Table1). The panel was constructed to: (1) cover each major step in the recombination pathway as evenly as possible, (2) contain genes that have integral functions in each step, and (3) include genes that have been associated with inter-individual differences in recombination rate within mammalian populations. Reference sequences were downloaded for each gene in 16
110 mammalian species from both NCBI and Ensembl (Release-89)[@Wheeler2006; @Zerbino2017].

Alternative splicing is widespread and presents a challenge for molecular evolution studies [@Pan2008; @Barbosa2012]. To focus our analyses on coding sequences that are transcribed during meiosis and to validate the computational annotations for each gene in each species, we used available testes expression datasets. We downloaded raw testes expression data for each mammalian species from NCBI Gene Expression Omnibus (GEO) (Table S1)[@Barrett2012]. We converted the SRA files into FASTQ files using SRAtoolkit [@Leinonen2010]. The reads were mapped to an indexed reference genome (Table S2,3) (Bowtie2, [@Langmead2012]) using TopHat [@Trapnell2009]. The resulting bam files were sorted using Samtools [@Li2009] and visualized using IGV 2.4.10 [@Thorvaldsdottir2013]. This allowed us to: (1) identify the transcript expressed in testes, (2) check the reference transcript for errors, and (3) revise the reference transcript based upon the transcript data.

We compared expression data to annotations from both Ensembl and NCBI [@Wheeler2006; @Zerbino2017]. When both transcripts were identical, we selected the NCBI transcript.  The Ensembl transcript was used instead when: (1) the NCBI reference sequences was not available for a given gene in a given species, (2) when none of the NCBI transcripts matched the expression data, or (3) when there were sequence differences between the two transcripts and the Ensembl transcript was more parsimonious - i.e. had the fewest differences when compared to the rest of sequences in the alignment.  **The use of testes expression data was a key data processing step and the inclusion of species in this study was primarily determined by the availability of testes expression data.**

###  Phylogenetic Comparative Approach in Mammals

For each gene, we used phylogenetic analysis by maximum likelihood (PAML 4.8) to measure the rate of evolution across the mammalian phylogeny and to search for molecular signatures indicative of positive selection (Table 2) [@Yang1997; @Yang2007]. This approach requires a sequence alignment and a phylogenetic tree.  For each gene, sequences were aligned using Translator X, a codon-based alignment tool, powered by MUSCLE v3.8.31 [@Edgar2004; @Abascal2010]. Each alignment was examined by hand and edited as necessary. We used a species tree that reflects current understanding of the phylogenetic relationships of the species included in our study (Figure 1)[@Prasad2008; @Perelman2011; @Fan2013; @Chen2017].

Due to the ambiguity in the relationship between Laurasithians and the placement of tree shrews, we also inferred gene trees using MrBayes [@Ronquist2012; @Fan2013; @Chen2017]. This approach also allowed us to control for effects of incomplete lineage sorting (ILS) [@Pamilo1988; @Rosenberg2002; @Scornavacca2017].  Using gene trees and using the consensus species tree produced highly similar results (Table S4).

For the majority of genes, transcripts from all 16 species were used (19 genes). However, for a number of genes, the chimpanzee and bonobo sequences were identical, in which case only the chimpanzee sequence was included in the analyses (11 genes). In one case, the chimpanzee, bonobo and human sequences were all identical, in which case only the human sequence was included in the analyses. In only a small number of instances, a suitable reference sequence could not be identified for a given species. 

We estimated rates of synonymous and non-synonymous substitutions per site using the CODEML program in PAML4.8 [@Yang2007]. This program considers multiple substitutions per site, different rates of transitions and transversions, and effects of codon usage [@Yang2007]. Rates of substitution were computed for 6 different models of molecular evolution (Table 2). The fit of each model was compared using a likelihood ratio test. Reported substitution rates assume the best-fit model for each gene.

### Identifying Signatures of Selection

To test for positive selection, we compared the fit of models including a class of sites with $\omega$ greater than 1 to the fit of models in which all classes of sites have $\omega$ values equal to, or less than, 1.  Specifically, we report three comparisons: M1 vs. M2, M7 vs. M8, M8 vs. M8a (Table 2). The first comparison, M1 vs. M2, compares a model with two classes of sites ($\omega$  < 1, $\omega$ = 1) to a model with a third class of sites where $\omega$ is greater than 1, indicative of positive selection [@Yang2007]. More complex models (M7 & M8) were developed to take into account variation in $\omega$ less than one among sites within genes and thus, include 10 site classes drawn from a beta distribution between 0 and 1 [@Yang2007]. In this case, Model 8 includes an additional 11 class of sites in which $\omega$ is greater than 1, allowing for the identification of signatures of positive selection [@Yang2007]. In cases in which a large fraction of sites within a gene are evolving neutrally ($\omega$ = 1), Model 8 will fit significantly better due to a very poor fit of Model 7 rather than a signature of positive selection. To avoid incorrectly identifying signature of positive selection, Model 8 is also compared to Model 8a which contains a larger fraction of neutrally evolving sites than Model 7 [citations].

### Multinucleotide Mutations

Multi-nucleotide mutations (MNMs) occur when two mutations happen simultaneously in close proximity [@Schrider2011; @Besenbacher2016]. MNMs violate the PAML assumption that the probability of two simultaneous mutations in the same codon is 0 [@Yang2007; @Venkat2018]. Recent work has shown that MNMs can falsely detect positive selection when using branch-site tests in PAML [@Venkat2018]. Although we did not use branch-site tests, it is possible that MNMs contributed to some of the signatures of positive selection we observed. We could not directly identify MNMs in our dataset. Instead, we identified codons with multiple differences (CMDs) that likely arose on a single branch of the phylogeny.  We used PAML to reconstruct the ancestral sequence at each node in the phylogeny [@Yang2007]. For the reconstruction, Model 8 was chosen because we specifically re-analyzed genes that showed evidence for positive selection when comparing Model 7 with Model 8.  From the ancestrally reconstructed sequences, we identified any codons in which PAML inferred more than 1 substitution on a single branch.  All identified CMDs were removed from the sequences in which they occurred. For example, if a CMD was identified in an external branch, that codon was replaced with ‘---’ only in the sequence of that species. If a CMD was inferred on an internal branch, the codon was replaced with ‘---’ in all species descended from that internal branch.  For each gene that showed evidence of positive selection using the unedited sequences, we also conducted PAML analyses using sequences from which all CMDs were removed.

###  Polymorphism & Divergence in the Primate Lineage

To further examine evidence for selection on recombination genes, we compared divergence between humans and macaque to polymorphism within humans in 29 recombination genes. Human polymorphism data was downloaded from ExAC database. Polymorphism data was not available for 3 genes (*RNF212, MEI4,* and *REC8*), and thus these genes were not included in this analysis. By comparing counts of non-synonymous and synonymous polymorphisms to counts of non-synonymous and synonymous substitutions using the McDonald-Kreitman test, we can identify either an excess of non-synonymous substitutions, indicative of positive selection, or a paucity of non-synonymous substitutions, indicative of negative selection [**citation**]. Additionally, pairwise divergence between humans and macaques was calculated using yn00 package in PAML [@Yang2007].

### Identifying Evolutionary Patterns

To identify evolutionary patterns among our recombination genes, we compared the rate of evolution and the proportion of genes experiencing positive selection among groups of interest. We asked: (1) Do genes that function in different steps of the pathway exhibit different rates of evolution? (2) Do genes that function post-synapsis evolve more rapidly than genes that function pre-synapsis? and (3) Do genes associated with between-individual variation in recombination rate diverge more rapidly between species? All statistical analyses were performed in R [**citation**].

Evolutionary rate covariation (ERC) metric is the correlation coefficient between branch-specific rates between two proteins [@Clark2012]. ERC is typically elevated among interacting proteins and is assumed to result from: (1) concordance in fluctuating evolutionary pressures, (2) parallel evolution of expression level, or (3) compensatory changes between co-evolving genes [@Clark2012; @Clark2013]. We used a publicly available ERC dataset (https://csb.pitt.edu/erc_analysis/index.php) to compare the median ERC-value among a subset of our focal recombination genes (N = 25) to the genome as a whole, as described in [@Priedigkeit2015].

To control for this general elevation in ERC among recombination genes and test for relationships between specific groups between them, we calculated ERC values for only our focal set of 32 recombination genes. Branch lengths were calculated using aaML package in PAML [@Yang2007] and pairwise ERC values were calculated following the methods of [@Clark2012]. Using this approach, we specifically compared the
211 ERC values among three of the most rapidly evolving recombination genes (*TEX11, SHOC1, and SYCP2*).

\pagebreak

## Results


### Heterogeneity in evolutionary rate among recombination genes

We observed substantial heterogeneity in the rate of evolution of recombination genes, spanning a range of 0.0268 – 0.8483 (mean $\omega$ = 0.3275, SD = 0.1971, median = 0.30945) (Figure 2A, Figure 3, Table 3). Four genes exhibit particularly rapid evolution compared to other recombination genes, having evolutionary rates greater than 1 SD above mean (*SYCP2, TEX11, SHOC1, IHO1*). At the other end of the spectrum, five genes have evolutionary rates more than 1 SD below mean and are highly conserved across the mammalian phylogeny (*BRCC3, HEI10, DMC1, RAD51, RAD50*). In general, there is very high concordance between evolutionary rate across mammals and pairwise divergence between humans and macaques (mean $\omega$ = 0.3301, SD = 0.2370, median = 0.30925) (Figure 2B, Table 4). It should be noted, however, that these two measures are not independent - divergence between human and macaque sequences is incorporated in the phylogenetic analysis. Six genes have evolutionary rates more than 1 SD above mean (*CNTD1, TEX11, SHOC1, IHO1, MEI4, RAD21L*). Likewise, six genes have evolutionary rates more than 1 SD below mean (*HORMAD1, MRE11, RAD50, DMC1, RAD51, MLH1*).

The genes that show the most rapid and most conserved rates of divergence between humans and macaques largely, but not completely, overlaps with the genes showing extreme evolutionary rates across the mammalian phylogeny.There are a few notable outliers that show much more rapid divergence between humans and macaques than across the mammalian phylogeny as a whole. These include MEI4 ($\omega$~mammals~ = 0.4332, $\omega$~human-macaque~ = 0.7252), CNTD1 ($\omega$~mammals~ = 0.2496, $\omega$~human-macaque~ = 0.6803), and HEI10 ($\omega$~mammals~ = 0.1226, $\omega$~human-macaque~ = 0.3235).

### Elevated evolutionary rate among recombination genes

Gradnigo et al. (2016) measured the rate of divergence between human and macaque for 3,606 genes throughout the genome. We used this dataset to ask whether the rate of evolution of recombination genes as a group is different than expected from the genome-wide distribution. We randomly sampling 32 $\omega$ values from this larger dataset and asked how frequently we observed average evolutionary rates as high or higher than observed among our focal set of recombination genes (mean $\omega$ = 0.3301). We found evidence for a significantly elevated evolutionary rate among recombination genes, observing a mean as high (or higher) than the value observed among recombination genes less than 1% of the time (*p* = 0.0075, sample size = 10,000) (Figure 4).

### Evidence of positive selection across the mammalian phylogeny

We identified signatures of positive selection in 10 recombination genes (31.25%) using site models in CODEML. These genes include: *IHO1, MRE11, SYCP1, SYCP2, REC8, RAD21L, RNF212, TEX11, MSH4, SHOC1* (Table 2). For each of these genes, models that include a fraction of sites where the rate of non-synonymous substitutions is estimated to be greater than the rate of synonymous substitutions ($\omega$ > 1, Model 8) had a significantly better fit than models that did not include such a class of sites (Model 7, 8a). Due to the potential for multi-nucleotide mutations to produce erroneous signatures of positive selection, we re-analyzed this subset of genes removing any codons inferred to have accumulated multiple changes on a single branch (CMDs). After removing all CMDs, 1 gene (*TEX11*) retained a significant signature of positive selection (Table 5).

Comparing polymorphism within humans to divergence between humans and macaques revealed a general pattern of negative selection among recombination genes in the primate lineage. A majority of the recombination genes (16 genes, 55.17%) had a significant paucity of non-synonymous substitutions, indicative of negative (purifying) selection (Fisher’s Exact Test, Table 4). None of the genes had a significant excess of non-synonymous substitutions, which would indicate a significant signature of positive selection. Only one gene (*TEX11*) had a positive alpha score ($\alpha$ = 0.2929) and a corresponding neutrality index less than 1 (*NI* = 0.7071), indicating a higher fraction of non-synonymous substitutions than non-synonymous polymorphisms
(Table 4).

### Recombination genes associated with inter-individual differences do not diverge more rapidly between species 

We did not find evidence that recombination genes associated with inter-individual differences in recombination rate evolve more rapidly than other recombination genes. While we observed a higher mean evolutionary rate among genes associated with inter-individual differences ($\omega$ = 0.3943 v. $\omega$ = 0.2925, respectively), the difference was not significant (*p* = 0.2381, Mann-Whitney U Test). Likewise, we observed a greater proportion of genes associated with inter-individual variation exhibited signatures of positive selection (5/11 vs. 5/21, respectively), this difference was also not significant (*p* = 0.210, Chi-Squared Test). The difference in evolutionary rates between these two classes of genes was greater when considering only divergence between humans and macaques ($\omega$ = 0.4181 vs. $\omega$ = 0.2839)(*p* = 0.08816, Mann-Whitney U Test).

### Genes that function post-synapsis are more likely to exhibit signatures of positive selection

We did not find evidence that recombination genes that in different steps of the pathway exhibit different evolutionary rates. This was the case both when comparing the 6 major steps in the recombination pathway (*p* = 0.1422, Kruskal-Wallis Test)(Figure 6) and when comparing more generally between genes that function pre- and post-synapsis ($\omega$ = 0.3762 vs. $\omega$ = 0.2723, respectively)(*p* = 0.1425, Mann-Whitney U Test). Likewise, we didn’t observed significant differences between recombination genes by step in the pathway when comparing just divergence between humans and macaques (*p* = 0.1422, Kruskal-Wallis Test). However, the rate of divergence between humans and macaques of post-synapsis genes was borderline significantly higher when compared to pre-synapsis recombination genes ($\omega$ = 0.3994 v. $\omega$ = 0.2514, respectively)(*p* = 0.05827, Mann-Whitney U Test). Interestingly, we did observe that a significantly higher fraction of post-synapsis recombination genes exhibited signatures of positive selection in comparison with pre-synapsis recombination genes (8/17 v. 2/15, respectively) (*p* = 0.03998, Chi-Squared Test).

### Evolutionary rates among recombination genes are correlated  

Meiotic genes have been shown to exhibit statistically significant, but not strong, ERC among mammals [@Clark2013]. Similarly, we identified significant evidence for correlated evolution among genes in the recombination pathway (mean ERC = 0.134, permutation *p* = 0.000358). After factoring out the general elevation of ERC values among recombination genes, the mean ERC value among our focal set of genes was approximately zero (mean ERC = 0.000358). Among recombination genes, we detected strong signature of correlated evolution between our three genes of interest: *SHOC1, TEX11, SYCP2* (mean ERC = 0.42369, permutation *p* = 0.025). Thus, the coevolutionary pattern among these three genes is statistically stronger than that observed generally among recombination genes.

\pagebreak

## Discussion

\pagebreak

**Table 1** : List of 32 recombination genes surveyed by step in the recombination pathway. Genes in bold have been associated with inter-individual differences in recombination rate in at least one species of mammals.  

**Pathway Step** | **Genes** 
---|---
DSB Formation | *HORMAD1, MEI4, **REC114**, IHO1, SPO11*
DSB Processing | *HORMAD2, MRE11, NBS1, RAD50, BRCC3*
Strand Invasion | *DMC1, RAD51, SPATA22, MEIOB, MCMDC2*
Homologous Pairing | ***REC8**, **RAD21L**, SYCP1, SYCP2, TEX11*
CO vs. NCO Decision | ***TEX11**, SHOC1, **RNF212**, **RNF212B**, **MSH4**, **MSH5***
Resolution | ***MER3**, CNTD1, **HEI10**, MLH1, **MLH3**, MUS81*

\bigbreak

**Table 2**: Six PAML site models used to measure evolutionary rate and test for positive selection.  Models varied in the number of $\omega$ classes, the range of $\omega$ for each of these classes, and whether a class of sites subject to positive selection was included.

**Model** | **# Site Classes** | **$\omega$ Range** | **Pos. Selection?**
---|---|---|---
0 | 1 | <1 | No
1 | 2 | <1, =1 | No
2 | 3 | <1, =1, >1 | Yes
7 | 10 | 0-1 | No
8 | 11 | 0-1, >1 | Yes
8a | 6 | 0-1, =1 | No

\pagebreak

**Figure 1**: Species tree assumed in analyses of molecular evolution.

\bigbreak

![Figure 1](../Figures/Species_Tree.pdf)

\pagebreak

**Figure 2**:Distribution of $\omega$ for 32 recombination genes.  Bar shows the mean +/- 1 standard deviation. (A) Divergence estimated across the mammalian phylogeny. (B) Pairwise divergence between human and macaque.

(A)

![Figure 2A](../Figures/omega_dist.png)

(B)

![Figure 2B](../Figures/div_dist.png)

\pagebreak

**Figure 3**: **Pathway Figure Description** The color of each gene represents its evolutionary rate relative to the average rate of evolution of recombination genes ($\omega$ = 0.3275): more rapidly evolving genes are depicted in darker shades of red and the more conserved genes are depicted in darker shades of blue. Genes that exhibit a signature of positive selection are in bold.

\bigbreak

![Figure 3](../Figures/PATHWAY_fig.pdf)

\pagebreak

**Figure 4**: Distribution of the mean divergence ($\omega$) between human and macaque of 10,000 random draws from the entire genome. Mean $\omega$ among these random draws was observed to be equal to or greater than that observed among recombination genes less than 1% of the time (*p* = 0.0075, 10,000 random draws).

\bigbreak

![Figure 4](../Figures/RandSamp_DivergenceFig.pdf)

\pagebreak

**Figure 5**: High concordance between there rate of evolution of recombination gene between human and macaques and the rate of evolution among mammals. The linear regression is shown in red and the 1:1 line is shown as a dashed line.

\bigbreak

![Figure 5](../Figures/DivVDiv_plot.png)

\pagebreak

**Figure 6**: Boxplot of $\omega$ by step in recombination pathway.

\bigbreak

![Figure 6](../Figures/step_boxplot.png)

\pagebreak

**Table 3**: PAML analysis of 32 recombination genes in mammals [@Yang2007].  

***Gene*** | ***bp*** | ***N*** | ***$\omega$*** | ***M*** | ***M1-M2*** | ***p-value*** | ***M7-M8*** | ***p-value*** | ***M8a-M8*** | ***p-value*** 
---|---|---|---|---|---|---|---|---|---|---
**A)** | | | | | | | | | | | | 
*HORMAD1* | 1212 | 16 | 0.3036 | 7 | 0 | *1.000* | 1.795 | *0.4076* | --- | --- 
*MEI4* | 1170 | 16 | 0.4332 | 7 | 0 | *1.000* | 0.005 | *0.9976* | --- | --- 
*REC114* | 870 | 15 | 0.4003 | 7 | 0 | *1.000* | 5.384 | *0.0677* | --- | --- 
*IHO1* | 1824 | 16 | 0.7095 | **8** | 13.061 | ***0.0015*** | 17.571 | ***0.0002*** | 14.527 | ***0.0001*** 
*SPO11* | 1188 | 15 | 0.1654 | 7 | 0 | *1.000* | 4.648 | *0.0980* | --- | --- |
**B)** | | | | | | | | | | | | 
*HORMAD2* | 981 | 15 | 0.3153 | 7 | 0 | *1.000* | 3.650 | *0.1612* | --- | --- 
*MRE11* | 2136 | 16 | 0.1688 | **8** | 0.363 | *0.8342* | 11.931 | ***0.0026*** | 4.706 | ***0.0301***
*NBS1* | 2289 | 15 | 0.4183 | **8** | 0 | *1.000* | 12.763 | ***0.0017*** | 4.087 |  ***0.0432***
*RAD50* | 3936 | 16 | 0.1006 | 7 | 0 | *1.000* | 0.301 | *0.8605* | --- | ----
*BRCC3* | 954 | 15 | 0.0602 | 7 | 0 | *1.000* | 0.250 | *0.8826* | --- | --- 
**C)** | | | | | | | | | | | | 
*DMC1* | 1020 | 15 | 0.0351 | 1 | 0.488 | *0.7835* | 5.000 | *0.0821* | --- | --- 
*RAD51* | 1017 | 16 | 0.0268 | 7 | 0 | *1.000* | 0 | *1.000* | --- | ---
*SPATA22* | 1101 | 16 | 0.4893 | 7 | 0 | *1.000* | 0.429 | *0.8070* | --- | --- 
*MEIOB* | 1425 | 16 | 0.2341 | 7 | 0 | *1.000* | 0.665 | *0.7172* | --- | ---
*MCMDC2* | 2052 | 16 | 0.2239 | 7 | 0 | *1.000* | 0.628 | *0.7307* | --- | ---
**D)** | | | | | | | | | | | | 
*REC8* | 1833 | 16 | 0.3698 | **8** | 0 | *1.000* | 14.690 | ***0.0006*** | 5.927 | ***0.0149*** |  
*RAD21L* | 1686 | 15 | 0.503 | **8** | 12.124 | ***0.0023*** | 32.050 | ***>0.0001*** | 12.049 | ***0.0005*** | 
*SYCP1* | 3015 | 16 | 0.4337 | **8** | 8.711 | ***0.0128*** | 26.860 | ***>0.0001*** | 9.243 | ***0.0024*** | 
*SYCP2* | 4650 | 16 | 0.5572 | **8**| 11.584 | ***0.0031*** | 37.200 | ***>0.0001*** | 15.838  | ***0.0001*** |  
*TEX12* | 369 | 14 | 0.2297 | 7 | 0.0565 | *0.9721* | 1.549 | *0.4610* | --- | ---
**E)** | | | | | | | | | | | | 
*TEX11* | 2844 | 15 | 0.8483 | **8** | 60.872 | ***>0.0001***  | 82.665 | ***>0.0001***  | 61.141 | ***>0.0001***  | 
*SHOC1* | 4644 | 16 | 0.6113 | **8** | 12.447 | ***0.0020*** | 30.561 | ***>0.0001*** | 15.645 | ***0.0001*** |
*RNF212* | 948 | 16  | 0.5014 | **8** | 0 | *1.000* | 16.366 | ***0.0003*** | 5.202 | ***0.0226*** |
*RNF212B* | 906 | 14 | 0.4066 | 7 | 0 | *1.000* | 0.500 | *0.7788* | --- | ---
*MSH4* | 2814 | 16 | 0.2132 | **8** | 16.608 | ***0.0002*** | 39.447 | ***>0.0001*** | 23.238 | ***>0.0001*** | 
*MSH5* | 2565 | 15 | 0.1642 | 7 | 0 | *1.000* | 4.214 | *0.1216* | --- | ---
**F)** | | | | | | | | | | | |
*MER3* | 4458 | 16 | 0.3633 | 8a | 0 | *1.000* | 12.838 | ***0.0016*** | 3.109 | *0.0779* | 
*CNTD1* | 1026 | 15 | 0.2496 | 7 | 0 | *1.000* | 0.936 | *0.6263* | --- | ---  
*HEI10* | 831 | 15 | 0.1226 | 7 | 0 | *1.000* | 0.250 | *0.8826* | --- | ---
*MLH1* | 2313 | 15 | 0.1652 | 8a | 0 | *1.000* | 12.221 | ***0.0022*** | 0.280 | *0.5970* | 
*MLH3* | 4419 | 16 | 0.4444 | 7 | 0 | *1.000* | 3.757 | *0.1528* | --- | ---
*MUS81* | 1665 | 16 | 0.2124 | 7 | 0 | *1.000* | 0.628 | *0.7304* | --- | ---

\pagebreak

**Table 5**: Polymorphism & Divergence Data

***Gene*** | ***$\omega$*** | ***Pn*** | ***Ps*** | ***Pn/Ps*** | ***Dn*** | ***Ds*** | ***Dn/Ds*** | ***MK Test*** | ***$\alpha$*** | ***NI*** |  |
---|---|---|---|---|---|---|---|---|---|---|---|
**A)** | | | | | | | | | |
*HORMAD1* | 0.0901 | 84 | 35 | 2.4000 | 5 | 12 | 0.4167 | ***0.0018*** | -4.7600 | 5.7600 | Neg. 
*MEI4* | 0.7252 | 15 | 7 | 2.1429 | 24 | 9 | 2.6667 | *0.7679* | 0.1964 | 0.8036 | ---
*REC114* | 0.3239 | 76 | 37 | 2.0541 | 11 | 14 | 0.7857 | ***0.0392*** | -1.6143 | 2.6143 | Neg.
*IHO1* | 0.6608 | 130 | 64 | 2.0313 | 36 | 19 | 1.8947 | *0.8718* | -0.0720 | 1.0720 | ---
*SPO11* | 0.1434 | 118 | 52 | 2.2692 | 11 | 22 | 0.5000 | ***0.0001*** | -3.5385 | 4.5385 | Neg.
**B)** | | | | | | | | | |
*HORMAD2* | 0.295 | 80 | 31 | 2.5806 | 7 | 9 | 0.7778 | ***0.0404*** | -2.3180 | 3.3180 | Neg. 
*MRE11* | 0.0392 | 211 | 86 | 2.4535 | 5 | 35 | 0.1429 | ***>0.0001*** | -16.1744 | 17.1744 | Neg.
*NBS1* | 0.4155 | 221 | 93 | 2.3763 | 34 | 25 | 1.3600 | *0.0666* | -0.7473 | 1.7473 | ---
*RAD50* | 0.0714 | 303 | 118 | 2.5678 | 8 | 43 | 0.1860 | ***>0.0001*** | -12.8019 | 13.8019 | Neg.
*BRCC3* | 0.0979 | 13 | 21 | 0.6190 | 2 | 6 | 0.3333 | 0.6888 | -0.8571 | 1.8571 | ---
**C)** | | | | | | | | | |
*DMC1* | 0.000 | 72 | 42 | 1.7143 | 0 | 11 | 0.0000 | ***>0.0001*** | --- | --- | Neg.
*RAD51* | 0.000 | 50 | 48 | 1.0417 | 0 | 13 | 0.0000 | ***>0.0001*** | --- | --- | Neg.
*SPATA22* | 0.4523 | 114 | 45 | 2.5333 | 21 | 10 | 2.1000 | *0.6700* | -0.2063 | 1.2063 | ---
*MEIOB* | 0.2462 | 91 | 40 | 2.2750 | 20 | 22 | 0.9091 | ***0.0200*** | -1.5025 | 2.5025 | Neg. 
*MCMDC2* | 0.2108 | 165 | 54 | 3.0556 | 16 | 26 | 0.6154 | ***>0.0001*** | -3.9653 | 4.9653 | Neg.
**D)** | | | | | | | | | |
*REC8* | 0.477 | 147 | 76 | 1.9342 | 38 | 31 | 1.2258 | *0.1164* | -0.5779 | 1.5779 | ---
*RAD21L* | 0.6334 | 51 | 17 | 3.000 | 27 | 13 | 2.0769 | *0.5051* | -0.4444 | 1.4444 | ---
*SYCP1* | 0.3676 | 213 | 100 | 2.1300 | 33 | 37 | 1.2222 | *0.0546* | -0.7427 | 1.7427 | ---
*SYCP2* | 0.3676 | 429 | 154 | 2.8506 | 74 | 53 | 1.3962 | ***0.0005*** | -1.0417 | 2.0417 | Neg.
*TEX12* | 0.1349 | 31 | 16 | 1.9375 | 2 | 4 | 0.5000 | 0.1836 | -2.875 | 3.875 | ---
**E)** | | | | | | | | | |
*TEX11* | 0.9068 | 126 | 81 | 1.5556 | 55 | 25 | 2.200 | *0.2234* | 0.2929 | 0.7071 | ---
*SHOC1* | 0.7225 | 368 | 124 | 2.9677 | 85 | 37 | 2.2973 | *0.2521* | -0.2918 | 1.2918 | ---
*RNF212* | 0.387 | --- | --- | --- | 17 | 18 | 0.9444 | --- | --- | --- | ---
*RNF212B* | 0.2566 | 368 | 124 | 2.9677 | 8 | 12 | 0.6667 | ***0.0013*** | -3.4516 | 4.4516 | Neg.
*MSH4* | 0.2635 | 260 | 94 | 2.7660 | 24 | 29 | 0.8276 | ***>0.0001*** | -2.3422 | 3.3422 | Neg.
*MSH5* | 0.2106 | 197 | 104 | 1.8942 | 19 | 33 | 0.5758 | ***0.0002*** | -2.2900 | 3.2900 | Neg.
**F)** | | | | | | | | | |
*MER3* | 0.3247 | 402 | 143 | 2.8112 | 54 | 44 | 1.2273 | ***0.0004*** | -1.2906 | 2.2906 | Neg.
*CNTD1* | 0.6803 | 81 | 47 | 1.7234 | 13 | 8 | 1.6250 | *1.0000* | -0.0606 | 1.0606 | ---
*HEI10* | 0.3235 | 73 | 33 | 2.2121 | 4 | 5 | 0.8000 | *0.1541* | -1.7652 | 2.7652 | ---
*MLH1* | 0.0924 | 255 | 90 | 2.8333 | 9 | 29 | 0.3103 | ***>0.0001*** | -8.1296 | 9.1296 | Neg.
*MLH3* | 0.4919 | 437 | 167 | 2.6168 | 77 | 57 | 1.3509 | ***0.0012*** | -0.9370869 | 1.937087 | Neg.
*MUS81* | 0.1299 | 208 | 81 | 2.5679 | 17 | 40 | 0.4250 | ***>0.0001*** | -5.0421 | 6.0421 | Neg.

\pagebreak

**Table 4**: PAML - MNM Analysis

***Gene*** | ***bp*** | ***N*** | ***$\omega$*** | ***M*** | ***M1-M2*** | ***p-value*** | ***M7-M8*** | ***p-value*** | ***M8a-M8*** | ***p-value*** 
---|---|---|---|---|---|---|---|---|---|---
*IHO1* | 1824 | 16 | 0.6104 | 7 | 0 | *1.000* | 0.258 | *0.8789* | --- | ---
*MRE11* | 2136 | 16 | 0.1330 | 7 | 0.226 | *0.8930* | 3.056 | *0.2169* | --- | ---
*NBS1* | 2289 | 15 | 0.3413 | 7 | 0 | *1.000* | 1.956 | *0.3761* | --- | ---
*REC8* | 1833 | 16 | 0.2905 | 7 | 0 | *1.000* | 5.321 | *0.0699* | --- | --- 
*RAD21L* | 1686 | 15 | 0.4271 | 8a | 2.329 | *0.3121* | 9.497 | ***0.0087*** | 1.620 | *0.2031* 
*SYCP1* | 3015 | 16 | 0.3731 | 8a | 3.328 | *0.1893* | 13.440 | ***0.0012*** | 2.122 | *0.1452* 
*SYCP2* | 4650 | 16 | 0.4752 | 7 | 0 | *1.000* | 1.758 | *0.4151* | --- | ---  
*TEX11* | 2844 | 15 | 0.7287 | **8** | 9.989 | ***0.0068***  | 18.776 | ***0.0001***  | 10.656 | ***0.0011*** | 
*SHOC1* | 4644 | 16 | 0.5519 | 8a | 0 | *1.000* | 7.439 | ***0.0242*** | 0.292| *0.5887* |
*RNF212* | 948 | 16  | 0.3685 | 7 | 0 | *1.000* | 0 | *1.000* | --- | --- 
*MSH4* | 2814 | 16 | 0.1509 | 7 |  0 | *1.000* | 2.079 | *0.3536* | --- | ---  

\pagebreak

## Acknowledgements 

A.L.D. was supported by NHGRI Training Grant to the Genomic Sciences Training Program
5T32HG002760. B.A.P. was supported by NIH grant R01 GM100426A and NSF grant DEB
1353737.

## References


