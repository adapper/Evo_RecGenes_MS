import sys
import statistics as st

"""
function to translate a sequence, given a gene table
"""
#credit to https://www.biostars.org/p/157527/
#could also just use biopython here
bases = ['T', 'C', 'A', 'G']
codons = [a+b+c for a in bases for b in bases for c in bases]
amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
codon_table = dict(zip(codons, amino_acids))

#nostop -- if True, don't break at stop codons
#use 'd' to indicate a codon deletion
#translate sequence
def translate(seq, nostop = True):
    peptide = ''
    if nostop == False:
        for i in range(0, len(seq), 3):
            codon = seq[i:(i + 3)]
            amino_acid = codon_table.get(codon, '*')
            if amino_acid != '*':
                peptide += amino_acid
            else:
                break
    elif nostop == True:
        try:
            aa_counter = 0
            for i in range(0, len(seq), 3):
                codon = seq[i:(i + 3)]
                if codon != '---':
                    amino_acid = codon_table.get(codon)
                    peptide += amino_acid
                elif codon == '---':
                    peptide += 'd'
        except TypeError:
            print('seq ' + codon + ' not a valid codon')
    return(peptide)    

with open(sys.argv[1]) as inf:

    ##get 2 seqs
    seq_ls = []
    for line in inf:
        if not line.startswith('>'):
            seq = line.rstrip()
            seq_ls.append(seq)

##translate both seqs
aa_seq_ls = []
for seq in seq_ls:
    aa_seq = translate(seq)
    aa_seq_ls.append(aa_seq)

##what dna positions contain substitutions?
sub_ls = []
for pos in range(len(seq_ls[0])):
    if seq_ls[0][pos] != seq_ls[1][pos]:
           sub_ls.append(pos)
    
##what codons are these in?
aa_sub_ls = []
for pos in sub_ls:
    aa_pos = int(pos / 3)
    aa_sub_ls.append(aa_pos)

##do these substitutions result in amino acid change?
syn_count = 0
nonsyn_count = 0
for pos in aa_sub_ls:
    aa1 = aa_seq_ls[0][pos]
    aa2 = aa_seq_ls[1][pos]
    if aa1 == 'd' or aa2 == 'd':
        continue
    if aa1 != aa2:
        nonsyn_count += 1
    elif aa1 == aa2:
        syn_count += 1
print('# nonsynonymous substitutions: ', str(nonsyn_count))
print('# synonymous substitutions: ', str(syn_count))


"""
number of possible DN/DS
"""
#changing position 'pos', what are all possible amino acids -- 'pos' is zero-based
def get_possible_aa(codon, pos):
    pos_ls = ['A', 'T', 'C', 'G']
    aa_ls = []
    for change_ID in pos_ls:
        cd = list(codon)
        cd[pos] = change_ID
        new_codon = ''
        for i in cd:
            new_codon += i
        aa = codon_table.get(new_codon)
        aa_ls.append(aa)
    return(aa_ls)
            
#calculate synonymous addition for a codon position
#aa: amino acid observed at a site
#aa_ls: list of amino acids obtained following a substitution at a position in observed codon (obtained via get_possible_aa)
def get_synonymous_weight(aa, aa_ls):
    synonymous_count = 0
    for i in aa_ls:
        if i == aa:
            synonymous_count += 1
    #subtract 1 (because the observed amino acid/codon combination is in this list) and divide by three to get synonymous weight
    synonymous_weight = (synonymous_count - 1) / float(3)
    return(synonymous_weight)
        
        
#apply get_possible_aa and get_synonymous_weight to first and third positions of a codon
#sums number of synonymous and nonsynonymous sites w/in a codon
#returns tuple, first position containing synonymous addition for the codon, second containing nonsynonymous
def get_codon_syn_nonsyn_add(codon):
    a = codon_table.get(codon)
    #start with 0
    sum_syn_weight = 0
    #start with 1, for nonsynonymous second position
    sum_nonsyn_weight = 1
    for i in [0, 2]:
        ls = get_possible_aa(codon, i)
        syn_weight = get_synonymous_weight(a, ls)
        sum_syn_weight += syn_weight
        sum_nonsyn_weight += (1 - syn_weight)
    return(sum_syn_weight, sum_nonsyn_weight)
        

##Iterate over codons -- return summed weights
def codon_map(seq):
    syn_nonsyn_dict = {'syn_count' : 0, 'nonsyn_count' : 0}
    for i in range(0, len(seq), 3):
        c = seq[i:(i + 3)]
        if c != '---':
            weights = get_codon_syn_nonsyn_add(c)
            syn_nonsyn_dict['syn_count'] += weights[0]
            syn_nonsyn_dict['nonsyn_count'] += weights[1]
    print(syn_nonsyn_dict)
    
##Iterate over codons -- return list of tuples. 1st postion -- synonymous weight for a codon. 2nd postion -- nonsynonymous weight for a codon.
def codon_map_ls(seq):
    syn_nonsyn_ls = []
    for i in range(0, len(seq), 3):
        c = seq[i:(i + 3)]
        weights = get_codon_syn_nonsyn_add(c)
        syn_nonsyn_ls.append(weights)
    return(syn_nonsyn_ls)

def avg_synnonsyn_exdel(seq_1, seq_2):
    weights_1 = codon_map_ls(seq_ls[0])
    weights_2 = codon_map_ls(seq_ls[1])
    aa_seq_1 = translate(seq_ls[0])
    aa_seq_2 = translate(seq_ls[1])
    d_ct = 0
    syn_nonsyn_dict = {'syn_count' : 0, 'nonsyn_count' : 0}
    for i in range(len(weights_1)):
        if aa_seq_1[i] != 'd' and aa_seq_2[i] != 'd':
            mean_syn = st.mean([weights_1[i][0], weights_2[i][0]])
            mean_nonsyn = st.mean([weights_1[i][1], weights_2[i][1]])
            syn_nonsyn_dict['syn_count'] += mean_syn
            syn_nonsyn_dict['nonsyn_count'] += mean_nonsyn
    print(syn_nonsyn_dict)

#get sequence ID's

name_ls = []

with open(sys.argv[1]) as inf:
    for line in inf:
        if line.startswith('>'):
            name_ls.append(line.rstrip()[2:])

print(name_ls[0])
codon_map(seq_ls[0])

print(name_ls[1])
codon_map(seq_ls[1])

print('Human-Macaque Average (excluding indels)')
avg_synnonsyn_exdel(seq_ls[0], seq_ls[1])


        
    
    
    
    


    