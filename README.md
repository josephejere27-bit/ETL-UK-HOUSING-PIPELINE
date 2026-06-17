# ETL Pipeline — UK House Price Data

## What this project does
A simple ETL (Extract, Transform, Load) pipeline built in Python that processes UK housing price data from a public dataset.

## Data Source
UK House Price Index — publicly available CSV dataset containing average house prices by region.

## Transformations Applied
- Removed rows with missing values
- Filtered data for England only
- Standardised column names to lowercase
- Converted date column to datetime format
- Converted average price to integer format

## How to Run
1. Ensure Python is installed
2. Install pandas: pip install pandas
3. Place average-house-prices.csv in the same folder as etl_pipeline.py
4. Run: python etl_pipeline.py
5. Output will be saved to housing_data.db

## Technologies Used
- Python
- Pandas
- SQLite3