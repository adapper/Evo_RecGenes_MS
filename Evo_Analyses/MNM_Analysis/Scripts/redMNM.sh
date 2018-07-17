#!/bin/bash
# redMNM.sh GENE

echo "MOUSE:" 
grep -o "MOUSE" MNM_Removal/$1_MNMlist.txt | wc -l

echo "RAT:"
grep -o "RAT" MNM_Removal/$1_MNMlist.txt | wc -l

#No BONOBO / TREE_SHREW
echo "Node23 (MOUSE, RAT):"
grep -o "node23" MNM_Removal/$1_MNMlist.txt | wc -l

#echo "Node25 (MOUSE, RAT):"
#grep -o "node25" MNM_Removal/$1_MNMlist.txt | wc -l

echo "CHIMP:"
grep -o "CHIMP" MNM_Removal/$1_MNMlist.txt | wc -l

echo "BONOBO:"
grep -o "BONOBO" MNM_Removal/$1_MNMlist.txt | wc -l

# NO Tree Shrew
echo "Node22 (CHIMP, BONOBO):"
grep -o "node22" MNM_Removal/$1_MNMlist.txt | wc -l

#echo "Node24 (CHIMP, BONOBO):"
#grep -o "node24" MNM_Removal/$1_MNMlist.txt | wc -l

echo "HUMAN:"
grep -o "HUMAN" MNM_Removal/$1_MNMlist.txt | wc -l

# No TREE SHREW
echo "Node21 (CHIMP, HUMAN):"
grep -o "node21" MNM_Removal/$1_MNMlist.txt | wc -l

# No BONOBO
#echo "Node22 (CHIMP, HUMAN):"
#grep -o "node22" MNM_Removal/$1_MNMlist.txt | wc -l

#echo "Node23 (HUMAN, CHIMP, BONOBO):"
#grep -o "node23" MNM_Removal/$1_MNMlist.txt | wc -l

echo "GORILLA:"
grep -o "GORILLA" MNM_Removal/$1_MNMlist.txt | wc -l

# No TREE SHREW
echo "Node20 (GORILLA, CHIMP, HUMAN):"
grep -o "node20" MNM_Removal/$1_MNMlist.txt | wc -l

# No BONOBO
#echo "Node21 (GORILLA, CHIMP, HUMAN):"
#grep -o "node21" MNM_Removal/$1_MNMlist.txt | wc -l

#echo "Node22 (GORILLA, HUMAN, CHIMP, BONOBO):"
#grep -o "node22" MNM_Removal/$1_MNMlist.txt | wc -l

echo "ORANGUTAN:"
grep -o "ORANGUTAN" MNM_Removal/$1_MNMlist.txt | wc -l

# No TREE SHREW
echo "Node19 (ORANGUTAN, GORILLA, CHIMP, HUMAN):"
grep -o "node19" MNM_Removal/$1_MNMlist.txt | wc -l

# No BONOBO
#echo "Node20 (ORANGUTAN, GORILLA, CHIMP, HUMAN):"
#grep -o "node20" MNM_Removal/$1_MNMlist.txt | wc -l

#echo "Node21 (ORANGUTAN, GORILLA, HUMAN, CHIMP, BONOBO):"
#grep -o "node21" MNM_Removal/$1_MNMlist.txt | wc -l

echo "MACAQUE:"
grep -o "MACAQUE" MNM_Removal/$1_MNMlist.txt | wc -l

# No TREE SHREW
echo "Node18 (MACAQUE, ORANGUTAN, GORILLA, CHIMP, HUMAN):"
grep -o "node18" MNM_Removal/$1_MNMlist.txt | wc -l

# No BONOBO
#echo "Node19 (MACAQUE, ORANGUTAN, GORILLA, CHIMP, HUMAN):"
#grep -o "node19" MNM_Removal/$1_MNMlist.txt | wc -l

