# SPO11

Chicken - XM_015296537.1
Beginning of CDS is different in Ensembl and NCBI.  Low coverage overall, but some support for NCBI while no support for Ensembl.
*In either case, the first exon sequence does not align with mammalian sequences at all.*  Removed for analysis by hand.

Platypus - ENSOANT00000014736.2 OR XM_007671414.1
Both NCBI & Ensembl versions are the same.  12-bp deletion in the first exon.

Opossum - ENSMODT00000030715.2 OR XM_001377908.3
Both NCBI & Ensembl versions are the same.  9-bp deletion in the first exon.  *Deletions in Opossum & Platypus overlap.*

Cow - ENSBTAT00000061470.2 OR NM_001193090.1
Both NCBI & Ensembl versions are the same.

Sheep - ENSOART00000019594.1
NCBI version X1 & X2 (missing 2nd exon) predict extra exon at start of the transcript.  The preferred Ensembl transcript misses the end codon *TAA* - added by hand.

Pig - XM_005673040.2
Ensembl transcript lacks 2nd exon.

Bat - XM_008141201.1
Other NCBI transcript lacks 2nd exon.

Horse - ENSECAT00000013756.1 OR XM_001489926.2
Both NCBI & Ensembl versions are the same.

Dog - ENSCAFT00000019104.3 OR XM_848394.4
Both NCBI & Ensembl versions are the same - with the exception that the Ensembl version lacks the end codon *TAA*

Mouse - ENSMUST00000050442.14 OR NM_012046.2
Both NCBI & Ensembl versions are the same. Alternate transcripts lack the 2nd exon.

Rat - XM_006235698.3
End of ensembl transcript does not align.

Tree Shrew - XM_006141881.1
The 12-bp deletion at the very begginning is consistent with the reference sequence - first start codon lost.

Marmoset - ENSCJAT00000037574.2 OR XM_002747707.3
Both NCBI & Ensembl versions are the same.

Macaque - XM_001088572.3
Not annotated in Ensembl (maybe see RAE1).

Orangutan - XM_009233747.1
NCBI transcript annotation incorrect due to gap in reference genome.  Misses one exon and creates an incorrect one in its place.  Edited by hand.  Same problem with the Ensembl transcript.

Gorilla - XM_004062412.2
(also see ENSGGOT00000008888.3)

Human - NM_012444.2
(also see ENST00000371263.7)

Chimp - ENSPTRT00000025448 OR XM_514741.4
Both NCBI & Ensembl versions are the same.

Bonobo - XM_003806159.2
(also see ENSPPAT00000048855.1)

# IHO1/CCDC36 

Chicken - XM_004944621.2

Platypus - Not Annotated.

Opossum - XM_016424383.1
(See also ENSMODT00000016571.3)

Cow - ENSBTAT00000012334.5 OR NM_001205523.2
Both NCBI & Ensembl versions are the same.

Sheep - ENSOART00000015544.1 OR XM_012100069.2 
Both NCBI & Ensembl versions are the same.

Pig - XM_005669538.3
NCBI transcript fills in gaps present in the Ensembl transcript

Bat - XM_008157561.1

Horse - XM_001494366.5
Ensembl transcript missing very start of transcript.

Dog - ENSCAFT00000044029 OR XM_003432877.4
Both NCBI & Ensembl versions are the same.

Mouse - ENSMUST00000076592.3 OR  NM_001135198.1 
Both NCBI & Ensembl versions are the same.

Rat - ENSRNOT00000071189 OR XM_001055346.6
Both NCBI & Ensembl versions are the same.

Tree Shrew - XM_006170965.1

Marmoset - ENSCJAT00000007206 OR XM_008981624.2
Both NCBI & Ensembl versions are the same.

Macaque - XM_002802780.2
No Ensembl Annotation

Orangutan - XM_002813755.2 
Ensembl transcript missing very start of transcript.

Gorilla - ENSGGOT00000064151.1 OR XM_019023203.1
Both NCBI & Ensembl versions are the same.

Human - ENST00000296449 OR NM_178173.3
Both NCBI & Ensembl versions are the same.

Chimpanzee - ENSPTRT00000065561 OR XM_001162713.4
Both NCBI & Ensembl versions are the same.

Bonobo - Hybrid XM_008971826.1 & ENSPPAT00000060897.1
Poorly assembled reference genome - both transcripts have errors.  Ensembl transcript misses the start and the NCBI transcript has some junk in the middle of a missing exon.
Using a hybrid for analysis.

## HORMAD1

Chicken - Edited version of ENSGALT00000055524.2 (gal_gal_HORMAD1)
Not in the current NCBI Annotation.  Ensembl version missing two exons and contained one exon with extra basepairs.

Platypus - XM_007659811.1
Three HORMAD1 transcripts annotated in the NCBI database on an unplaced scaffold - however, they align very poorly with the other species HORMAD1 sequence, much worse than chicken.  Including the best supported transcript for completeness, may need to remove.

Opossum - XM_016429151.1 OR ENSMODT00000023872.3
Both NCBI & Ensembl versions are the same.

Cow - NM_001046305.2 OR ENSBTAT00000003529.4
Both NCBI & Ensembl versions are the same.

Sheep - XM_012180626.2 OR ENSOART00000022714.1
Both NCBI & Ensembl versions are the same.

Pig - NM_001194981.1 OR ENSSSCT00000007285.3
Both NCBI & Ensembl versions are the same.

Bat - XM_008155836.1
A suspicious lack of mapping around 5th exon - but no gaps in that part of the reference genome.  Leaving as is for now because alignment matches other species well in that area.

Horse - XM_014739928.1 (OR ENSECAT00000012333.1)
A small number of sequence differences between the two - NCBI transcript is more similar than the ensembl transcript, so I am using that one.

Dog - XM_003639633.4 OR ENSCAFT00000019166.3
Both NCBI & Ensembl versions are the same.

Mouse - NM_001289532.1 OR ENSMUST00000029754.12
Both NCBI & Ensembl versions are the same.

Rat - NM_001108949.1 OR ENSRNOT00000066821.1
Both NCBI & Ensembl versions are the same.

Tree Shrew - XM_006172205.1
The insertion at the end of the gene is supported by expression data.  Looks like a small duplication with accumulated mutations.

Marmoset - XM_008984285.2 OR ENSCJAT00000056776.1
Both NCBI & Ensembl versions are the same.

Macaque - XM_015151704.1 OR ENSMMUT00000073393.1
Both NCBI & Ensembl versions are the same.

Orangutan - XM_002810265.3 OR ENSPPYT00000001075.1
Both NCBI & Ensembl versions are the same.

Gorilla - XM_019021785.1 OR ENSGGOT00000049434.1
Both NCBI & Ensembl versions are the same.

Human - NM_032132.4 OR ENST00000361824.6
Both NCBI & Ensembl versions are the same.

