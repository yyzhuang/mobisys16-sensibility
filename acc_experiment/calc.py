import re
import matplotlib.pyplot as plt
import os

g = 9.8  # gravity

zup = []
with open('acclogup.txt') as f:
  for line in f:
    line = re.sub('[[]', '', line)
    line = re.sub('[]]', '', line).rstrip()
    x, y, z = line.split(",")
    zup.append(float(z))

zdown = []
with open('acclogdown.txt') as f:
  for line in f:
    line = re.sub('[[]', '', line)
    line = re.sub('[]]', '', line).rstrip()
    x, y, z = line.split(",")
    zdown.append(float(z))

if len(zup) != len(zdown):
  print "something went wrong..."

sz = []
oz = []

for i in xrange(len(zup)):
 sz.append((zup[i] - zdown[i])/(2*g)) 
 oz.append((zup[i] + zdown[i])/2) 

f1 = open(os.getcwd().split('/')[-1] + '-sz.txt', "w")
f1.write(str(sz)) 
f1.close()

f2 = open(os.getcwd().split('/')[-1] + '-oz.txt', "w")
f2.write(str(oz)) 
f2.close()

plt.scatter(sz, oz, c='red')
plt.show()
