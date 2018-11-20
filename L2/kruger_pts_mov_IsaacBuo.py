# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 18:23:01 2018

@author: admin
"""

import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)





#function to make tuples of lat and lon
def coord (row):
    x = row["lon"]
    y = row["lat"]
    return (x,y)


#read file using pandas
df = pd.read_csv(r'C:\Users\admin\geopython\L2\Data\some_posts.csv',sep=',', encoding='latin1')

#creates field coordinates and populates with tuples using function "coord"

df ["coordinates"] = df.apply(coord,axis=1)

df["geometry"]= None

#progress check
df.head(5)

#createes geodataframe from dataframe df
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

#iterates over rows and populates geometry column with points..(runtime longer than using a function)
for index, row in df.iterrows():
    geo.loc[index,'geometry']=Point(row["lon"],row["lat"])
    
    
#progress check
geo.head()


#makes a copy of the dataframe without the column for coordinates as tuples
geo_out = geo[['lat', 'lon', 'timestamp','userid', 'geometry',]].copy()


geo_out = gpd.GeoDataFrame(geo_out,geometry="geometry")

out_file = r'C:\Users\admin\geopython\L2\Data\Kruger_posts.shp'

geo_out.to_file(out_file)

#visualisation
geo_out.plot()







#problem 3




geo_proj = geo.copy()

geo_proj.crs = from_epsg(32735)

geo.head(1)

geo_proj_grp = geo_proj.groupby('userid')

#progress check
geo_proj_grp.head(1)




#create new datafram movements
movements = gpd.GeoDataFrame()

movements.crs= from_epsg(32735)

movements["geometry"]=None

movements["userid"]=None

movements["Distance"]=None


from shapely.geometry import LineString

#iterates over grouped dataframe creating a temporary dataframe for each group
for userid, userid_df in geo_proj_grp:
    #print(userid_df)
   #path = userid.geometry.apply(lambda x:                 LineString(x.tolist()))
   temp_df = gpd.GeoDataFrame(userid_df)
   temp_df= temp_df.sort_values("timestamp")
   coord_list= temp_df['coordinates'].values.tolist() #creates list of coordinates in coordinates column
   if len (coord_list) >1:                            #for users who posted at more than one point
       path = LineString(coord_list)
       distance = path.length
   else:
       a=coord_list[0]                                  #for users who posted at one point
       #print (a)
       path = LineString([a,a])
       #distance = 0
       distance = path.length
   movements=movements.append({"userid":userid, "geometry":path, "Distance":distance}, ignore_index=True)
   
   
#progress check 
movements.head(1)


#reassign movements to movements Geodataframe and assign crs
movements = gpd.GeoDataFrame(movements,geometry="geometry")

movements.crs= from_epsg(32735)



out_file = r'C:\Users\admin\geopython\L2\Data\some_movements.shp'

movements.to_file(out_file)

a= movements['Distance'].max()

print (a)

b= movements['Distance'].min()

print (b)

c= movements['Distance'].mean()

print (c)
   