Chimpanzee - XM_016926530.1 (OR ENSPTRT00000045262.4)
NCBI version is better quality - do not use Ensembl transcript (NNN and missing stop).

Bonobo - XM_003817290.3 OR ENSPPAT00000007841.1
Both NCBI & Ensembl versions are the same.

## DMC1

Chicken - XM_004937733.2
Ensembl transcript missing exon (ENSGALT00000019979.5).

Platypus - orn_ana_DMC1
(XM_007656122.2 OR ENSOANT00000016753.1)
Poor assembly in both databases - Ensembl transcript is worse.  Both likely making up exon to fill an gap in the assembly.  Small editing in NCBI transcript to get rid of errors caused by this.

Opossum - XM_016425704.1 OR ENSMODT00000012291.2
Both NCBI & Ensembl versions are the same.

Cow - NM_001191338.1 (OR ENSBTAT00000007794.4)
Ensembl transcript missing one codon.

Sheep - XM_012175647.2 (OR ENSOART00000016963.1)
NCBI transcript is more parsimonius (a few AA differences in Ensembl transcript)

Pig - XM_005655492.2 OR ENSSSCT00000000109.3
Both NCBI & Ensembl versions are the same.

Bat - XM_008144619.1

Horse - XM_005606637.2 (OR ENSECAT00000021148.1)
Ensembl transcript has two extra codons at start.

Dog - XM_005625879.2 (OR  ENSCAFT00000002150.2)
Ensembl transcript missing stop codon.

Mouse - NM_010059.3 OR ENSMUST00000023065.6
Both NCBI & Ensembl versions are the same.

Rat - NM_001130567.1 OR ENSRNOT00000018526.5
Both NCBI & Ensembl versions are the same.

Tree Shrew - XM_006155359.2

Marmoset - XM_017963708.1 OR ENSCJAT00000022883.2
Both NCBI & Ensembl versions are the same.

Macaque - XM_001094012.3 OR ENSMMUT00000067790.1
Both NCBI & Ensembl versions are the same.

Orangutan - ENSPPYT00000013725.1
Poorly annotated in NCBI - split into two transcripts LOC100449963 & LOC100449611

Gorilla - XM_019017941.1 OR ENSGGOT00000011258.3
Both NCBI & Ensembl versions are the same.

Human - NM_007068.3 OR ENST00000216024.6
Both NCBI & Ensembl versions are the same.

Chimpanzee - XM_009438401.2 (OR ENSPTRT00000026857)
Sequences differences - NCBI version is more conservative.

Bonobo - XM_003821593.1 OR ENSPPAT00000056603.1
Both NCBI & Ensembl versions are the same.

## RNF212

Chicken - XM_015286023.1 OR ENSGALT00000051631.2
Both NCBI & Ensembl versions are the same.

Platypus - XM_007671892.1
Evidence for additional exon expression - but, doesn't appear to be relevant.

Opossum - XM_007496872.2 OR ENSMODT00000043005.1
Both NCBI & Ensembl versions are the same.

Cow - XM_005208286.2
End matches expression data - very limited expression coverage at start of gene, but aligns well.

Sheep - XM_015090635.1
(*)  Wild sheep, not domesticated sheep.

Pig - sus_scr_RNF212
Starting point: XM_021100860.1
No expression data mapping to end of transcript & very poor alignment of end of predicted transcript. Removed.

Bat - XM_019712467.1
(*) Rhinolophus sinicus
NW_007370714.1

Horse - cab_equ_RNF212
Starting point: XM_014738575.1
First exon is an error due to a gap in the assembly (removed).  Expression data supports different ending - hand edited.

Dog - XM_005618673.2 OR ENSCAFT00000047401.1
Both NCBI & Ensembl versions are the same.

Mouse - ENSMUST00000212212.1 (OR XM_006535331.3)
Ensembl transcript more parsimonius with rat - NCBI transcript has a few extra codons at the end.

Rat - XM_003751319.4 OR ENSRNOG00000059010
Both NCBI & Ensembl versions are the same.

Tree Shrew - tup_chi_RNF212
first section of transcript missing due to poor assembly.  edited by hand to include additional exons supported by expression data.
Starting point: XM_006143860.1

Marmoset - cal_jac_RNF212
none of the transcripts match the expression data - edited by hand using expression data - excellent alignment with other primate transcripts
one gap in middle of gene due to poor assembly of reference. Starting point: ENSCJAT00000003406.2.

Macaque - mac_mul_RNF212
ENSMMUG00000015507 - no expression support for final exon in transcript - replaced with exons supported by expression data.

Orangutan - pon_pyg_RNF212
XM_002814497.2 OR ENSPPYT00000016879.1
No expression support for this transcript.  Deleted unsupported final exon. Support for three more exons at end of transcript - added to edited transcript.

Gorilla - XM_019026074.1
Originial NCBI transcript lacked start of gene.  Ensembl transcript does not match.

Human - XM_005272274.2

Chimpanzee - XM_016952718.1
None of the Ensembl transcripts match.

Bonobo - XM_003811293.2
None of the Ensembl transcripts match.

## HEI10/CCNB1IP1

Chicken - Not found.

Platypus - XM_007656776.1 OR ENSOANT00000001629.2
Both NCBI & Ensembl versions are the same.

Opossum - XM_001368551.4 OR ENSMODT00000009137.2
Both NCBI & Ensembl versions are the same.

Cow - NM_001046565.1 OR ENSBTAT00000011140.3
Both NCBI & Ensembl versions are the same.

Sheep - XM_012181091.1 OR ENSOART00000021540.1
Both NCBI & Ensembl versions are the same.

Pig - ENSSSCT00000002398.2

Bat - XM_008160495.1

Horse - XM_001502548.4 (OR ENSECAT00000022582.1)
Ensembl version has extra at start - similar to orangutan.

Dog - ENSCAFT00000008662.3 (OR  XM_014119730.2)
NCBI version has extra at start - similar to orangutan.

Mouse - NM_001111119.1 OR ENSMUST00000095932.3
Both NCBI & Ensembl versions are the same.

Rat - ENSRNOT00000082139.1 (OR XM_008770565.2)
NCBI version has extra at start - similar to orangutan.

Tree Shrew - XM_006163065.1

Marmoset - XM_009005649.2 OR ENSCJAT00000019348.1
Both NCBI & Ensembl versions are the same.

Macaque - XM_015143199.1 OR ENSMMUT00000022831.3
Both NCBI & Ensembl versions are the same.

Orangutan -
XM_002824502.3 OR ENSPPYT00000006583.2
Both NCBI & Ensembl versions are the same.
Extra codons at start, not clear if real, but do not match any other sequence so removed for analysis.

Gorilla - XM_019009992.1 OR ENSGGOT00000057568.1
Both NCBI & Ensembl versions are the same.

