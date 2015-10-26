# GPS Experiment

This directory contains a GPS experiment (aka "mailman trace") recorded 
using a Sony Tablet S. The raw data are contained in `mailman.raw`. The 
columns are space-separated, and contain latitude (in degrees), longitude 
(in degrees), elevation (aka altitude, in meters), and a Unix timestamp 
(in seconds since 1970-01-01, 00:00:00).

To plot data using OpenLayers / OpenStreetMap later on, we convert 
them to [GPX format](https://en.wikipedia.org/wiki/GPS_Exchange_Format) 
using the script `spacesep_to_gpx.py`. As the name indicates, this script 
reads in space-separated data like the `mailman` trace, and converts it 
to a basic GPX file.

Using the `filter_*.py` scripts, a raw trace can be filtered down (e.g. 
so as to remove rows based on inter-data point timing, reduce the 
precision of data points, or a combination of both).

The filter scripts read in and output the raw data format as described. 
Thus, to create the other (filtered) GPX files in this dir, the pipeline 
was

```
<mailman.raw python filter_XYZ.py FILTER_ARGS | \
python spacesep_to_gpx.py > outfile_xyz.gpx
```

(Read from the raw `mailman` trace, filter by `XYZ` with suitable filter 
arguments, pipe through the GPX format converter, and output into file 
`outfile_xyz.gpy`)

