import re
import matplotlib.pyplot as plt
import os
import math
import random
import numpy
import sys

directory = sys.argv[1]  # specify a subdir
g = 9.8  # gravity

def getz(file):
  zvalue = []
  with open(file) as f:
    for line in f:
      line = re.sub('[[]', '', line)
      line = re.sub('[]]', '', line).rstrip()
      x, y, z = line.split(",")
      #val = float(z) * abs(math.cos(random.expovariate(random.random())))
      val = float(z) * abs(math.cos(random.uniform(0, math.pi/2)))
      print z, val
      zvalue.append(val)
  return zvalue

def savedata(file, data):
  f = open(file, "w")
  f.write(str(data)) 
  f.close()
    
zup = getz(directory + '/acclogup.txt')
zdown = getz(directory + '/acclogdown.txt')

if len(zup) != len(zdown):
  print "zup and zdown should have the same size..."
  raise

sz = []
oz = []
for i in xrange(len(zup)):
 sz.append((zup[i] - zdown[i])/(2*g)) 
 oz.append((zup[i] + zdown[i])/2) 

#savedata(directory + '-sz-rand.txt', sz)
#savedata(directory + '-oz-rand.txt', oz)

print numpy.mean(sz)
print numpy.median(sz)
print numpy.std(sz)
print numpy.var(sz)
print 

print numpy.mean(oz)
print numpy.median(oz)
print numpy.std(oz)
print numpy.var(oz)


plt.scatter(sz, oz, c='yellow')
plt.show()
