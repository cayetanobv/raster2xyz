Raster2xyz
==========

|Build Status| |PyPI version| |Python versions|

Alternative and faster (vectorized) version of gdal2xyz.py
(https://svn.osgeo.org/gdal/trunk/gdal/swig/python/scripts/gdal2xyz.py)

Builded on top of GDAL, Numpy and Pandas.

-  input file: `geotiff <https://en.wikipedia.org/wiki/GeoTIFF>`__
-  output file: `ASCII Gridded
   XYZ <http://www.gdal.org/frmt_xyz.html>`__

Install
-------

Install from `PYPI <https://pypi.python.org/pypi/raster2xyz>`__:

::

    $ pip install raster2xyz

Usage
-----

Command Line
~~~~~~~~~~~~

.. code:: bash

    $ raster2xyz [-h] input_raster out_csv

    positional arguments:
      input_raster  input_raster filepath
      out_csv       out_csv filepath

    optional arguments:
      -h, --help    show this help message and exit

Importing module
~~~~~~~~~~~~~~~~

.. code:: python

    from raster2xyz.raster2xyz import Raster2xyz

    input_raster = "input_raster.tif"
    out_csv = "/tmp/out_xyz.csv"

    rtxyz = Raster2xyz()
    rtxyz.translate(input_raster, out_csv)

Requirements
------------

-  Numpy: http://www.numpy.org/
-  Pandas: http://pandas.pydata.org/
-  GDAL: http://www.gdal.org/

About author
------------

Developed by Cayetano Benavent. GIS Analyst at Geographica.

http://www.geographica.gs

License
-------

This program is free software; you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the
Free Software Foundation; either version 2 of the License, or (at your
option) any later version.

.. |Build Status| image:: https://travis-ci.org/cayetanobv/raster2xyz.svg?branch=master
   :target: https://travis-ci.org/cayetanobv/raster2xyz
.. |PyPI version| image:: https://badge.fury.io/py/raster2xyz.svg
   :target: https://badge.fury.io/py/raster2xyz
.. |Python versions| image:: https://img.shields.io/pypi/pyversions/raster2xyz.svg?maxAge=2592000
   :target: https://pypi.python.org/pypi/raster2xyz
