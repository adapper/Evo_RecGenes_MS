#!/bin/bash
# step2.sh GENE

python3 Scripts/yellowMNM.py $1 > MNM_Removal/$1_MNMlist.txt

Scripts/redMNM.sh $1 > MNM_Removal/$1_MNM_summary.txt

Scripts/redMNM.sh $1

python3 Scripts/remove_MNM.py $1 > MNM_Removal/$1_noMNM.fasta
