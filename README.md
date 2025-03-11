# Explonatory-Data-Analysis-using-Ecommerce-dataset
The EDA of this e-commerce dataset analyzes 541,909 records with 8 attributes, including invoices, products, prices, and customer locations. Missing values in CustomerID and Description suggest guest checkouts. We’ll explore purchase trends, price variations, and customer segmentation using visualizations to uncover patterns for future analysis.
<br>
<br>
The dataset is hosted externally.Check it Out (https://raw.githubusercontent.com/gujjaripavan222/Explonatory-Data-Analysis-using-Ecommerce-dataset/refs/heads/main/data.csv)
<br>
<br>
This code is a comprehensive data analysis pipeline, ready to be used in real-world business intelligence. It gives insights into customer behavior, sales trends, and country-wise performance. I covered data ingestion, cleaning, transformation, analysis, and visualization — a full-cycle EDA!

step 1: Importing libraries
<br>
step 2: loading the dataset and initial inspection
        checked shape,head/tail
        printed column names and renamed column names 
        verified changes by checked updated column names
<br>
step 3: Data Cleaning
        converted invoice_date to datetime format
        converted description column to lower case
        checked for missing values isna().sum() and dropped missing values 
        converted cust_id to int64 datatype 
        Removed negative values from quantity column
        created new column  amount_spent as quantity * unit_price
<br>
step 4: Feature engieneering
        created new date related columns 
        year_month,month,day,hour columns 
<br>
step 5: Explonatory Data Anlysis
        Grouped data to analyze customer-wise and country-wise orders and amount spent.
        Identified top customers by number of orders and money spent.
        Analyzed monthly and daily sales patterns - Number of orders per month - Number of orders per day
        Examined unit_price distribution to spot outliers and free products (0 price).
        Filtered free products and analyzed their monthly trend.
<br>
step 6: Data Visualization
        Used Matplotlib and Seaborn for visualizing key metrics
        Line plots for: Orders and money spent by different customers
        Bar plots for: Orders by month, day, and country and Money spent by country
        Boxplot for analyzing unit price distribution
        Horizontal bar plots for better readability on country-based data
        Special visualization of data excluding the United Kingdom to see smaller markets.
<br>
step 7: Country-level Analysis
        Identified number of orders and total money spent per country.
        Visualized spending distribution, excluding dominant regions like the UK for better clarity.
<br>
Author-Pavan Kumar
