# -*- coding: utf-8 -*-
#
#  Author: Cayetano Benavent, 2015-2016.
#  cayetano.benavent@geographica.gs
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#

import argparse
from .raster2xyz import Raster2xyz


def run():
    descr = "Alternative and faster (vectorized) version of gdal2xyz.py"
    arg_parser = argparse.ArgumentParser(description=descr)

    arg_parser.add_argument('input_raster', type=str, help='input_raster filepath')
    arg_parser.add_argument('out_csv', type=str, help='out_csv filepath')

    args = arg_parser.parse_args()

    input_raster = args.input_raster
    out_csv = args.out_csv

    rtxyz = Raster2xyz()
    rtxyz.translate(input_raster, out_csv)
