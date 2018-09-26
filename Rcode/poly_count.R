library(readr)

#args = commandArgs(trailingOnly=TRUE)

GENE <- read_csv("Data/polymorphism/RNF212B_ExAC.csv")
#GENE <- read.csv(paste(c('Data/polymorphism/',args[1],'_ExAC.csv'), collapse=''))
#View(GENE)

GENE_EXON <-GENE[!(GENE$Annotation=="intron"),]
GENE_EXON <-GENE_EXON[!(GENE_EXON$Annotation=="splice region"),]
GENE_EXON <-GENE_EXON[!(GENE_EXON$Annotation=="splice donor"),]
GENE_EXON <-GENE_EXON[!(GENE_EXON$Annotation=="splice acceptor"),]
GENE_EXON <-GENE_EXON[!(GENE_EXON$Annotation=="frameshift"),]
GENE_EXON <-GENE_EXON[!(GENE_EXON$Annotation=="stop gained"),]
GENE_EXON <-GENE_EXON[!(GENE_EXON$Annotation=="3' UTR"),]
GENE_EXON <-GENE_EXON[!(GENE_EXON$Annotation=="5' UTR"),]
GENE_EXON <-GENE_EXON[!(GENE_EXON$Annotation=="downstream gene"),]
GENE_EXON <-GENE_EXON[!(GENE_EXON$Annotation=="upstream gene"),]
GENE_EXON <-GENE_EXON[!(GENE_EXON$Annotation=="inframe deletion"),]
GENE_EXON <-GENE_EXON[!(GENE_EXON$Annotation=="coding sequence"),]
GENE_EXON <-GENE_EXON[!(GENE_EXON$Annotation=="stop lost"),]
GENE_EXON <-GENE_EXON[!(GENE_EXON$Annotation=="inframe insertion"),]
GENE_EXON <-GENE_EXON[!(GENE_EXON$Annotation=="start lost"),]
GENE_EXON <-GENE_EXON[!(GENE_EXON$Annotation=="stop retained"),]

# Remove sites at the same position
row = 0
double_pos = c()
for (row in 1:(nrow(GENE_EXON)-1)){
  pos <- GENE_EXON[row, "Position"]
  pos2 <- GENE_EXON[row+1, "Position"]
  row = row + 1
  if (pos == pos2){
    double_pos <- c(double_pos, row, row + 1)
  }
}
GENE_EXON <- GENE_EXON[-double_pos, ]

# Check for triple hits.
for (row in 1:(nrow(GENE_EXON)-2)){
  pos <- GENE_EXON[row, "Position"]
  pos2 <- GENE_EXON[row+1, "Position"] 
  pos3 <- GENE_EXON[row+2, "Position"]
  if (pos == pos2 & pos2 == pos3){
    print("WARNING")
  }
}

GENE_SING <-GENE_EXON[!(GENE_EXON$`Allele Count`=="1"),]

GENE_RSID <-GENE_EXON[!(GENE_EXON$RSID=="."),]

GENE_EURO <-GENE_EXON[!(GENE_EXON$`Allele Count European (Non-Finnish)`=="0"),]

GENE_EURO_SING <-GENE_EURO[!(GENE_EURO$`Allele Count European (Non-Finnish)`=="1"),]

GENE_EURO_RSID <-GENE_EURO[!(GENE_EURO$RSID=="."),]

print("All Data")
print(table(unlist(GENE_EXON$Annotation)))

#print("RSID Only")
#print(table(unlist(GENE_RSID$Annotation)))

#print("No Singletons")
#print(table(unlist(GENE_SING$Annotation)))

#print("European Population")
#print(table(unlist(GENE_EURO$Annotation)))

#print("European Population - RSID Only")
#print(table(unlist(GENE_EURO_RSID$Annotation)))

#print("European Population - No Singletons")
#print(table(unlist(GENE_EURO_SING$Annotation)))
