# Raster2xyz
Alternative and faster (vectorized) version of gdal2xyz.py (https://svn.osgeo.org/gdal/trunk/gdal/swig/python/scripts/gdal2xyz.py)

Builded on top of GDAL, Numpy and Pandas.

## Install
```
$ pip install .
```

## Usage
### Command Line
```
$ raster2xyz [-h] input_raster out_csv

positional arguments:
  input_raster  input_raster filepath
  out_csv       out_csv filepath

optional arguments:
  -h, --help    show this help message and exit
```
### Importing module
```
from raster2xyz.raster2xyz import Raster2xyz

input_raster = "input_raster.tif"
out_csv = "/tmp/out_xyz.csv"

rtxyz = Raster2xyz()
rtxyz.translate(input_raster, out_csv)
```
## Requirements
- Numpy: http://www.numpy.org/
- Pandas: http://pandas.pydata.org/
- GDAL: http://www.gdal.org/


## About author
Developed by Cayetano Benavent.
GIS Analyst at Geographica.

http://www.geographica.gs


## License
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.
