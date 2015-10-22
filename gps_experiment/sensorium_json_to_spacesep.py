import sys
import json

data = sys.stdin.read()
pointslist = json.loads(data)

for p in pointslist:
  timestamp = int(p["timestamp"]) / 1000
  print p["latitude"], p["longitude"], int(float(p["altitude"])), timestamp
