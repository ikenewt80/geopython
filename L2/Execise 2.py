# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 20:18:26 2018

@author: admin
"""

import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


#read file using pandas

df = pd.read_csv(r'C:\Users\admin\geopython\L2\Data\some_posts.csv',sep=',', encoding='latin1')

df["geometry"]= None


geo = gpd.GeoDataFrame(df,geometry="geometry")

from fiona.crs import from_epsg

geo.crs = from_epsg(4326)




# function to create points per row
#def point(row):
   # latitude = row["lat"]
   # longitude = row["lon"]
   # return Point(latitude,longitude)

#populates geometry column with 
#df["geometry"] = df.apply(point,axis=1)

#progress check
#df.head()

#iterates over rows and populates geometry column with points......runtime long
for index, row in df.iterrows():
    geo.loc[index,'geometry']=Point(row["lat"],row["lon"])
    
    
#progress check
geo.head()

out_file = r'C:\Users\admin\geopython\L2\Data\Kruger_posts.shp'

geo.to_file(out_file)

geo.plot()

#problem 3




geo_proj = geo.copy()

geo_proj.crs = from_epsg(32735)

geo.head(1)

for index, row in geo_proj.iterrows():
    geo_proj.loc[index,'coordinates']=(row["lat"],row["lon"])

geo_proj_grp = geo_proj.groupby('userid')

geo_proj_grp.head(1)




#create new datafram movements
movements = gpd.GeoDataFrame()

movements.crs= from_epsg(32735)

movements["geometry"]=None

movements["userid"]=None

from shapely.geometry import LineString


for userid, userid_df in geo_proj_grp:
    for 
    #print(userid_df)
   #path = userid.geometry.apply(lambda x:                 LineString(x.tolist()))
   temp_df = gpd.GeoDataFrame(userid_df)
   temp_df= temp_df.sort_values("timestamp")
   
   
   #temp_df =temp_df['geometry'].apply(lambda x:                 LineString(x.tolist()))
   temp_df= temp_df['geometry'].values.tolist()
   temp_df = LineString(temp_df)
   
   
   
    #pd.to_datetime(["timestamp"], format="%Y%m%d %H:%M").sort_values()
   # print(["geometry"])
    path= column["]
    print (path)
    

