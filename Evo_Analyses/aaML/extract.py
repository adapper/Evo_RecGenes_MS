# Extract branch lengths from aaML mlc files.
# python extract.py GENE > GENE_vector.txt


import sys
import re
import pandas as pd

g = sys.argv[1]

with open ('%s_tree.txt' % (g)) as file:
	file_contents = file.read()
	#print(file_contents)

	test = file_contents.split(':')
	test = test[1:]
	
	print(g)
	for i in range(len(test)):
		value = re.sub("[^0-9.]", "",test[i])
		print(value)

