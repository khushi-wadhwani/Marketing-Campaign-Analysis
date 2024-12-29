#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 16:41:12 2024

@author: khushiwadhwani
"""
# Loading and Importing Libraries
import pandas as pd

pip install matplotlib
pip install seaborn 

import matplotlib.pyplot as plt
import seaborn as sns

file_path = '/Users/khushiwadhwani/desktop/cleaned_marketing_campaign_dataset.csv'

df = pd.read_csv(file_path)

print(df.head())

# Average ROI by Campaign_Type for Fashiontas

norm = plt.Normalize(grouped_df['ROI'].min(), grouped_df['ROI'].max())  
cmap = plt.get_cmap("YlGnBu") 


plt.figure(figsize=(10, 6))
ax = sns.barplot(x='Campaign_Type', y='ROI', data=grouped_df, palette=cmap(norm(grouped_df['ROI'])))


for p in ax.patches:
    ax.annotate(f'{p.get_height():,.2f}',  
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='center', fontsize=12, color='black',  
                xytext=(0, 5), textcoords='offset points')  

plt.title('Average ROI by Campaign Type for Fashionistas')
plt.xlabel('Campaign Type')
plt.ylabel('Average ROI')

plt.show()

# Average ROI by Campaign_Type for Tech Entusiasts
 
norm2 = plt.Normalize(grouped_df2['ROI'].min(), grouped_df2['ROI'].max())  
cmap2 = plt.get_cmap("YlGnBu") 

plt.figure(figsize=(10, 6))
ax = sns.barplot(x='Campaign_Type', y='ROI', data=grouped_df2, palette=cmap2(norm2(grouped_df2['ROI'])))

for p in ax.patches:
    ax.annotate(f'{p.get_height():,.2f}', 
                (p.get_x() + p.get_width() / 2., p.get_height()),  
                ha='center', va='center', fontsize=12, color='black',  

plt.title('Average ROI by Campaign Type for Tech Enthusiasts')
plt.xlabel('Campaign Type')
plt.ylabel('Average ROI')

plt.show()


# Clicks and Impressions by Campaign type for Fashionistas


filtered_df3 = df[df['Customer_Segment'] == 'Fashionistas'][['Campaign_Type', 'Clicks', 'Impressions']]

grouped_df3 = filtered_df3.groupby('Campaign_Type')[['Clicks', 'Impressions']].sum().reset_index()

grouped_df3 = grouped_df3.melt(id_vars='Campaign_Type', value_vars=['Clicks', 'Impressions'], var_name='Metric', value_name='Sum')


grouped_df3 = grouped_df3.sort_values(by='Sum', ascending=True)

plt.figure(figsize=(12, 8)) 

ax = sns.barplot(x='Campaign_Type', y='Sum', hue='Metric', data=grouped_df3)

for p in ax.patches:
    ax.annotate(f'{p.get_height():,.2f}',  
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='center', fontsize=12, color='black', 
                xytext=(0, 5), textcoords='offset points')  

plt.title('Sum of Clicks and Impressions by Campaign Type for Fashionistas')
plt.xlabel('Campaign Type')
plt.ylabel('Sum')

plt.legend(title='Metric', loc='upper left', bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.show()


# Clicks and Impressions by Campaign type for Tech Enthusiasts


filtered_df4 = df[df['Customer_Segment'] == 'Tech Enthusiasts'][['Campaign_Type', 'Clicks', 'Impressions']]

grouped_df4 = filtered_df4.groupby('Campaign_Type')[['Clicks', 'Impressions']].sum().reset_index()

grouped_df4 = grouped_df4.melt(id_vars='Campaign_Type', value_vars=['Clicks', 'Impressions'], var_name='Metric', value_name='Sum')

grouped_df4 = grouped_df4.sort_values(by='Sum', ascending=True)

plt.figure(figsize=(12, 8)) 

ax = sns.barplot(x='Campaign_Type', y='Sum', hue='Metric', data=grouped_df4)

for p in ax.patches:
     ax.annotate(f'{p.get_height():,.2f}', 
                 (p.get_x() + p.get_width() / 2., p.get_height()), 
                 ha='center', va='center', fontsize=12, color='black',  
                 xytext=(0, 5), textcoords='offset points')  

plt.title('Sum of Clicks and Impressions by Campaign Type for Tech Enthusiasts')
plt.xlabel('Campaign Type')
plt.ylabel('Sum')

plt.legend(title='Metric', loc='upper left', bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.show()

# Engagement Score for each Campaign Type - Fashionistas (Pie Chart)


norm4 = plt.Normalize(avg_engagement_by_campaign.min(), avg_engagement_by_campaign.max())
cmap4 = plt.get_cmap("YlGnBu") 


colors = [cmap4(norm4(score)) for score in avg_engagement_by_campaign]


plt.figure(figsize=(8, 8))
plt.pie(avg_engagement_by_campaign, 
        labels=avg_engagement_by_campaign.index, 
        autopct='%1.1f%%', 
        startangle=90, 
        colors=colors)

plt.title('Average Engagement Score by Campaign Type (Fashionistas)')
plt.axis('equal')  

# Engagement Score for each Campaign Type - Tech enthusiasts (Pie Chart)
norm5 = plt.Normalize(avg_engagement_by_campaign2.min(), avg_engagement_by_campaign2.max())
cmap5 = plt.get_cmap("YlGnBu")  
colors2 = [cmap5(norm5(score)) for score in avg_engagement_by_campaign2]

plt.figure(figsize=(8, 8))
plt.pie(avg_engagement_by_campaign2, 
        labels=avg_engagement_by_campaign2.index, 
        autopct='%1.1f%%', 
        startangle=90, 
        colors=colors2)

plt.title('Average Engagement Score by Campaign Type (Tech Enthusiasts)')
plt.axis('equal')  
plt.show()

# Average ROI by Campaign Type over different durations for Fashionistas

fashionistas_df2 = df[df['Customer_Segment'] == 'Fashionistas']

avg_roi_by_campaign_duration = fashionistas_df2.groupby(['Campaign_Type', 'Duration (in days)'])['ROI'].mean().reset_index()


plt.figure(figsize=(10, 6))
sns.lineplot(x='Duration (in days)', y='ROI', hue='Campaign_Type', data=avg_roi_by_campaign_duration, marker='o')

plt.title('Average ROI by Campaign Type over Different Durations (Fashionistas)')
plt.xlabel('Duration (in days)')
plt.ylabel('Average ROI')

plt.legend(title='Campaign Type', loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout()

plt.show()

# Average ROI by Campaign Type over different durations for Tech Enthusiasts

tech_df2 = df[df['Customer_Segment'] == 'Tech Enthusiasts']

avg_roi_by_campaign_duration_tech = tech_df2.groupby(['Campaign_Type', 'Duration (in days)'])['ROI'].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.lineplot(x='Duration (in days)', y='ROI', hue='Campaign_Type', data=avg_roi_by_campaign_duration_tech, marker='o')

plt.title('Average ROI by Campaign Type over Different Durations (Tech Enthusiasts)')
plt.xlabel('Duration (in days)')
plt.ylabel('Average ROI')

plt.legend(title='Campaign Type', loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout()

plt.show()