Human - NM_182852.3 OR ENST00000437553.6
Both NCBI & Ensembl versions are the same.

Chimpanzee - XM_001142928.4 OR ENSPTRT00000044936.5
Both NCBI & Ensembl versions are the same.

Bonobo - XM_003811719.2 OR ENSPPAT00000040567.1
Both NCBI & Ensembl versions are the same.

## CNTD1

Chicken - gal_gal_CNTD1
XM_015299628.1 OR ENSGALT00000058299.2
Neither transcript is great.  Most parsimonius is a hybrid with first few codons from NCBI and the rest from Ensembl transcript.

Platypus - XM_001514450.3
Beginning exons missing due to poor assembly.  Otherwise supported by expression data.
May need to check again.

Opossum - XM_003340238.3 (OR ENSMODT00000035072.1)
Ensembl transcript has extra stuff at start.

Cow - XM_003587448.4 (OR ENSBTAT00000026529.5)
Ensembl version no good at begginning or end.

Sheep - XM_004012946.3

Pig - sus_scr_CNTD1
ENSSSCT00000060076.1
extra codons at start - removed cause lack information regardless if they are real or not.
NCBI transcript no good (XM_021066977.1)

Bat - XM_008149331.1

Horse - XM_003362549.3 OR ENSECAT00000028826.1
Both NCBI & Ensembl versions are the same.

Dog - can_fam_CNTD1
XM_548081.5
extra codons at start - removed cause lack information regardless if they are real or not.

Mouse - mus_mus_CNTD1
NM_026562.2 OR ENSMUST00000103107.4
Both NCBI & Ensembl versions are the same.
Two extra codons at start - removed cause lack information regardless if they are real or not.

Rat - NM_001197217.1 OR ENSRNOT00000076865.1
Both NCBI & Ensembl versions are the same.

Tree Shrew - XM_006156068.2

Marmoset - XM_003732911.3 OR ENSCJAT00000025617.2
Both NCBI & Ensembl versions are the same.

Macaque - XM_015119796.1 OR ENSMMUT00000017730.3
Both NCBI & Ensembl versions are the same.

Orangutan - ENSPPYT00000009794.1 (OR XM_002827497.2)
NCBI version missing end of gene.

Gorilla - XM_019026928.1 OR ENSGGOT00000032919.2
Both NCBI & Ensembl versions are the same.
First exon appears to be missing.

Human - NM_173478.2 OR ENST00000588408.5
Both NCBI & Ensembl versions are the same.

Chimpanzee - XM_009432131.2 (OR ENSPTRT00000016962.4)
NCBI version is more parsimonious - differ in a one codon deletion in the middle of the gene.

Bonobo - XM_003813917.3 (OR ENSPPAT00000044595.1)
Ensembl transcript missing a few codons at start.

## HFM1/MER3
** May want to remove segment of sequence with only two species data.

Chicken - gal_gal_HFM1
Beginning of the gene matches Ensembl transcript, end matches NCBI transcript.  Hybrid.
XM_015290640.1 and ENSGALT00000009827.5

Platypus - NA
Not enough information to reconstruct meaningful segments.
XM_007672879.1

Opossum - ENSMODT00000039127.2
missing start of gene - IGV error so unable to visualize.

Cow - NM_001205576.2 OR ENSBTAT00000027789.5
Both NCBI & Ensembl versions are the same. (extra codon ensembl - but no effect on alignment)

Sheep - ENSOART00000017229.1 (OR XM_015092107.1)
NCBI version missing end.

Pig -  XM_013997383.2 OR ENSSSCT00000007570.3
Both NCBI & Ensembl versions are the same.

Bat - XM_008154712.1

Horse - ENSECAT00000026025.1 (OR XM_014740023.1)
NCBI version has extra sequence.

Dog - ENSCAFT00000032148.2  (OR XM_005621938.2)
NCBI has extra sequence near end of gene.

Mouse - NM_177873.3 OR ENSMUST00000112690.9
Both NCBI & Ensembl versions are the same.

Rat - NM_001191101.1 OR ENSRNOT00000033794.5
Both NCBI & Ensembl versions are the same.

Tree Shrew - XM_006140160.1
the two NCBI transcripts only differ at two codons - unclear which is best, originially picked the other

Marmoset - XM_017974927.1 OR  ENSCJAT00000063585.1
Both NCBI & Ensembl versions are the same.

Macaque - XM_015144699.1 OR ENSMMUT00000009536.3
Both NCBI & Ensembl versions are the same.

Orangutan - XM_002810615.3 (OR ENSPPYT00000001392.1)
Two codons differ - absence of info - equivalent.

Gorilla - XM_019038158.1 OR ENSGGOT00000067567.1
Both NCBI & Ensembl versions are the same.

Human - NM_001017975.4 OR ENST00000370425.7
Both NCBI & Ensembl versions are the same.

Chimpanzee - ENSPTRT00000065671.3 (OR XM_524618.6)
One codon difference - Ensembl more parsimonius.

Bonobo - XM_003808406.2 (OR ENSPPAT00000027114.1)
Ensembl transcript truncated.

## REC114

Chicken - ENSGALT00000086157.1

Platypus - orn_ana_REC114
Starting point: XM_007668342.2 OR ENSOANT00000001610.2
Neither transcript a good match - poor assembly in this region - consider excluding.
Chose high confidence regions well supported by expression data and decent alignment.

Opossum - XM_007478123.1 OR ENSMODT00000012575.3
Both NCBI & Ensembl versions are the same.

Cow - XM_002690533.5

Sheep - XM_015096854.1 (OR ENSOART00000020700.1)
Ensembl version missing start of transcript.

Pig - XM_001928745.5 OR ENSSSCT00000037005.1
Both NCBI & Ensembl versions are the same.

Bat - XM_008160866.1
Assembly very bad in this region. First exon missing.

Horse - equ_cab_REC114
XM_001494312.3
First exon incorrect, actually first exon probably falls in assembly gap.

Dog - XM_003433938.4
Other transcripts very poorly align at begginning or end.
Multiple isoforms supported - but this appears to be the major one.

Mouse - NM_028598.1 OR ENSMUST00000098674.5
Both NCBI & Ensembl versions are the same.

Rat - NM_001106825.1 OR ENSRNOT00000012381.5
Both NCBI & Ensembl versions are the same.

Tree Shrew - XM_006167279.1
Not a great assembly in this region.

Marmoset - XM_002753337.3 (OR ENSCJAT00000035106.2)
Sequence not identical.

Macaque - XM_015142681.1 OR ENSMMUT00000013787.3
Both isoforms are supported equally with expression data (Alt: XM_001093604.3). Keeping most inclusive for now.

Orangutan - XM_002825645.3 (OR ENSPPYT00000007818.1)
Ensembl transcript has two extra codons at start.

