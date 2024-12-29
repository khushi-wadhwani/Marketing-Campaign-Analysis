# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 14:36:06 2024

@author: louis
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the dataset
file_path = r'C:\Users\louis\OneDrive - Arizona State University\cleaned_marketing_campaign_dataset.csv'
df = pd.read_csv(file_path)

# General checks
print(df.columns)
print(df.head())

# Analysis and Visualizations

# Filter the DataFrame for 'Foodies' and 'Health & Wellness' segments
foodies_df = df[df['Customer_Segment'] == 'Foodies']
health_wellness_df = df[df['Customer_Segment'] == 'Health & Wellness']

# Calculate average ROI for each campaign type
foodies_roi = foodies_df.groupby('Campaign_Type')['ROI'].mean().sort_values()
health_wellness_roi = health_wellness_df.groupby('Campaign_Type')['ROI'].mean().sort_values()

# Plotting the bar chart for Foodies
plt.figure(figsize=(10, 6))
bars_foodies = foodies_roi.plot(kind='bar', color='skyblue', edgecolor='black')
plt.xlabel('Campaign Type')
plt.ylabel('ROI')
plt.title('Campaign Type vs ROI for Foodies')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Annotate the bars with the ROI values for Foodies
for bar in bars_foodies.patches:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() - 0.05,
             f'{bar.get_height():.2f}', ha='center', va='bottom', color='black')

plt.tight_layout()
plt.show()


# Plotting the bar chart for Health & Wellness
plt.figure(figsize=(10, 6))
bars_health_wellness = health_wellness_roi.plot(kind='bar', color='lightgreen', edgecolor='black')
plt.xlabel('Campaign Type')
plt.ylabel('ROI')
plt.title('Campaign Type vs ROI for Health & Wellness')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Annotate the bars with the ROI values for Health & Wellness
for bar in bars_health_wellness.patches:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() - 0.05,
             f'{bar.get_height():.2f}', ha='center', va='bottom', color='black')

plt.tight_layout()
plt.show()

# Calculate average values for each metric by campaign type
foodies_stats = foodies_df.groupby('Campaign_Type')[['Conversion_Rate', 'Clicks', 'Impressions']].mean()
health_wellness_stats = health_wellness_df.groupby('Campaign_Type')[['Conversion_Rate', 'Clicks', 'Impressions']].mean()

# Function to create side-by-side bar charts
def create_side_by_side_bar_chart(stats, segment_name):
    metrics = ['Conversion_Rate', 'Clicks', 'Impressions']
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    bar_width = 0.35

    for i, metric in enumerate(metrics):
        index = np.arange(len(stats))
        axes[i].bar(index, stats[metric], bar_width, color='skyblue', edgecolor='black')

        axes[i].set_xlabel('Campaign Type')
        axes[i].set_ylabel(metric)
        axes[i].set_title(f'{metric} by Campaign Type ({segment_name})')
        axes[i].set_xticks(index)
        axes[i].set_xticklabels(stats.index, rotation=45)

        # Annotate bars with their values
        for bar in axes[i].patches:
            height = bar.get_height()
            axes[i].annotate(f'{height:.2f}', xy=(bar.get_x() + bar.get_width() / 2, height),
                             xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=9, color='black')

    plt.tight_layout()
    plt.show()
# Create side-by-side bar charts for Foodies
create_side_by_side_bar_chart(foodies_stats, 'Foodies')

# Create side-by-side bar charts for Health & Wellness
create_side_by_side_bar_chart(health_wellness_stats, 'Health & Wellness')

# Function to create pie charts
def create_pie_chart(stats, segment_name):
    stats.plot(kind='pie', y='Engagement_Score', autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors, legend=False)
    plt.title(f'Engagement Score by Channel Used ({segment_name})')
    plt.ylabel('')  # Remove the y-label
    plt.tight_layout()
    plt.show()

# Calculate total Engagement Score for each channel in Foodies segment
foodies_stats = foodies_df.groupby('Channel_Used')['Engagement_Score'].sum()

# Calculate total Engagement Score for each channel in Health & Wellness segment
health_wellness_stats = health_wellness_df.groupby('Channel_Used')['Engagement_Score'].sum()

# Create pie chart for Foodies
create_pie_chart(foodies_stats, 'Foodies')

# Create pie chart for Health & Wellness
create_pie_chart(health_wellness_stats, 'Health & Wellness')


# Convert the 'Duration (in days)' to a categorical variable to keep the order
df['Duration (in days)'] = pd.Categorical(df['Duration (in days)'], ordered=True)

# Group by Campaign Type and Duration, and calculate the average ROI
grouped_df = df.groupby(['Campaign_Type', 'Duration (in days)'])['ROI'].mean().unstack()

# Plotting the line chart
plt.figure(figsize=(12, 8))
for campaign_type in grouped_df.index:
    plt.plot(grouped_df.columns, grouped_df.loc[campaign_type], marker='o', label=campaign_type)

plt.xlabel('Duration (in days)')
plt.ylabel('Average ROI')
plt.title('Average ROI by Campaign Type and Duration')
plt.legend(title='Campaign Type')
plt.grid(True)
plt.tight_layout()
plt.show()


# Function to create scatter plots
def create_scatter_plots(df, segment_name):
    plt.figure(figsize=(15, 5))
    
    # Scatter plot for Conversion Rate
    plt.subplot(1, 3, 1)
    sns.scatterplot(data=df, x='Campaign_Type', y='Conversion_Rate', hue='Campaign_Type', palette='viridis')
    plt.title(f'Conversion Rate vs Campaign Type for {segment_name}')
    plt.xticks(rotation=45)
    plt.legend([],[], frameon=False)
    
    # Scatter plot for Clicks
    plt.subplot(1, 3, 2)
    sns.scatterplot(data=df, x='Campaign_Type', y='Clicks', hue='Campaign_Type', palette='viridis')
    plt.title(f'Clicks vs Campaign Type for {segment_name}')
    plt.xticks(rotation=45)
    plt.legend([],[], frameon=False)
    
    # Scatter plot for Impressions
    plt.subplot(1, 3, 3)
    sns.scatterplot(data=df, x='Campaign_Type', y='Impressions', hue='Campaign_Type', palette='viridis')
    plt.title(f'Impressions vs Campaign Type for {segment_name}')
    plt.xticks(rotation=45)
    plt.legend([],[], frameon=False)
    
    plt.tight_layout()
    plt.show()

# Create scatter plots for Foodies
create_scatter_plots(foodies_df, 'Foodies')

# Create scatter plots for Health & Wellness
create_scatter_plots(health_wellness_df, 'Health & Wellness')