#echo "Node20 (MACAQUE, ORANGUTAN, GORILLA, HUMAN, CHIMP, BONOBO):"
#grep -o "node20" MNM_Removal/$1_MNMlist.txt | wc -l

echo "MARMOSET:"
grep -o "MARMOSET" MNM_Removal/$1_MNMlist.txt | wc -l

# No TREE SHREW
echo "Node17 (MARMOSET, MACAQUE, ORANGUTAN, GORILLA, CHIMP, HUMAN):"
grep -o "node17" MNM_Removal/$1_MNMlist.txt | wc -l

# No BONOBO
#echo "Node18 (MARMOSET, MACAQUE, ORANGUTAN, GORILLA, CHIMP, HUMAN):"
#grep -o "node18" MNM_Removal/$1_MNMlist.txt | wc -l

#echo "Node19 (MARMOSET, MACAQUE, ORANGUTAN, GORILLA, HUMAN, CHIMP, BONOBO):"
#grep -o "node19" MNM_Removal/$1_MNMlist.txt | wc -l

#echo "TREE SHREW:"
#grep -o "TREE_SHREW" MNM_Removal/$1_MNMlist.txt | wc -l

# No BONOBO
#echo "Node17 (TREE_SHREW, MARMOSET, MACAQUE, ORANGUTAN, GORILLA, CHIMP, HUMAN):"
#grep -o "node18" MNM_Removal/$1_MNMlist.txt | wc -l

#echo "Node17 (TREE_SHREW, MARMOSET, MACAQUE, ORANGUTAN, GORILLA, HUMAN, CHIMP, BONOBO):"
#grep -o "node18" MNM_Removal/$1_MNMlist.txt | wc -l

echo "COW:"
grep -o "COW" MNM_Removal/$1_MNMlist.txt | wc -l

echo "SHEEP:"
grep -o "SHEEP" MNM_Removal/$1_MNMlist.txt | wc -l

# No BONOBO / No TREE_SHREW
echo "Node27 (COW, SHEEP):"
grep -o "node27" MNM_Removal/$1_MNMlist.txt | wc -l

#echo "Node29 (COW, SHEEP):"
#grep -o "node29" MNM_Removal/$1_MNMlist.txt | wc -l

echo "PIG:"
grep -o "PIG" MNM_Removal/$1_MNMlist.txt | wc -l

# No BONOBO / No TREE_SHREW
echo "Node26 (PIG, COW, SHEEP):"
grep -o "node26" MNM_Removal/$1_MNMlist.txt | wc -l

#echo "Node28 (PIG, COW, SHEEP):"
#grep -o "node28" MNM_Removal/$1_MNMlist.txt | wc -l

echo "DOG:"
grep -o "DOG" MNM_Removal/$1_MNMlist.txt | wc -l

# No BONOBO / No TREE_SHREW
echo "Node25 (DOG, PIG, COW, SHEEP):"
grep -o "node25" MNM_Removal/$1_MNMlist.txt | wc -l

#echo "Node27 (DOG, PIG, COW, SHEEP):"
#grep -o "node27" MNM_Removal/$1_MNMlist.txt | wc -l

echo "HORSE:"
grep -o "HORSE" MNM_Removal/$1_MNMlist.txt | wc -l

echo "BAT:"
grep -o "BAT" MNM_Removal/$1_MNMlist.txt | wc -l

# No BONOBO / No TREE_SHREW
echo "Node28 (HORSE, BAT):"
grep -o "node28" MNM_Removal/$1_MNMlist.txt | wc -l

#echo "Node30 (HORSE, BAT):"
#grep -o "node30" MNM_Removal/$1_MNMlist.txt | wc -l

# No BONOBO / No TREE_SHREW
echo "Node26 (HORSE, BAT, DOG, PIG, COW, SHEEP):"
grep -o "node26" MNM_Removal/$1_MNMlist.txt | wc -l

#echo "Node26 (HORSE, BAT, DOG, PIG, COW, SHEEP):"
#grep -o "node26" MNM_Removal/$1_MNMlist.txt | wc -l