Gorilla - XM_004056457.2 OR ENSGGOT00000000745.3
Both NCBI & Ensembl versions are the same.

Human - NM_001042367.1 OR ENST00000331090.10
Both NCBI & Ensembl versions are the same.

Chimpanzee - XM_001175167.5 OR ENSPTRT00000076905.1
Both NCBI & Ensembl versions are the same.

Bonobo - XM_003818569.3 OR ENSPPAT00000004460.1
Both NCBI & Ensembl versions are the same.

## MEI4

Chicken - NA
expression data does not match very well at all - also very low coverage - don't include
ENSGALT00000081702.1

Platypus - NA
expression data does not match very well at all - also very low coverage - don't include
XM_007670758.1

Opossum - XM_007484232.2 (OR ENSMODT00000023450.2)
Mostly the same, Ensembl version has some extra codons at start.

Cow - XM_015472775.1

Sheep - XM_012182419.2 (OR ENSOART00000007365.1)
Same with exception that Ensembl transcript has a few extra codons at start.

Pig - XM_021092258.1 OR ENSSSCT00000059409.1
Both NCBI & Ensembl versions are the same.

Bat - ept_fus_MEI4
XM_008139546.1
No coverage at start of transcript (low overall), so I removed the begginning section with poor alignment.

Horse - XM_014733869.1

Dog - XM_005627549.3 OR ENSCAFT00000004445.3
Both NCBI & Ensembl versions are the same.

Mouse - NM_175213.4 OR ENSMUST00000057067.9
Both NCBI & Ensembl versions are the same.

Rat - NM_001109378.1 OR ENSRNOT00000037530.4
Both NCBI & Ensembl versions are the same.

Tree Shrew - XM_006143412.2
Begginning of transcript supported by expression.

Marmoset - XM_017971222.1

Macaque - XM_015136811.1 OR ENSMMUT00000007496.3
Both NCBI & Ensembl versions are the same.

Orangutan - XM_002817080.3 (OR ENSPPYT00000019533.1)
Versions differ - Ensembl less parsimonius and incomplete end.

Gorilla - XM_019028929.1 OR ENSGGOT00000051461.1
Both NCBI & Ensembl versions are the same.

Human - NM_001322247.1 OR ENST00000602452.2
Both NCBI & Ensembl versions are the same.

Chimpanzee - XM_016955885.1 OR ENSPTRT00000092340.1
Both NCBI & Ensembl versions are the same.

Bonobo - XM_008975281.1 OR ENSPPAT00000020304.1
Both NCBI & Ensembl versions are the same.

## REC8

Chicken - NA

Platypus - NA

Opossum - XM_007479866.2

Cow - NM_001191288.1 OR ENSBTAT00000003504.5
Both NCBI & Ensembl versions are the same.

Sheep - ENSOART00000020906.1 (OR XM_012180931.2)
NCBI transcript has extra codons.

Pig - XM_005666240.3 OR ENSSSCT00000002239.3
Both NCBI & Ensembl versions are the same.

Bat - ept_fus_REC8
XM_008158552.1
Edited out extra codons not supported by expression data.

Horse - XM_014733672.1 (OR ENSECAT00000027115.1)
Ensembl transcript not a good match for expression data.

Dog - XM_005623258.3 (OR ENSCAFT00000019096.3)
Ensembl version missing codons at end of transcript.

Mouse - NM_020002.3 OR ENSMUST00000002395.7
Both NCBI & Ensembl versions are the same.

Rat - NM_001011916.1 OR ENSRNOT00000026430.5
Both NCBI & Ensembl versions are the same.

Tree Shrew - XM_006144555.2
*Matches expression data exactly.

Marmoset - XM_009005810.2 (OR ENSCJAT00000013808.2)
NCBI transcript matches expression data - low coverage.

Macaque - XM_015143436.1
*Matches expression data exactly.

Orangutan - XM_009248971.1 OR ENSPPYT00000006722.2
Both NCBI & Ensembl versions are the same.

Gorilla - XM_004054988.2 OR ENSGGOT00000016113.3
Both NCBI & Ensembl versions are the same.

Human - NM_005132.2 OR ENST00000620473.4
Both NCBI & Ensembl versions are the same.

Chimpanzee - NM_001280430.2 (OR ENSPTRT00000011376.6)
Ensembl transcript has a one codon gap.

Bonobo - XM_003809069.3 OR ENSPPAT00000038819.1
Both NCBI & Ensembl versions are the same.

## RNF212B

Chicken - NA

Platypus - XM_007657789.1 OR ENSOANT00000012180.2
Last exons doesn't align well, but supported by expression data.

Opossum - XM_007479816.2 OR ENSMODT00000005737.3
Both NCBI & Ensembl versions are the same.  Last two exons don't align well, but supported by expression data.

Cow - XM_005211442.3 OR ENSBTAT00000036401.1
Both NCBI & Ensembl versions are the same.

Sheep - XM_015096878.1 OR ENSOART00000021072.1
Both NCBI & Ensembl versions are the same.

Pig - XM_021099238.1

Bat - XM_008158556.1
Further investigation needed to determine whether the gap is real. Low quality assembly.

Horse - XM_005603229.2 (OR ENSECAT00000029036.1)
Ensembl transcript missing stop codon.

Dog - XM_005623231.3 OR ENSCAFT00000036997.3
Both NCBI & Ensembl versions are the same.

Mouse - XM_006519865.2 OR ENSMUST00000218311.1
Both NCBI & Ensembl versions are the same.

Rat - NA

Tree Shrew - XM_006144519.1

Marmoset - ENSCJAT00000015307.2 (OR XM_017977003.1)
NCBI transcript has extra codons at start, otherwise the same.

Macaque - XM_015143398.1

Orangutan - XM_009248926.1 OR ENSPPYT00000006692.2
Both NCBI & Ensembl versions are the same.

Gorilla - ENSGGOT00000002204.3  (OR XM_019009238.1)
No expression support for poorly aligned section of NCBI transcript.  Further investigation needed to determine whether the gap is real.

Human - XM_011536313.2 OR ENST00000399910.5
Both NCBI & Ensembl versions are the same.

Chimpanzee - XM_001150530.4 (OR ENSPTRT00000065849.2)
One codon difference, NCBI more parsimonious,

Bonobo - XM_003808095.2 OR ENSPPAT00000037884.1
Both NCBI & Ensembl versions are the same.


## HORMAD2

Chicken - XM_004934462.2

Platypus - NA

Opossum - XM_007490542.2

Cow - XM_005218101.3 OR ENSBTAT00000029451.4
Both NCBI & Ensembl versions are the same.

Sheep - XM_004017471.3 (OR ENSOART00000006711.1)
NCBI more parsimonius.

Pig - sus_scr_HORMAD2.fa
edited ENSSSCT00000010952.3

Bat - XM_008142821.1

