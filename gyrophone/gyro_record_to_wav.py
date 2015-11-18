"""
@aaaaalbert's Python kind-of-port of the GyroPhone folks'
https://bitbucket.org/ymcrcat/gyrophone/src/aa816eec3d7a17d9e30ab7afa0d4b79ef0a7a82e/gyro_record_to_wav.m?at=master&fileviewer=file-view-default
"""
usage = """
Usage:
  THIS.py file_containing_samples basename_for_output_file \
      source_sample_rate XMAX YMAX ZMAX

Use `python find_max.py <file_containing_samples` to get the max values.
"""
import sys
import wave

SAMPLE_WIDTH = 2 # in bytes

try:
  inputfilename, basename, sample_rate, xmax, ymax, zmax = sys.argv[1:]
  sample_rate = int(sample_rate)
  maxima = float(xmax), float(ymax), float(zmax)
except Exception, e:
  print repr(e)
  print usage
  sys.exit(1)


# Open output files
f1 = wave.open(basename + "_x.wav", "w")
f2 = wave.open(basename + "_y.wav", "w")
f3 = wave.open(basename + "_z.wav", "w")

outfiles = [f1, f2, f3]

# Configure WAV output
for f in outfiles:
  f.setnchannels(1)
  f.setsampwidth(SAMPLE_WIDTH)
  f.setframerate(sample_rate)


# Actually output stuff
for line in open(inputfilename, "r").readlines():
  ts_ignore, x, y, z = line.split()
  data = float(x), float(y), float(z)
  for f,d,max in zip(outfiles, data, maxima):
    intval = int(d/max * 2**(8*SAMPLE_WIDTH-1))
    hi, lo = (intval & 0xff00) >> 8, intval & 0x00ff
    f.writeframesraw(chr(lo) + chr(hi))

for f in outfiles:
  f.close()

