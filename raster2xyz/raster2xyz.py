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

import logging
import numpy as np
import pandas as pd
from osgeo import gdal


class Logger(object):

    def __init__(self, level=logging.INFO):
        logfmt = "[%(asctime)s - %(levelname)s] - %(message)s"
        dtfmt = "%Y-%m-%d %I:%M:%S"
        logging.basicConfig(level=level, format=logfmt, datefmt=dtfmt)

    def get(self):
        return logging.getLogger()

class Raster2xyz(object):

    def __init__(self, verbose=True):
        if not verbose:
            lg = Logger(level=logging.ERROR)
        else:
            lg = Logger()

        self.__logger = lg.get()

    def __geotrCoords(self, gtr, x, y):
        """
        """
        try:
            self.__logger.info("Getting geotransformed coordinates...")

            gtr_x = gtr[0] + (x + 0.5) * gtr[1] + (y + 0.5) * gtr[2]
            gtr_y = gtr[3] + (x + 0.5) * gtr[4] + (y + 0.5) * gtr[5]

            return(gtr_x, gtr_y)

        except Exception as err:
            self.__logger.error("Error getting geotransformed coordinates: {0}".format(err))

    def __getRasterData(self, input_raster, n_band):
        """
        """
        try:
            self.__logger.info("Getting geotransform and data...")

            src_raster = gdal.Open(input_raster)
            raster_bnd = src_raster.GetRasterBand(n_band)

            raster_values = raster_bnd.ReadAsArray()
            gtr = src_raster.GetGeoTransform()

            src_raster = None

            return(gtr, raster_values)

        except Exception as err:
            self.__logger.error("Error getting geotransform and data: {0}".format(err))

    def __getXyzData(self, raster_values, no_data):
        """
        """
        try:
            self.__logger.info("Getting XYZ data...")

            y, x = np.where(raster_values != no_data)
            data_vals = np.extract(raster_values != no_data, raster_values)

            return(x, y, data_vals)

        except Exception as err:
            self.__logger.error("Error getting XYZ data: {0}".format(err))

    def __buildXyzData(self, gtr_x, gtr_y, data_vals):
        """
        """
        try:
            self.__logger.info("Building XYZ data...")

            data_dict = {
                "x": gtr_x,
                "y": gtr_y,
                "z": data_vals
            }

            return pd.DataFrame(data_dict)

        except Exception as err:
            self.__logger.error("Error building XYZ data: {0}".format(err))

    def __toXYZ(self, out_xyz, dataframe, rnd):
        """
        """
        try:
            if rnd:
                rnd_x, rnd_y, rnd_z = rnd
                rnd_df = dataframe.round({'x': rnd_x, 'y': rnd_y, 'z': rnd_z})
                rnd_df.to_csv(out_xyz, index=False)
            else:
                dataframe.to_csv(out_xyz, index=False)

            self.__logger.info("New XYZ (csv file) created...")

        except Exception as err:
            self.__logger.error("Error creating XYZ file (csv): {0}".format(err))

    def translate(self, input_raster, out_xyz, no_data=-9999, n_band=1, rnd=None):
        """
        """
        gtr, raster_values = self.__getRasterData(input_raster, n_band)

        if not no_data:
            no_data = np.nan

        x, y, data_vals = self.__getXyzData(raster_values, no_data)

        gtr_x, gtr_y = self.__geotrCoords(gtr, x, y)

        df = self.__buildXyzData(gtr_x, gtr_y, data_vals)

        self.__toXYZ(out_xyz, df, rnd)
