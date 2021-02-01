#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 14:53:28 2021

@author: safayet08
"""

import pandas as pd
import math
from helperFunction import distance
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

requestLogs = pd.read_csv('../Results/Label/POI_Assignment.csv', index_col = 1)
requestLogs = requestLogs.reset_index()

poiList = pd.read_csv('../data/POIList.csv', index_col = 0)

#------- Average and Standard Deviation of distances from origin to POI ------

Origin_to_POI__dict = dict()
for idx in range(len(requestLogs)):
    origin = (float(requestLogs.iloc[idx]['Latitude']), float(requestLogs.iloc[idx]['Longitude']))
    POI = (float(requestLogs.iloc[idx]['POI_Latitude']), float(requestLogs.iloc[idx]['POI_Longitude']))
    D = distance(origin, POI)
    Origin_to_POI__dict.update({idx : D})
        
requestLogs['Origin_to_POI'] = Origin_to_POI__dict.values()


#------- Circle with POI as center and calculating other metrics--------------

#------------------ Filtering our anomalous data -----------------------------
requestLogs = requestLogs[requestLogs['Origin_to_POI'] <= 500] 
#-----------------------

mapBBox = (-145, -40, 30, 70)


poiCluster = []
poi_numbers = requestLogs.POI_Number.max() - requestLogs.POI_Number.min() + 2
for i in range(poi_numbers):
    poiCluster.append([])
    
#------ Plotting each clusters--------------   
geoMap = plt.imread('Map.png')
fig, ax = plt.subplots(figsize = (20, 20)) 
ax.set_title('RequestLogs all over Canada')
ax.set_xlim(math.floor(mapBBox[0]), math.ceil(mapBBox[1]))
ax.set_ylim(math.floor(mapBBox[2]), math.ceil(mapBBox[3]))


colors = ['blue', 'lime', 'green', ]
colorIdx = -1

for i in range(poi_numbers + 1):
    currentPOI = requestLogs[requestLogs['POI_Number'] == i] 
    if len(currentPOI) > 0: 
        colorIdx = colorIdx + 1
        ax.scatter(currentPOI.Longitude, currentPOI.Latitude, zorder = 1, alpha = 0.2, 
                   c = colors[colorIdx], s = 1)
        ax.scatter(poiList.iloc[i]['Longitude'], poiList.iloc[i]['Latitude'], 
                   zorder = 1, alpha = 1, c = 'r', s = 25)
        
        average = currentPOI['Origin_to_POI'].mean()
        sd_deviation = currentPOI['Origin_to_POI'].std()      
        print('Average distance from reqestOrigin to POI : {}'.format(average))
        print('Standard Deviation of reqestOrigin from Origin to POI : {}'.format(sd_deviation))
        
        # Relevant section
        Width = (currentPOI.Longitude.max() - currentPOI.Longitude.min())
        Height = (currentPOI.Latitude.max() - currentPOI.Latitude.min())
        Radius = (60 * Height + 40 * Width + 20 * sd_deviation) / 200
        
        center = (currentPOI.Longitude.mean(), currentPOI.Latitude.mean())
        circle = Circle(center, Radius, edgecolor = 'r', fc = 'None', lw = 2)
        ax.add_patch(circle)
    
        
        area = 3.1416 * Radius * Radius
        totalRequests = len(currentPOI)
        requestPerArea = totalRequests / area
        print("Radius of the the POI: {}".format(Radius))
        print("Request/Area : {}".format(requestPerArea))
        print("\n\n")
        
        
        
fig.tight_layout()
ax.imshow(geoMap, zorder = 0, extent = mapBBox)
fig.savefig('../Results/Analysis/POIDistribution.png')




