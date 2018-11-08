#!/bin/bash

mkdir $1
mv $1* $1/
cp BRCC3/wag.dat $1/
cp ../Codeml/$1/tree_species.txt $1/
cp BRCC3/BRCC3_aaML.ctl $1/
mv $1/BRCC3_aaML.ctl $1/$1_aaML.ctl
sed -i '' -e "s/BRCC3/$1/g" $1/$1_aaML.ctl
touch $1/$1_tree.txt
