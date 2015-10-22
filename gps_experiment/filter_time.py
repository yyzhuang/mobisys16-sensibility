import sys

try:
  min_spacing = int(sys.argv[1])
except:
  print "filter_time complains:"
  print "Please provide an integer MIN_SPACING (in seconds) as the single command-line arg!"
  sys.exit(1)

linecount = 0
last_ts = 0
for line in sys.stdin.readlines():
  linecount += 1
  line.strip()
  try:
    lat, lon, alt, ts = line.split()
  except:
    print >>sys.stderr, "Error in line", linecount, line
    continue
  if int(ts) - last_ts > min_spacing:
    print lat, lon, alt, ts
    last_ts = int(ts)

