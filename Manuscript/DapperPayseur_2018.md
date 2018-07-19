---
date: \today{}
geometry: margin=1in
header-includes:
    - \usepackage{setspace}
    - \doublespacing
    - \usepackage{lineno}
    - \linenumbers
---


**Rapid and Adaptive Evolution of the Recombination Pathway in Mammals**

*Article*

$~$

Amy L. Dapper\* and Bret A. Payseur

$~$

Laboratory of Genetics, University of Wisconsin, Madison, WI 53706, USA

\*Corresponding Author : dapper@wisc.edu

\pagebreak

## Abstract

Meiotic recombination, the exchange of genetic material between homologous chromosomes during meiosis, is required for successful gametogenesis in most sexually reproducing species. Recombination is also a fundamental evolutionary force, influencing the fate of new mutations and determining the genomic scale over which selection shapes genetic variation. Despite the central importance of recombination, basic questions about its evolution have yet to be addressed.  Although many genes that play roles in recombination have been identified, the molecular evolution of most of these genes remains uncharacterized.  Using a phylogenetic comparative approach, we measure rates of evolution in 32 recombination pathway genes across 16 mammalian species, spanning primates, murids, and laurasithians.  By analyzing a carefully-selected panel of genes involved in key components of recombination – spanning double strand break formation, strand invasion, the crossover/non-crossover decision, and resolution – we generate a comprehensive picture of the evolution of the recombination pathway in mammals. Recombination genes exhibit marked heterogeneity in the rate of protein evolution, both across and within genes.  We report signatures of rapid evolution and positive selection that could underlie species differences in recombination rate.   

\pagebreak

## Introduction


## Results

\pagebreak

**Table 1**: Sequence divergence between Human (*Homo sapiens*) and Rhesus Macaque (*Macaca mulatta*) [@yang2000,@yang2007].  Steps: A - double strand break (DSB) formation, B - DSB processing & Strand Invasion, C - Homologous Pairing, D1 - crossover (CO) vs. non-crossover (NCO) step1 - MutS, D2 - CO vs. NCO step 2 - MutL.

***Gene*** | ***bp*** | ***$\omega$*** | ***S*** | ***N*** | ***t*** | ***$\kappa$*** | ***dN*** | ***dS*** | 
---|---|---|---|---|---|---|---|---|---|
**A)** | | | | | | | | | |
*SPO11* | XXX | A | 0.1434 | 291.2 | 896.8 | 0.0872 | 2.5317 | 0.0118 +/- 0.0036 | 0.0823 +/- 0.0178 |
*MEI4* | XXX | A | 0.7252 | 331 | 824 | 0.0822 | 4.6295 | 0.0247 +/- 0.0056 | 0.0341 +/- 0.0104 | 
*REC114* | XXX | A | 0.3239 | 237.2 | 557.8 | 0.0974 | 2.9455 | 0.0200 +/- 0.0061 | 0.0618 +/- 0.0168 |

\pagebreak

**Table 2**: PAML analysis of 32 recombination genes in mammals [@yang2007].  

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

## Acknowledgements 

A.L.D. was supported by NHGRI Training Grant to the Genomic Sciences Training Program
5T32HG002760. B.A.P. was supported by NIH grant R01 GM100426A and NSF grant DEB
1353737.

## References


