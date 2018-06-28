# USAGE:
# python gene.py GENE > GENE.fasta

# purpose is to generate gene specific files for use with PAML from large lists
# of many genes across multiple species

import sys
from Bio import SeqIO

for seq_record in SeqIO.parse("master/master.fa", "fasta"):
	if sys.argv[1] in seq_record.description:
		print('>',seq_record.id)
		print(seq_record.seq)						
