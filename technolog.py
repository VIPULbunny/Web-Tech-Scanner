# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
import requests

# Define URLs for fetching JSON data
content_url = 'content.json'  # Local JSON file
tech_url = 'http://raw.githubusercontent.com/sahilrahman12/Technology-Lookup-Web-Application/main/technologies.json'

# Load technology data from external JSON URL
tech = pd.read_json(tech_url)

# Load category data from local JSON file
cats = pd.read_json(content_url)

# Display available column names in the dataset
print("Available columns:", cats.columns)

# Display first few rows to understand the structure
print(cats.head())

# Define the timestamp column name
timestamp_col = "TimeStamps"

# Convert timestamps to a readable datetime format if the column exists
if timestamp_col in cats.columns:
    cats[timestamp_col] = pd.to_datetime(pd.to_numeric(cats[timestamp_col], errors='coerce'), unit='s')
else:
    print(f"Column '{timestamp_col}' not found! Available columns: {cats.columns}")

# Create copies of the original datasets for further processing
data_cats = cats.copy()
data_tech = tech.copy()

# Display the first few rows of both datasets
print(data_tech.head())
print(data_cats.head())

# Transpose the technology dataset so that rows become columns
data_tech = data_tech.T

# Display the shape (dimensions) of the transposed dataset
print(data_tech.shape)

# Show column names after transposition
print(data_tech.columns)

# Display dataset information to check for missing values or data types
print(data_tech.info())

# Create deep copies of datasets to prevent accidental modifications
tec = data_tech.copy()
cat = data_cats.copy()

# Map numerical category IDs in 'cats' column to actual category names
for i in tec.cats:
    for j in range(len(i)):
        if not isinstance(i[j], (int, float)) or np.isnan(i[j]):  # Skip NaN values
            continue
        
        # Check if categories exist in different possible formats
        if isinstance(cat.categories, pd.Series):
            i[j] = cat.categories.iloc[int(i[j]) - 1]
        elif isinstance(cat.categories, pd.DataFrame) and 'name' in cat.categories.columns:
            i[j] = cat.categories.iloc[int(i[j]) - 1]['name']
        elif isinstance(cat.categories, (list, np.ndarray)):
            i[j] = cat.categories[int(i[j]) - 1]
        else:
            print(f"Unexpected type for cat.categories: {type(cat.categories)}")

# Display the cleaned dataset with mapped category names
print(tec)
