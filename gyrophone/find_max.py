import sys

xmax, ymax, zmax = 0., 0., 0.

for line in sys.stdin.readlines():
  _, x, y, z = line.split()
  x, y, z = abs(float(x)), abs(float(y)), abs(float(z))
  xmax, ymax, zmax = max(xmax,x), max(ymax,y), max(zmax,z)

print xmax, ymax, zmax
