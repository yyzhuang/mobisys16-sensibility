from pandas import *
import glob  
import os
import re

def savedata(subdir, filename):
  with open (subdir + '/' + filename, "r") as f:
    data = f.readlines()[0]
      
  data = re.sub('[[]', '', data)
  data = re.sub('[]]', '', data)
  floats = [float(x) for x in data.split(',')]
  return floats


def savecsv(x, y, filename):
  f = open(filename, "w")

  if len(x) != len(y):
    print "two arrays should have the same size..."
    raise

  for i in range(len(x)):
    f.write(str(x[i]) + ',' + str(y[i]) + '\n')
    
  f.close() 


for subdir in glob.glob("./*"):
  if os.path.isdir(subdir) and subdir != "./scripts":  
    # "./scripts" does not store data
    sz = savedata(subdir, '/sz-rand20.txt')
    oz = savedata(subdir, '/oz-rand20.txt')
    savecsv(sz, oz, subdir + '/sz-oz-rand20.csv')

    sz = savedata(subdir, '/sz-rand30.txt')
    oz = savedata(subdir, '/oz-rand30.txt')
    savecsv(sz, oz, subdir + '/sz-oz-rand30.csv')