Horse - XM_023646875.1 OR ENSECAT00000016246.1
Both NCBI & Ensembl versions are the same.

Dog - XM_849626.5 OR ENSCAFT00000035261.3
Both NCBI & Ensembl versions are the same.

Mouse - NM_029458.1 OR ENSMUST00000109949.7
Both NCBI & Ensembl versions are the same.

Rat - XM_017599331.1 OR ENSRNOT00000080078.1
Both NCBI & Ensembl versions are the same.

Tree Shrew - XM_006147915.2

Marmoset - XM_017979021.1 OR ENSCJAT00000020029.2
Both NCBI & Ensembl versions are the same.

Macaque - XM_001107741.3 OR ENSMMUT00000044106.2
Both NCBI & Ensembl versions are the same.

Orangutan - XM_009234250.1 (OR ENSPPYT00000013586.2)
Sequences differ at a few codons, NCBI version more parsimonius.

Gorilla - XM_019018586.1 OR ENSGGOT00000063480.1
Both NCBI & Ensembl versions are the same.

Human - NM_152510.3 OR ENST00000336726.10
Both NCBI & Ensembl versions are the same.

Chimpanzee - XM_001138517.4 OR ENSPTRT00000064188.3
Both NCBI & Ensembl versions are the same.

Bonobo - XM_003812011.2 OR ENSPPAT00000001079.1
Both NCBI & Ensembl versions are the same.

## MCMDC2

Chicken - ENSGALT00000056272.2

Platypus - XM_007666885.1 OR ENSOANT00000003672.3
Both NCBI & Ensembl versions are the same.

Opossum - XM_007487025.2 OR ENSMODT00000009983.4
Both NCBI & Ensembl versions are the same.

Cow - XM_015474464.1 OR ENSBTAT00000000816.3
Both NCBI & Ensembl versions are the same.

Sheep - XM_015097792.1 OR ENSOART00000019492.1
Both NCBI & Ensembl versions are the same.

Pig - XM_005663044.3 OR ENSSSCT00000006800.3
Both NCBI & Ensembl versions are the same.

Bat - XM_008150364.1

Horse - XM_001494432.6 OR ENSECAT00000019992.1
Both NCBI & Ensembl versions are the same.

Dog - XM_544111.6

Mouse - NM_177722.3 OR ENSMUST00000171802.7
Both NCBI & Ensembl versions are the same.

Rat - NM_001024340.1 OR ENSRNOT00000030053.4
Both NCBI & Ensembl versions are the same.

Tree Shrew - XM_006150453.1

Marmoset - XM_002758967.3

Macaque - XM_015145491.1

Orangutan - XM_002819147.3

Gorilla - XM_019032377.1 OR ENSGGOT00000002787.3
Both NCBI & Ensembl versions are the same.

Human - NM_173518.4 OR ENST00000422365.6
Both NCBI & Ensembl versions are the same.

Chimpanzee - XM_016960222.1 OR ENSPTRT00000037621.5
Both NCBI & Ensembl versions are the same.

Bonobo - XM_008956714.1

## RAD51

Chicken - XM_015286146.1 OR ENSGALT00000070280.1
Both NCBI & Ensembl versions are the same.

Platypus - NA
Assembly issues - at end of contig.

Opossum - XM_007480057.2 OR ENSMODT00000000330.2
Both NCBI & Ensembl versions are the same.

Cow - NM_001046179.2 OR ENSBTAT00000003788.3
Both NCBI & Ensembl versions are the same.

Sheep - XM_004010447.3 OR ENSOART00000022051.1
Both NCBI & Ensembl versions are the same.

Pig - NM_001123181.1 OR ENSSSCT00000005265.2
Both NCBI & Ensembl versions are the same.

Bat - XM_008143005.1

Horse - XM_001503522.4 (OR ENSECAT00000018765.1)
Ensembl transcript missing start codons.

Dog - NM_001003043.1 OR ENSCAFT00000014658.2
Both NCBI & Ensembl versions are the same.

Mouse - NM_011234.4 OR ENSMUST00000028795.9
Both NCBI & Ensembl versions are the same.

Rat - XM_006234784.3 OR ENSRNOT00000056432.2
Both NCBI & Ensembl versions are the same.

Tree Shrew - XM_006158691.1

Marmoset - XM_017976922.1 OR ENSCJAT00000040921.2
Few codon differences, not clear which is better.  Using NCBI by default.

Macaque - XM_015141945.1 OR ENSMMUT00000058167.1
Both NCBI & Ensembl versions are the same.

Orangutan - XM_002825304.2 OR ENSPPYT00000007497.2
Both NCBI & Ensembl versions are the same.

Gorilla - XM_019011276.1 OR ENSGGOT00000068668.1
Both NCBI & Ensembl versions are the same.

Human - NM_002875.4 OR ENST00000267868.7
Both NCBI & Ensembl versions are the same.

Chimpanzee - XM_016927950.1 OR ENSPTRT00000079122.1
Both NCBI & Ensembl versions are the same.

Bonobo - XM_003826585.3 OR ENSPPAT00000060886.1
Both NCBI & Ensembl versions are the same.

## MLH1

Chicken - XM_418828.3 OR ENSGALT00000068346.1
Both NCBI & Ensembl versions are the same.

Platypus - orn_ana_MLH1
XM_007669544.1 OR ENSOANT00000024096.1
*areas of very poor alignment.

Opossum - XM_007500654.2 OR ENSMODT00000017007.2
Both NCBI & Ensembl versions are the same.

Cow - NM_001075994.2 OR ENSBTAT00000022288.4
Both NCBI & Ensembl versions are the same.

Sheep - XM_004018218.3 OR ENSOART00000018033.1
Both NCBI & Ensembl versions are the same.

Pig - ENSSSCT00000027443.2 (OR NM_001172367.1)
Not the same - Ensembl transcript more parsimonius.

Bat - XM_008154103.1

Horse - XM_001489218.6 OR  ENSECAT00000003240.1
Both NCBI & Ensembl versions are the same.

Dog - XM_534219.6 (OR ENSCAFT00000007703.3)
Ensembl transcript missing stop codon.

Mouse - NM_026810.2 OR ENSMUST00000035079.9
Both NCBI & Ensembl versions are the same.

Rat - (NM_031053.1 OR) ENSRNOT00000081718.1
Not the same - Ensembl transcript more parsimonius.

Tree Shrew - XM_006161069.2

Marmoset - XM_002759730.3 (OR ENSCJAT00000024286.2)
NCBI is more parsimonius - extra codon in ensembl.

Macaque - XM_015131400.1 (OR ENSMMUT00000031713.3)
Ensembl missing start of transcript.

Orangutan - ENSPPYT00000016304.1 (OR XM_009239229.1)
NCBI has inaccurate 2nd exon due to assembly issues.  Just absent in Ensembl transcript.
Might be possible to go back and reconstruct a few codons at beginning of first exon.

