# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 01:39:13 2018

@author: admin
"""

import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, Polygon
import fiona

#creates a new empty geodataframe
newdata= gpd.GeoDataFrame()

#checks the new data created
newdata

#creates an empty column in the dataframe
newdata["geometry"] = None

#checks the new data created
newdata

coordinates = [(24.950899, 60.169158), (24.953492, 60.169158), (24.953510, 60.170104), (24.950958, 60.169990)]

poly = Polygon(coordinates)
 
type(poly)


# populates the fisrts index of the geometry column with poly
newdata.loc[0, 'geometry'] = poly

#checks the new data created
newdata

#adds new column and inserts name of poly
newdata.loc[0, 'Location'] = 'Helsinki Senate Square'

# Import specific function 'from_epsg' from fiona module to define crs
from fiona.crs import from_epsg

newdata.crs = from_epsg(4326)

newdata.crs

out_file = r"C:\Users\admin\geopython\L2\Data\Senaatintori.shp"

newdata.to_file(out_file)
