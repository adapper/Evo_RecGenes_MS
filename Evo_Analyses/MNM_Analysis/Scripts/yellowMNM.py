## python select_codon.py GENE CODONS

import sys
from Bio import SeqIO

gene = sys.argv[1]
#codons = int(sys.argv[2])-1

for seq_record in SeqIO.parse('MNM_Removal/%s_MNM.fa' % (gene), "fasta"):
    SEQ = seq_record.seq
codons = int((len(SEQ))/3)

for j in range(codons):
    bp = j*3

	# Make table of codons & species/nodes:
    table = []
    for seq_record in SeqIO.parse('MNM_Removal/%s_MNM.fa' % (gene), "fasta"):
        seq = seq_record.seq
        codon = [seq_record.id, seq[bp], seq[bp+1], seq[bp+2]]
        table.append(codon)


# NO TREE SHREW
    focal = ['_MOUSE','_RAT','_CHIMP','_BONOBO','_HUMAN','_GORILLA','_ORANGUTAN','_MACAQUE','_MARMOSET','_COW','_SHEEP','_PIG','_DOG','_HORSE','_BAT', 'node17', 'node18', 'node19', 'node20', 'node21', 'node22', 'node23', 'node24', 'node25', 'node26', 'node27', 'node28']
    node = ['node23', 'node23', 'node22', 'node22', 'node21', 'node20', 'node19', 'node18', 'node17', 'node27', 'node27', 'node26', 'node25', 'node28', 'node28', 'node16', 'node17', 'node18', 'node19', 'node20', 'node21', 'node16', 'node16', 'node24', 'node25', 'node16', 'node24']

# NO BONOBO
#focal = ['_MOUSE','_RAT','_CHIMP','_HUMAN','_GORILLA','_ORANGUTAN','_MACAQUE','_MARMOSET','_TREE_SHREW','_COW','_SHEEP','_PIG','_DOG','_HORSE','_BAT','node17','node18','node19', 'node20','node21','node22','node23','node24','node25','node26','node27','node28']
#node = ['node23','node23', 'node22', 'node22', 'node21', 'node20', 'node19', 'node18', 'node17', 'node27', 'node27', 'node26', 'node25', 'node28', 'node28','node16', 'node17', 'node18', 'node19', 'node20', 'node21', 'node16', 'node16', 'node24', 'node25', 'node26', 'node24']

# ALL
#focal = ['_MOUSE','_RAT','_CHIMP','_BONOBO','_HUMAN','_GORILLA','_ORANGUTAN','_MACAQUE','_MARMOSET','_TREE_SHREW','_COW','_SHEEP','_PIG','_DOG','_HORSE','_BAT','node18', 'node19', 'node20', 'node21', 'node22', 'node23', 'node24', 'node25', 'node26', 'node27', 'node28', 'node29', 'node30']
#node = ['node25', 'node25', 'node24', 'node24', 'node23', 'node22', 'node21', 'node20', 'node19', 'node18', 'node29', 'node29', 'node28', 'node27', 'node30', 'node30', 'node17', 'node18', 'node19', 'node20', 'node21', 'node22', 'node23', 'node17', 'node17', 'node26', 'node27', 'node28', 'node26']

    for k in range(len(focal)):
	    # Pull out pair for comparison:
        for i in range((len(table))):
            if table[i][0] == focal[k]:
                A = table[i]
            if table[i][0] == node[k]:
                B = table[i]

	    # Count differences:
        x = 0
        if A[1] != B[1] and A[1] != '-' and B[1] != '-':
            x = x + 1
        if A[2] != B[2] and A[2] != '-' and B[2] != '-':
            x = x + 1
        if A[3] != B[3] and A[3] != '-' and B[3] != '-':
            x = x + 1

	    # MNM?
        if x > 1:
            print(j, A[0], A[1], A[2], A[3]) #, B[0], B[1], B[2], B[3])







	
