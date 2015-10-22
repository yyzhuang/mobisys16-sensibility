import sys
import datetime

def header():
  return '''<?xml version="1.0" encoding="UTF-8"?>
<gpx version="1.0">
<name>Example gpx, see https://wiki.openstreetmap.org/wiki/GPX</name>
<wpt lat="48.08" lon="16.30">
<ele>160</ele>
<name>Mailman</name>
</wpt>
<trk><name>Example gpx</name><number>1</number><trkseg>
'''


def footer():
  return '''</trkseg></trk>
</gpx>
'''

print header()

linecount = 0
for line in sys.stdin.readlines():
  linecount += 1
  line.strip()
  try:
    lat, lon, alt, ts = line.split()
  except:
    print >>sys.stderr, "Error in line", linecount, line
    continue
  timestamp = datetime.datetime.fromtimestamp(int(ts))
  print '<trkpt lat="' + lat + '" lon="' + lon + '">' + \
      "<ele>" + alt + "</ele><time>" + \
      timestamp.isoformat() + "Z" + "</time></trkpt>"

print footer()