Gorilla - XM_004033830.2 OR ENSGGOT00000016403.3
Both NCBI & Ensembl versions are the same.

Human - NM_000249.3 OR ENST00000231790.6
Both NCBI & Ensembl versions are the same.

Chimpanzee - XM_001170433.3 OR ENSPTRT00000027570.5
Both NCBI & Ensembl versions are the same.

Bonobo - XM_003826110.2 OR ENSPPAT00000038767.1
Both NCBI & Ensembl versions are the same.

## MLH3

Chicken - gal_gal_TEX11
stitched together XM_004941803.2 OR ENSGALT00000016763.4

Platypus - NA
XM_007664882.1 & XM_007661587.1
Poor assembly, different sections of the gene appear to be on different unplaced scaffolds.
Too messy for now, but may be possible to better reconstruct.

Opossum - XM_001374978.3 OR ENSMODT00000007631.2
Both NCBI & Ensembl versions are the same. Trimmed start.

Cow - bos_tau_MLH3
ENSBTAT00000061421.2 OR XM_010809606.2
Ambiguous ending - inserted an A nucleotide near end to make parsimonius with sheep.  W/o A NCBI transcript best.

Sheep - XM_012182059.2 (OR ENSOART00000001748.1)
Ensembl transcript has extra codons at start.

Pig - ENSSSCT00000045183.1
*Might be able to fill gap (alt exon) from sequence data, if needed.

Bat - XM_008138825.1

Horse - ENSECAT00000008383.1 (OR XM_014735716.2)
NCBI has extra sequence at start - otherwise the same.

Dog - XM_005623668.2 (OR ENSCAFT00000026947.2)
Ensembl transcript missing alt. exon.

Mouse - XM_006515703.3 OR ENSMUST00000220854.1
Both NCBI & Ensembl versions are the same.

Rat - NM_001108043.1 OR ENSRNOT00000033493.3
Both NCBI & Ensembl versions are the same.

Tree Shrew - XM_006170555.2
(...56 NCBI transcript was better match to expression data - alternative splicing)

Marmoset - XM_002754117.3 OR ENSCJAT00000040453.2
Both NCBI & Ensembl versions are the same.

Macaque - NM_001257783.1

Orangutan - ENSPPYT00000007087.2 (OR XM_009249295.1)
Ensembl version has fewer gaps, but need to trim start.

Gorilla - XM_019009267.1 (OR ENSGGOT00000046130.1)
NCBI version has gaps - Ensembl version has errors.  Possible to improve???

Human - NM_001040108.1 OR ENST00000355774.6
Both NCBI & Ensembl versions are the same.

Chimpanzee - ENSPTRT00000089304.1 (OR XM_001158621.4)
NCBI transcript missing sequence.

Bonobo - XM_014347587.1 OR ENSPPAT00000064782.1
Both NCBI & Ensembl versions are the same.

## TEX11

Chicken - ENSGALT00000009276.5

Platypus - NA
*BLAST search?

Opossum - mon_dom_TEX11
spliced together XM_007507601.2 and XM_007507718.1
*still one gap - may be able to use Ensembl transcript to fill in??

Cow - XM_593293.7

Sheep - XM_015104932.1 OR ENSOART00000017348.1
Both NCBI & Ensembl versions are the same.

Pig - XM_003484125.4

Bat - ept_fus_TEX11
XM_008155978.1
trimmed beginning - no expression data to support! Some gaps.

Horse - XM_023634526.1

Dog - XM_022416057.1 (OR ENSCAFT00000026756.4)
NCBI transcript most parsimonius - best start and end.

Mouse - NM_031384.2 OR ENSMUST00000009814.9
Both NCBI & Ensembl versions are the same.

Rat - XM_008773302.2 (OR ENSRNOT00000041731.6)
NCBI more parsimonius.

Tree Shrew - NA
*BLAST search?

Marmoset - cal_jac_TEX11
stitched together ENSCJAT00000027446.2 and ENSCJAT00000015947.2
still some gaps

Macaque - mac_mul_TEX11
Edited based on expression data - still one small gap
ENSMMUT00000067347.1

Orangutan - ENSPPYT00000023845.1
Best match - still has large gaps.
** Try to make better?

Gorilla - XM_004064340.2 OR ENSGGOT00000041060.2
Both NCBI & Ensembl versions are the same.

Human - NM_031276.2 OR ENST00000374333.6
Both NCBI & Ensembl versions are the same.

Chimpanzee - pan_tro_TEX11
ENSPTRT00000040930.4 (OR XM_016944286.1)
NCBI transcript more truncated at start.  Ensembl transcript still missing beginning - reconstructed.

Bonobo - XM_003820153.2 (OR ENSPPAT00000056791.1)
Ensembl transcript truncated.

## MSH4

Chicken - XM_004936904.2
Poor alignment at start, but supported

Platypus - XM_001518796.3
Missing start of transcript - poor assembly.
*Start trimmed

Opossum - ENSMODT00000024256.3
No expression data to check .... poor alignment at beginning of transcript.
*Start trimmed.

Cow - NM_001206255.2

Sheep - XM_004002088.2 (OR ENSOART00000013835.1)
NCBI transcript more parsimonious

Pig - XM_021096463.1
*trimmed start

Bat - XM_008139443.1

Horse - XM_001918273.5 OR ENSECAT00000018447.1
Both NCBI & Ensembl versions are the same

Dog - can_fam_MSH4
edited ENSCAFT00000037908.2 - not sure about first codon, not included in edited version.

Mouse - NM_031870.3 OR ENSMUST00000005630.10
Both NCBI & Ensembl versions are the same
*trimmed start

Rat - NM_001106477.2 OR ENSRNOT00000014106.5
Both NCBI & Ensembl versions are the same.

Tree Shrew - tup_chi_MSH4
edited end of first exon XM_006146089.1

Marmoset - XM_017974846.1 (OR ENSCJAT00000013285.2)
NCBI transcript more parsimonius.

Macaque - XM_015142713.1 (OR ENSMMUT00000001248.3)
Ensembl transcript missing start of gene.

Orangutan - XM_024245413.1

Gorilla - XM_019037482.1 (OR ENSGGOT00000047233.1)
Expression data does not fill in gap.

Human - NM_002440.3 OR ENST00000263187.3
Both NCBI & Ensembl versions are the same.

Chimpanzee - XM_524742.5 OR ENSPTRT00000077635.1
Both NCBI & Ensembl versions are the same.

Bonobo - XM_003830571.2 OR ENSPPAT00000050600.1
Both NCBI & Ensembl versions are the same.

## MSH5

Chicken - XM_015284163.1 OR ENSGALT00000067131.2
Both NCBI & Ensembl versions are the same.

