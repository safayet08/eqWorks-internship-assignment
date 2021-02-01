#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 13:11:56 2021

@author: safayet08
"""

import pandas as pd
import numpy as np
from helperFunction import distance

requestLogs = pd.read_csv('../Results/Cleanup/part-00000-d5ab735a-66f9-4928-bf38-1cb5418e33ee-c000.csv', 
                          header = None, index_col = 1)
poiList = pd.read_csv('../data/POIList.csv', index_col = 0)

requestLogs = requestLogs.reset_index()

columns = ['TimeSt', '_ID', 'Country', 'Province', 'City', 'Latitude', 'Longitude']

requestLogs.columns = columns


poi_Longitude_dict = dict()
poi_Latitude_dict = dict()
poi_number_dcit = dict()
for idx in range(len(requestLogs)):
    origin = (float(requestLogs.iloc[idx]['Latitude']), float(requestLogs.iloc[idx]['Longitude']))
    
    minimumDistance, resultIndex = 10e50, -1
    for poiIndex in range(len(poiList)):
        destination = (float(poiList.iloc[poiIndex]['Latitude']), float(poiList.iloc[poiIndex]['Longitude']))
        D = distance(origin, destination)
        if minimumDistance >= D:
            minimumDistance = D
            resultIndex = poiIndex  
            
    poi_number_dcit.update({idx: resultIndex})
    poi_Latitude_dict.update({idx : poiList.iloc[resultIndex]['Latitude']})
    poi_Longitude_dict.update({idx : poiList.iloc[resultIndex]['Longitude']})

requestLogs['POI_Number'] = poi_number_dcit.values()
requestLogs['POI_Latitude'] = poi_Latitude_dict.values()
requestLogs['POI_Longitude'] = poi_Longitude_dict.values()

requestLogs.to_csv('../Results/Label/POI_Assignment.csv', encoding='utf-8', index = False)
