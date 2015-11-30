import re
import matplotlib.pyplot as plt
import os
import math
import random
import numpy
import sys

directory = sys.argv[1]  # specify a subdir
g = 9.8  # gravity

def getz(line):
  line = re.sub('[[]', '', line)
  line = re.sub('[]]', '', line).rstrip()
  x, y, z = line.split(",")
  return float(z)


def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    i, p, d = s.partition('.')
    result = '.'.join([i, (d+'0'*n)[:n]])
    if n == 0:
        result = result + '0'  # otherwise, truncate(3.141592, 0) will return 3., not 3.0
    return float(result)


def gettruncz(file):
  zvalue = []
  with open(file) as f:
    for line in f:
      z = getz(line)
      #val = truncate(z, 0)
      val = z
      #print z, val
      zvalue.append(val)
  return zvalue


def getrandomz(file):
  zvalue = []
  with open(file) as f:
    for line in f:
      z = getz(line)
      #val = float(z) * abs(math.cos(random.expovariate(random.random())))
      val = z * abs(math.cos(random.uniform(0, math.pi/6)))
      print z, val
      zvalue.append(val)
  return zvalue


def savedata(file, data):
  f = open(file, "w")
  f.write(str(data)) 
  f.close()
    
zup = getrandomz(directory + '/up.txt')
zdown = getrandomz(directory + '/down.txt')

if len(zup) != len(zdown):
  print "zup and zdown should have the same size..."
  raise

sz = []
oz = []
for i in xrange(len(zup)):
 sz.append((zup[i] - zdown[i])/(2*g)) 
 oz.append((zup[i] + zdown[i])/2) 

savedata(directory + '/sz-rand30.txt', sz)
savedata(directory + '/oz-rand30.txt', oz)

print numpy.mean(sz)
print numpy.median(sz)
print numpy.std(sz)
print numpy.var(sz)
print 

print numpy.mean(oz)
print numpy.median(oz)
print numpy.std(oz)
print numpy.var(oz)

#plt.scatter(sz, oz, c='yellow')
#plt.show()