Platypus - orn_ana_MSH5
Modified XM_007672691.1 - poor reference leads to gaps and missing end of the gene

Opossum - XM_003340377.3 (OR ENSMODT00000019372.3)
NCBI more parsimonious - can't access expression data.

Cow - XM_010818306.2 OR ENSBTAT00000026367.4
Both NCBI & Ensembl versions are the same.

Sheep - XM_015102786.1

Pig - XM_021098149.1 (OR ENSSSCT00000057162.1)
Ensembl transcript needs to be trimmed at start.

Bat - XM_008157343.1

Horse - XM_014734309.2  (OR ENSECAT00000022088.1)
Ensembl transcript missing codons at beginning.

Dog - can_fam_MSH5
From XM_005627746.2
Gap near start, assembly issue/gap.

Mouse - NM_013600.3 OR ENSMUST00000007250.13
Both NCBI & Ensembl versions are the same.

Rat - XM_017601574.1 OR ENSRNOT00000091022.1
Both NCBI & Ensembl versions are the same.

Tree Shrew - XM_006154286.2

Marmoset - ENSCJAT00000005329.2 (OR XM_017970974.1)
Ensembl transcript more parsimonious.

Macaque - XM_015135995.1 OR ENSMMUT00000013550.3
Both NCBI & Ensembl versions are the same.

Orangutan - XM_024248315.1 (OR ENSPPYT00000019136.1)
NCBI transcript more parsimonius.

Gorilla - XM_019028888.1 OR ENSGGOT00000060016.1
Both NCBI & Ensembl versions are the same.

Human - NM_002441.4 OR ENST00000375755.7
Both NCBI & Ensembl versions are the same.

Chimpanzee - XM_016955173.1 (OR ENSPTRT00000033224.6)
One codon difference - NCBI more parsimonious.
The extra codons (insert) are supported by 5 reads (to 4).

Bonobo - XM_008956893.1

## RAD21L

Chicken - XM_015296432.1 OR ENSGALT00000039400.4
NCBI more parsimonious.

Platypus - Not Annotated.

Opossum - XM_016428718.1 (OR ENSMODT00000031805.2)
NCBI more parsimonious.

Cow - XM_010811624.2 (OR ENSBTAT00000001812.5)
small differences, NCBI transcript more parsimonious

Sheep - XM_012188953.1 OR ENSOART00000020411.1
Both NCBI & Ensembl versions are the same.

Pig - sus_scr_RAD21L
Edited XM_021077689.1
(possibly took too much license with 1bp insertions in the conservative direction.)

Bat - XM_008140993.1

Horse - XM_023626262.1 (OR ENSECAT00000025198.1)
Gap in ensembl transcript.

Dog - XM_846853.5 OR ENSCAFT00000010977.4
Both NCBI & Ensembl versions are the same.

Mouse - NM_001276400.1 OR ENSMUST00000180195.7
Both NCBI & Ensembl versions are the same.

Rat - XM_001072159.4 OR ENSRNOT00000055455.3
Both NCBI & Ensembl versions are the same.

Tree Shrew - XM_006162491.1

Marmoset - ENSCJAT00000041064.1 (OR XM_017971892.1)
Ensembl transcript more parsimonious - one codon insert.

Macaque - XM_015149313.1 OR ENSMMUT00000072818.1
Both NCBI & Ensembl versions are the same.

Orangutan - XM_002830140.1

Gorilla - XM_019017008.1 OR ENSGGOT00000033526.2
Both NCBI & Ensembl versions are the same.

Human - XM_006723605.3 OR ENST00000409241.5
Both NCBI & Ensembl versions are the same.

Chimpanzee - XM_016937282.1 OR ENSPTRT00000059351.3
Both NCBI & Ensembl versions are the same.

Bonobo - XM_008974724.1 OR ENSPPAT00000010569.1
Both NCBI & Ensembl versions are the same.

## MEIOB

Chicken - XM_414840.5 OR ENSGALT00000033814.4
Both NCBI & Ensembl versions are the same.

Platypus - XM_007657223.1 (OR ENSOANT00000004639.1)
NCBI has a complete ending of the transcript (to stop codon).

Opossum - XM_001365539.3 (OR ENSMODT00000020467.3)
NCBI has a complete ending of the transcript (to stop codon).

Cow - ENSBTAT00000037536.2
*Edited to insert last three amino acids (from truncated isoform XM_015460247.1)

Sheep - XM_012103956.2

Pig - XM_021086801.1 OR ENSSSCT00000059272.1
Both NCBI & Ensembl versions are the same.
*trimmed beginning

Bat - XM_008146387.1

Horse - XM_023616606.1

Dog - XM_003434870.4 (OR ENSCAFT00000030980.5)
NCBI transcript more parsimonious.

Mouse - NM_029197.1 OR ENSMUST00000024972.5
Both NCBI & Ensembl versions are the same.

Rat - NM_001115033.1 OR ENSRNOT00000060551.2
Both NCBI & Ensembl versions are the same.

Tree Shrew - tup_chi_MEIOB
edited from XM_014587028.1 - expression data support exon not included in transcript

Marmoset - ENSCJAT00000028758.2

Macaque - NM_001193903.1 (OR ENSMMUT00000001059.3)
Gap in ensemble transcript.

Orangutan - XM_024234098.1 (OR ENSPPYT00000008216.1)
Gap in ensembl transcript.

Gorilla - XM_004056970.2 OR ENSGGOT00000012313.3
Both NCBI & Ensembl versions are the same.

Human - NM_001163560.2 OR ENST00000412554.6
Both NCBI & Ensembl versions are the same.

Chimpanzee - ENSPTRT00000014042.5 (OR XM_016929181.1)
Ensembl transcript more parsimonious.

Bonobo - XM_003807700.3
Both NCBI & Ensembl versions are the same.
missing end of transcript due to gap in assembly

## SPATA22

Chicken - XM_004946690.2

Platypus - XM_016228458.1 OR ENSOANT00000029779.2
Both NCBI & Ensembl versions are the same.

Opossum - XM_007506456.2
Matches expression data, but an overall elevation of expression coverage that is abnormal.

Cow - XM_010815932.2 OR ENSBTAT00000020932.4
Both NCBI & Ensembl versions are the same.

Sheep - XM_012185494.2

Pig - NM_001177921.1 OR ENSSSCT00000030197.2
Both NCBI & Ensembl versions are the same.

Bat - XM_008156773.1

Horse - XM_001504720.2 OR ENSECAT00000022882.1
Both NCBI & Ensembl versions are the same.

Dog - XM_005624350.2 (OR ENSCAFT00000050035.1)
Ensembl transcript missing last few codons.

Mouse - NM_001045531.1 OR ENSMUST00000092926.10
Both NCBI & Ensembl versions are the same.

Rat - XM_017597378.1 OR ENSRNOT00000056443.5
Both NCBI & Ensembl versions are the same.

