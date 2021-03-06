import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob  
import os
import math

colors = ('b', 'g', 'r', 'c', 'm', 'k')
markers = ['D', 's', '^', 'd', 'h', '*', 'D', 'p', 'H', 'v', '8', '<', '>']
    
def plotfig(csvfile):
  devicenum = 0

  for subdir in glob.glob("./*"):
    if os.path.isdir(subdir) and subdir != "./scripts":  
      # "./scripts" does not store data
      print subdir
      devicenum += 1  

      for datafile in glob.glob(subdir + '/' + csvfile): 
        col_names = ["sz", "oz"]
        dtypes = ["float", "float"]
        data = np.genfromtxt(datafile, delimiter=',', 
                             names=col_names, dtype=dtypes)
        color = colors[devicenum % len(colors)]
        marker = markers[devicenum % len(markers)]
        sz = data['sz']
        oz = data['oz']
        plt.errorbar(np.mean(sz), np.mean(oz), xerr=np.std(sz), yerr=np.std(oz), 
                     linestyle='None', marker=marker, markersize=10, color=color)
        print np.mean(sz), np.mean(oz), np.std(sz), np.std(oz), marker, color

  plt.xlim([0.98, 1.055])   
  plt.ylim([-0.501, 0.901])
  plt.xlabel('Sz')
  plt.ylabel('Oz')
  plt.show()
  

plotfig("sz-oz.csv")
#plotfig("sz-oz-rand10.csv")
