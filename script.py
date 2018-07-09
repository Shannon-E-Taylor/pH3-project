#! usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import math

#########
#GLOBALS#
#########

#open file and read into mat 
file = 'data/Statistics for C1-Image0001.oif redirect to C2-Image0001.csv'
f = open(file, "rb")
mat = np.genfromtxt(f, delimiter = ",", names = True)
f.close()

col=[]
d=mat['IntDen'] #intensity column
for i in d: 
	try: 
		col.append(math.log(i))
	except ValueError: 
		col.append(i)



#validation plots
xy = plt.scatter(mat['X'], mat['Y'], c=col) #2D diagram of nuclei w pH3 intenstity

h = plt.hist(d, bins = 50, log = True) #histogram of pH3 intensity- check cutoff is ok with data