Tree Shrew - XM_006167586.1
** strongly supported by expression data

Marmoset - XM_002747832.2
** Missing start of gene.  No expression evidence for the first part of the gene in Marmoset - but can check again.

Macaque - XM_015118240.1 OR ENSMMUT00000015459.2
Both NCBI & Ensembl versions are the same.

Orangutan - XM_002826841.2 OR ENSPPYT00000009159.2
Both NCBI & Ensembl versions are the same.

Gorilla - XM_004058278.2 OR ENSGGOT00000044319.1
Both NCBI & Ensembl versions are the same.

Human - NM_001170698.1 OR ENST00000572969.5
Both NCBI & Ensembl versions are the same.

Chimpanzee - XM_009431542.2 OR ENSPTRT00000015801.5
Both NCBI & Ensembl versions are the same.

Bonobo - XM_003810239.1 OR ENSPPAT00000053825.1
Both NCBI & Ensembl versions are the same.

## SYCP1

Chicken - ENSGALT00000003960.6

Platypus - ENSOANT00000007172.2 (OR XM_016228058.1)
Ensembl is more parsimonious - missing start of transcript appears to be supported by expression/reference info.

Opossum - XM_007485237.2 OR ENSMODT00000006036.3
Both NCBI & Ensembl versions are the same.

Cow - XM_010803140.2 (OR ENSBTAT00000030769.3)
NCBI is more parsimonious.
*trimmed start

Sheep - XM_015092191.1 OR ENSOART00000021870.1
Both NCBI & Ensembl versions are the same.

Pig - XM_021090002.1 OR ENSSSCT00000007395.3
NCBI is more parsimonious.

Bat - XM_008147202.1

Horse - XM_023641375.1 (OR ENSECAT00000013840.1)
NCBI is more parsimonious.

Dog - XM_014120721.1 (OR ENSCAFT00000015417.4)
NCBI is more parsimonious.

Mouse - NM_011516.2 OR ENSMUST00000029448.10
Both NCBI & Ensembl versions are the same.

Rat - rat_nor_SYCP1
NM_012810.1 OR ENSRNOT00000023333.5
added start of transcript missing from both databases, but supported by expression data

Tree Shrew - XM_006149647.2
trimmed start of transcript

Marmoset - XM_009001949.2 OR ENSCJAT00000024669.2
Ensembl transcript is more parsimonious.

Macaque - XM_015148835.1 OR ENSMMUT00000024850.3
Both NCBI & Ensembl versions are the same.

Orangutan - XM_002810393.2 OR ENSPPYT00000001197.1
Both NCBI & Ensembl versions are the same.

Gorilla - gor_gor_SYCP1
XM_019034831.1 (OR ENSGGOT00000015631.3)
removed small exon not supported by expression data

Human - NM_001282541.1 OR ENST00000618516.4
Both NCBI & Ensembl versions are the same.

Chimpanzee - XM_016925115.1 OR ENSPTRT00000002134.4
Both NCBI & Ensembl versions are the same.

Bonobo - XM_008973531.1 OR ENSPPAT00000039129.1
Both NCBI & Ensembl versions are the same.

## SYCP2

Chicken - XM_015296671.1

Platypus - XM_016228212.1

Opossum - ENSMODT00000030732.3

---

Cow - bos_tau_SYCP2
XM_015474200.1 OR ENSBTAT00000004704.5
removed exon with limited expression support - more parsimonious.

Sheep - XM_012188887.1 (OR ENSOART00000016830.1)
Ensembl transcript missing end.

Pig - XM_021078151.1 (OR ENSSSCT00000036024.2)
Ensembl transcript is of poor quality.

Bat - ept_fus_SYCP2
Edited from XM_008157159.1
Assembly low quality with lots of gaps, removed three exons with no support.

Horse - XM_023626839.1

Dog - XM_014107147.2 (OR ENSCAFT00000050079.2)
Gap strongly supported by expression data.

Mouse - NM_177191.3 OR ENSMUST00000081134.9
Both NCBI & Ensembl versions are the same.

Rat - NM_130735.1 OR ENSRNOT00000078047.1
Both NCBI & Ensembl versions are the same.

Tree Shrew - XM_006172210.2
First half of gene missing due to gap in assembly.
**2 stop codons

Marmoset - XM_002747732.3

Macaque - XM_015148684.1 OR ENSMMUT00000022886.3
Both NCBI & Ensembl versions are the same.

Orangutan - XM_024238859.1 (OR ENSPPYT00000012990.2)
NCBI transcript is more parsimonious.

Gorilla - XM_004062461.1 OR ENSGGOT00000067482.1
Both NCBI & Ensembl versions are the same.

Human - NM_014258.3 OR ENST00000357552.7
Both NCBI & Ensembl versions are the same.

Chimpanzee - XM_016938204.1 (OR ENSPTRT00000045404.4)
NCBI transcript is more parsimonious.

Bonobo - XM_014343106.1 (OR ENSPPAT00000038702.1)
Errors at start of ensembl transcript.
**2 stop codons

## TEX12

Chicken - XM_015298301.1

Platypus - NA
Could not find in NCBI or Ensembl - follow-up.

Opossum - XM_007494826.1 OR ENSMODT00000039962.2
Both NCBI & Ensembl versions are the same.

Cow - NM_001034263.1 OR ENSBTAT00000022009.3
Both NCBI & Ensembl versions are the same.

Sheep - XM_015089784.1 (OR ENSOART00000017776.1)
Ensembl transcript missing stop codon, otherwise the same.

Pig - XM_005667333.3  (OR ENSSSCT00000023354.2)
NCBI transcript more parsimonious at start.

Bat - XM_008150228.1
Missing end of transcript due to gap in assembly - was able to add an additional codon to the end from the reference.

Horse - XM_001501892.4  (OR ENSECAT00000021312.1)
NCBI transcript more parsimonious.

Dog - XM_848996.5 (OR ENSCAFT00000022196.3)
Ensembl transcript missing stop codon, otherwise the same.

Mouse - NM_025687.3 OR ENSMUST00000217236.1
Both NCBI & Ensembl versions are the same.

Rat - NM_001191106.1 OR ENSRNOT00000013014.5
Both NCBI & Ensembl versions are the same.

Tree Shrew - XM_006151001.1

Marmoset - XM_017978433.1
*gap in transcript most likely due to gap in assembly.

Macaque - XM_015115667.1 OR  ENSMMUT00000072122
Both NCBI & Ensembl versions are the same.

Orangutan - XM_002822475.3

Gorilla - XM_004052130.2

Human - NM_031275.4 OR ENST00000530752.5
Both NCBI & Ensembl versions are the same.

Chimpanzee - XM_016921991.2 OR ENSPTRT00000007974.5
Both NCBI & Ensembl versions are the same.

Bonobo - XM_003805463.2

