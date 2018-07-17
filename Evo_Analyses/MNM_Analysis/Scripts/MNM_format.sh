#!/bin/bash

# Remove header.
tail -n +3 MNM_Removal/$1_ancestral.fa > MNM_Removal/$1.tmp

# Add '>' to the start of each line.
sed -i -e 's/^/>/' MNM_Removal/$1.tmp

# Remove # from the Node names.
sed -i -e 's/ #//' MNM_Removal/$1.tmp

# Add new line between name and start of sequence.
gsed -i -e "s/     /\\n/" MNM_Removal/$1.tmp

# Remove spaces.
tr -d ' ' < MNM_Removal/$1.tmp > MNM_Removal/$1_MNM.fa

# Remove excess files.
rm MNM_Removal/*.tmp
rm MNM_Removal/*.tmp-e
