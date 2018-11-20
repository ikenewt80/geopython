# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 11:11:32 2018

@author: admin
"""

#importing shapefile via geopandas
import geopandas as gpd

fp = r"C:\Users\admin\geopython\L2\Europe_borders\Europe_borders.shp"

data =gpd.read_file(fp)

data.crs

data["geometry"].head()

#making a copy of the data
data_proj =data.copy()

#project data to lambert projection

data_proj=data_proj.to_crs(epsg=3035)


data_proj["geometry"].head()


#visualising

import matplotlib.pyplot as plt

# Plot the WGS84
data.plot(facecolor='gray');

# Add title
plt.title("WGS84 CRS");

# Remove empty white space around the plot
plt.tight_layout()

# Plot the one with ETRS-LAEA projection
data_proj.plot(facecolor='blue');

# Add title
plt.title("ETRS Lambert Azimuthal Equal Area projection");

# Remove empty white space around the plot
plt.tight_layout()


# Ouput file path
out_fp = r"Data\Europe_borders_epsg3035.shp"

# Save to disk
data_proj.to_file(out_fp)


