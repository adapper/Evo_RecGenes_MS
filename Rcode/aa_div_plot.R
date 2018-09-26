
args = commandArgs(trailingOnly=TRUE)

library(ggplot2)
library(zoo)
library(readr)
library(reshape)

# test if there is at least one argument: if not, return an error
if (length(args)==0) {
    stop("At least one argument must be supplied (input file).n", call.=FALSE)
}

# Import
gene_aa_div <- read_delim(paste(c('../Data/summary_files/',args[1],'_aa_div.txt'), collapse='')," ", escape_double = FALSE, col_names = FALSE, trim_ws = TRUE)

# Add empty column for sliding window values
gene_aa_div$X3 <- NA

# Calculate sliding windows:
win_size <- 10
win_slide <- 5
slide <- rollapply(gene_aa_div$X2, win_size, mean, by = win_slide) 
# print(slide)

for (i in 1:length(slide)){
  gene_aa_div$X3[i*win_slide] <- slide[i]
}

# Plot with sliding window averages
png(paste(c(args[1],'_aa_slide.png'), collapse = ''), units = "in", width = 18, height = 10, res = 500)
plot(gene_aa_div$X1,gene_aa_div$X2, pch = "*", ylim = c(0,1), ylab = "Amino Acid Conservation", xlab = "Position")
points(gene_aa_div$X1,gene_aa_div$X3, col = "red", lwd = 3)
dev.off()

# Plot with LOESS smoothing
png(paste(c(args[1],'_aa_div.png'), collapse = ''), units = "in", width = 18, height = 10, res = 500)
ggplot(gene_aa_div, aes(x=gene_aa_div$X1,y=gene_aa_div$X2)) +
  geom_point() +
  geom_smooth(span = 0.5) +
  ylim(0,1) + ylab("Amino Acid Conservation") + xlab("Position")
dev.off()
