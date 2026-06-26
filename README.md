# Zomato Bangalore Restaurant Analysis 

## Project Overview
Exploratory Data Analysis on the Zomato Bangalore Restaurants dataset 
using Python (pandas) for data cleaning and Tableau for visualization.

## Dataset
- Raw data: 51,717 rows, 17 columns
- After cleaning: 41,263 rows, 12 columns

## Tools Used
- Python (pandas) — data cleaning
- Tableau Public — data visualization

## Data Cleaning Steps
- Dropped irrelevant columns (url, phone, dish_liked, menu_item)
- Cleaned rate column — removed '/5' and converted to float
- Cleaned cost column — removed commas and converted to integer
- Handled missing values — dropped null rows
- Standardized text columns using strip() and title()
- Renamed columns for readability
- Used explode() to split multi-value cuisines column

## Key Insights
- BTM and Whitefield have the highest number of restaurants
- North Indian is the most popular cuisine in Bangalore
- 55% of restaurants accept online orders
- Only 12% of restaurants allow table booking
- Lavelle Road has the highest average restaurant rating
- Sankey Road is the most expensive area to dine in

## Dashboard
 [View Tableau Dashboard here](https://public.tableau.com/views/ZomatoDashboard_17824527109020/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

## Files
- `eda.py` — Python data cleaning script
- `zomato_cleaned.csv` — cleaned dataset

