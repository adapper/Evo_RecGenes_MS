### python remove_MNM.py

import sys
from Bio import SeqIO

gene = sys.argv[1]

species = ['_MOUSE', '_RAT', '_TREE_SHREW', '_CHIMP', '_BONOBO', '_HUMAN', '_GORILLA', '_ORANGUTAN', '_MACAQUE', '_MARMOSET', '_COW', '_SHEEP', '_PIG', '_DOG', '_HORSE', '_BAT']

# NO BONOBO
#node23 = ['_MOUSE', '_RAT']
#node22 = ['_CHIMP', '_HUMAN']
#node21 = ['_CHIMP', '_HUMAN', '_GORILLA']
#node20 = ['_CHIMP', '_HUMAN', '_GORILLA', '_ORANGUTAN']
#node19 = ['_CHIMP', '_HUMAN', '_GORILLA', '_ORANGUTAN', '_MACAQUE']
#node18 = ['_CHIMP', '_HUMAN', '_GORILLA', '_ORANGUTAN', '_MACAQUE', '_MARMOSET']
#node17 = ['_CHIMP', '_HUMAN', '_GORILLA', '_ORANGUTAN', '_MACAQUE', '_MARMOSET', '_TREE_SHREW']
#node27 = ['_COW', '_SHEEP']
#node26 = ['_COW', '_SHEEP', '_PIG']
#node25 = ['_COW', '_SHEEP', '_PIG', '_DOG']
#node28 = ['_HORSE', '_BAT']
#node24 = ['_COW', '_SHEEP', '_PIG', '_DOG', '_HORSE', '_BAT']

# NO TREE SHREW
node23 = ['_MOUSE', '_RAT']
node22 = ['_BONOBO', '_CHIMP']
node21 = ['_BONOBO', '_CHIMP', '_HUMAN']
node20 = ['_BONOBO', '_CHIMP', '_HUMAN', '_GORILLA']
node19 = ['_BONOBO', '_CHIMP', '_HUMAN', '_GORILLA', '_ORANGUTAN']
node18 = ['_BONOBO', '_CHIMP', '_HUMAN', '_GORILLA', '_ORANGUTAN', '_MACAQUE']
node17 = ['_BONOBO', '_CHIMP', '_HUMAN', '_GORILLA', '_ORANGUTAN', '_MACAQUE', '_MARMOSET']
node27 = ['_COW', '_SHEEP']
node26 = ['_COW', '_SHEEP', '_PIG']
node25 = ['_COW', '_SHEEP', '_PIG', '_DOG']
node28 = ['_HORSE', '_BAT']
node24 = ['_COW', '_SHEEP', '_PIG', '_DOG', '_HORSE', '_BAT']

# ALL
#node25 = ['_MOUSE', '_RAT']
#node24 = ['_BONOBO', '_CHIMP']
#node23 = ['_BONOBO', '_CHIMP', '_HUMAN']
#node22 = ['_BONOBO', '_CHIMP', '_HUMAN', '_GORILLA']
#node21 = ['_BONOBO', '_CHIMP', '_HUMAN', '_GORILLA', '_ORANGUTAN']
#node20 = ['_BONOBO', '_CHIMP', '_HUMAN', '_GORILLA', '_ORANGUTAN', '_MACAQUE']
#node19 = ['_BONOBO', '_CHIMP', '_HUMAN', '_GORILLA', '_ORANGUTAN', '_MACAQUE', '_MARMOSET']
#node18 = ['_BONOBO', '_CHIMP', '_HUMAN', '_GORILLA', '_ORANGUTAN', '_MACAQUE', '_MARMOSET', '_TREE_SHREW']
#node29 = ['_COW', '_SHEEP']
#node28 = ['_COW', '_SHEEP', '_PIG']
#node27 = ['_COW', '_SHEEP', '_PIG', '_DOG']
#node30 = ['_HORSE', '_BAT']
#node26 = ['_COW', '_SHEEP', '_PIG', '_DOG', '_HORSE', '_BAT']

for seq_record in SeqIO.parse('MNM_Removal/%s_MNM.fa' % (gene), "fasta"):
    if seq_record.id in species:
        seq = seq_record.seq
        mutable_seq = seq.tomutable()
        codon = []
        with open('MNM_Removal/%s_MNMlist.txt' % (gene)) as f:
            for line in f:
                line = line.split(' ')
                if line[1] == seq_record.id:
                    codon.append(int(line[0]))
                if line[1] == 'node17' and seq_record.id in node17:
                    codon.append(int(line[0]))
                if line[1] == 'node18' and seq_record.id in node18:
                    codon.append(int(line[0]))
                if line[1] == 'node19' and seq_record.id in node19:
                    codon.append(int(line[0]))
                if line[1] == 'node20' and seq_record.id in node20:
                    codon.append(int(line[0]))
                if line[1] == 'node21' and seq_record.id in node21:
                    codon.append(int(line[0]))
                if line[1] == 'node22' and seq_record.id in node22:
                    codon.append(int(line[0]))
                if line[1] == 'node23' and seq_record.id in node23:
                    codon.append(int(line[0]))
                if line[1] == 'node24' and seq_record.id in node24:
                    codon.append(int(line[0]))
                if line[1] == 'node25' and seq_record.id in node25:
                    codon.append(int(line[0]))
                if line[1] == 'node26' and seq_record.id in node26:
                    codon.append(int(line[0]))
                if line[1] == 'node27' and seq_record.id in node27:
                    codon.append(int(line[0]))
                if line[1] == 'node28' and seq_record.id in node28:
                    codon.append(int(line[0]))
#if line[1] == 'node29' and seq_record.id in node29:
#codon.append(int(line[0]))
#if line[1] == 'node30' and seq_record.id in node30:
#codon.append(int(line[0]))
        #print(codon, len(codon))
        for i in range(len(codon)):
            CODON = codon[i]
            bp = CODON*3
            mutable_seq[bp] = '-'
            mutable_seq[bp+1] = '-'
            mutable_seq[bp+2] = '-'
        print('>', seq_record.description)
        print(mutable_seq)



