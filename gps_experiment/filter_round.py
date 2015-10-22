import sys

try:
  accuracy = int(sys.argv[1])
except:
  print "filter_round complains:"
  print "Please provide an integer ACCURACY (in decimal digits) as the single command-line arg!"
  sys.exit(1)

linecount = 0
for line in sys.stdin.readlines():
  linecount += 1
  line.strip()
  try:
    lat, lon, alt, ts = line.split()
  except:
    print >>sys.stderr, "Error in line", linecount, line
    continue
  print round(float(lat), accuracy), round(float(lon), accuracy), alt, ts

