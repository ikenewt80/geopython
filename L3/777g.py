# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 09:48:00 2018

@author: admin
"""

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as pt

f_path = r"C:\Users\admin\geopython\L4\E4\dataE4\TravelTimes_to_5975373_Forum.csv"

shp_path = r"C:\Users\admin\geopython\L4\E4\dataE4\MetropAccess_YKR_grid_EurefFIN.shp"

data = pd.read_csv(f_path,sep=',',encoding='latin1')
#(fp_cl,sep=';',encoding='latin1')

#progress check
#data.head(5)

data.columns

#sel_cols = ["pt_r_tt","car_r_t","from_id","to_id"]
#selected_cols = ['pt_r_tt','car_r_t','from_id','to_id']

#data = data [selected_cols]

data = data[['pt_r_tt', 'car_r_t', 'from_id','to_id']].copy()

#rename columns pt_r_tt and Car_r_t

data.rename(columns={'pt_r_tt':'public_trans','car_r_t':'car',}, inplace=True)

#progress check
data.head(5)

poly_shp = gpd.read_file(shp_path)

poly_shp.head()



merged = pd.merge(data,poly_shp,how="inner",left_on="from_id",right_on='YKR_ID')

merged.head()


import pysal as ps

#create classifier
classifier = ps.Equal_Interval.make(k=5)

#apply classes to both modes of transportation
merged['public_trans_classes'] = merged[['public_trans']].apply(classifier)


merged['car_classes'] = merged[['car']].apply(classifier)


merged.head()


import matplotlib.pyplot as pt
import geopandas as gpd



poly_shp.plot()

merged.plot(column="car_classes", linewidth=0, legend=True);