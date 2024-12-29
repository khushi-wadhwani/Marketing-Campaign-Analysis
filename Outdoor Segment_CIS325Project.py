#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 10:36:10 2024

@author: angelaaparicio
"""

import pandas as pd
file_path = '/Users/angelaaparicio/Downloads/cleaned_marketing_campaign_dataset.csv' 
df = pd.read_csv(file_path)  
df

#Outdoor Segment 
outdoor = df[df['Customer_Segment'] == 'Outdoor Adventurers'] 

#ROI by Campaign Type
grouped_c = outdoor.groupby('Campaign_Type')[['ROI']].mean().reset_index()
print(grouped_c) 

#Bar Graph 
import numpy as np
import matplotlib.pyplot as plt
plt.figure(figsize=(5,6)) 
bars = plt.bar(grouped_c ['Campaign_Type'], grouped_c['ROI']) 
plt.title('Average ROI by Campaign Type-Outdoor')
plt.xlabel('Campaign Type')
plt.ylabel('Average ROI') 
plt.ylim(4.8,5.1) 
y_ticks = np.arange(4.8,5.1,0.1) 
plt.yticks(y_ticks) 

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height, 
             f'{height:.2f}',
             ha='center',
             va='bottom',
             fontsize=10,
             color='black') 
plt.show()  
plt.savefig('roi_by_campaign_type.pdf')  

#Coversion rate by clicks & impressions
grouped_cr = outdoor.groupby ('Campaign_Type').agg({'Clicks':'mean', 
                                                    'Impressions': 'mean',
                                                    'ROI':'mean'}).reset_index() 
grouped_cr  
#Double Bar Graph
fig, ax1 = plt.subplots(figsize=(10, 6))
width = 0.35
x = np.arange(len(grouped_cr))
bars1 = ax1.bar(x - width/2, grouped_cr['Clicks'], width, label='Clicks', color='b')
ax2 = ax1.twinx()
bars2 = ax2.bar(x + width/2, grouped_cr['Impressions'], width, label='Impressions', color='g')


ax1.set_xlabel('Campaign Type')
ax1.set_ylabel('Clicks', color='b')
ax2.set_ylabel('Impressions', color='g')
ax1.set_title('Clicks and Impressions by Campaign Type-Outdoor') 


ax1.set_xticks(x)
ax1.set_xticklabels(grouped_cr['Campaign_Type'], rotation=45)
ax1.set_yticks([544, 546, 548, 550, 552, 554, 556])
ax2.set_yticks([5440, 5460,5480, 5500, 5520, 5540, 5560]) 
ax1.set_ylim(544, 556)
ax2.set_ylim(5440, 5560)

for i in range(len(grouped_cr)):
    ax1.text(x[i] - width/2, grouped_cr['Clicks'][i] + 0.02, f'{grouped_cr["Clicks"][i]:.0f}', ha='center', va='bottom', fontsize=9)
    ax2.text(x[i] + width/2, grouped_cr['Impressions'][i] + 0.02, f'{grouped_cr["Impressions"][i]:.0f}', ha='center', va='bottom', fontsize=9)

ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.tight_layout()
plt.show() 

#Average ROI by campaign type & duration
grouped_cd = outdoor.groupby(['Campaign_Type', 'Duration (in days)']).agg({'ROI': 'mean'}).reset_index()

#Line graph 
plt.figure(figsize=(10,6))
for Campaign_Type in grouped_cd['Campaign_Type'].unique():
    campaign_data = grouped_cd[grouped_cd['Campaign_Type'] == Campaign_Type]
    plt.plot(campaign_data['Duration (in days)'], campaign_data['ROI'], label=Campaign_Type, marker='o')


plt.xlabel('Duration (days)')
plt.ylabel('Average ROI')
plt.title('Average ROI by Campaign Type and Duration-Outdoor')
plt.legend(title='Campaign Type')

plt.tight_layout()
plt.show() 

#Engagement Score by Channel Used 
grouped_es = outdoor.groupby('Channel_Used')[['Engagement_Score']].mean().reset_index()
total_engagement = grouped_es['Engagement_Score'].sum() 
grouped_es['Percentage'] = (grouped_es['Engagement_Score'] / total_engagement) * 100

#Pie Chart
plt.figure(figsize=(8, 8)) 

plt.pie(
    grouped_es['Percentage'], 
    labels=grouped_es['Channel_Used'], 
    autopct='%1.1f%%') 
    
plt.pie(grouped_es['Percentage'], labels=grouped_es['Channel_Used']) 
plt.title('Average Engagement Score by Channel for Outdoor') 
plt.show()



