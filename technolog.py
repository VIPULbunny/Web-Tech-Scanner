import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

# Load technology dataset from GitHub
tech_url = 'http://raw.githubusercontent.com/sahilrahman12/Technology-Lookup-Web-Application/main/technologies.json'
tec = pd.read_json(tech_url).T  # Transpose so tech names are correct
tec.reset_index(inplace=True)  # Reset index so tech names become a column
tec.rename(columns={"index": "name"}, inplace=True)  # Rename column

# Ensure required columns exist in the dataset
columns_to_check = ["url", "scripts", "meta", "headers", "html"]
for col in columns_to_check:
    if col not in tec.columns:
        tec[col] = ""  # Create missing columns

# Function to extract the domain from a given URL
def format_url(user_url):
    formatted_url = re.sub(r'^.*//|/.*|www\.', '', user_url)  # Extract domain
    return formatted_url.lower()

# Function to scrape website content
def scrape_website(url):
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
        if response.status_code == 200:
            return response.text.lower()  # Convert page content to lowercase for better matching
        else:
            print(f"Error: Failed to fetch website (Status Code: {response.status_code})")
            return None
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

# Function to extract and match technologies used in the website
def detect_technology(url, tec_df):
    page_content = scrape_website(url)
    if page_content is None:
        return ["Error: Unable to scrape website"]

    matched_tech = set()  # Store matched technologies

    # Check every technology in the dataset
    for _, row in tec_df.iterrows():
        tech_name = row["name"]
        
        # Convert technology identifiers to lowercase list
        for col in columns_to_check:
            tech_value = row[col]
            if isinstance(tech_value, str):
                tech_keywords = [kw.strip().lower() for kw in tech_value.split(",") if kw.strip()]

                # Check if any keyword is found in the page content
                if any(kw in page_content for kw in tech_keywords):
                    matched_tech.add(tech_name)
                    break  # Stop checking further once a match is found

    return list(matched_tech) if matched_tech else ["No matching technology found"]

# Get user input for website URL
user_url = input("Enter the website URL: ")
formatted_url = format_url(user_url)
print(f"Formatted URL: {formatted_url}")

# Detect technologies used in the website
tech_used = detect_technology(user_url, tec)
print("Technologies used in this website:", ", ".join(tech_used))
