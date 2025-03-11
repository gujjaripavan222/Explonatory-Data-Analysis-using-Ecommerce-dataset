#Importing The Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#Loading the dataset
df=pd.read_csv("https://github.com/gujjaripavan222/Explonatory-Data-Analysis-using-Ecommerce-dataset/releases/download/v1.0/data.csv",encoding='ISO-8859-1')
#Number of rows and columns
print(df.shape)
#Access first five rows
print(df.head())
#Access last five rows
print(df.tail())
#Displaying total columns from dataset
print(df.columns)
#Getting all columns one by one
for column in df.columns:
    print(column)
#Renaming Column names
d={
    "InvoiceNo":"invoice_num",
    "StockCode":"stock_code",
    "Description":"description",
    "Quantity":"quantity",
    "InvoiceDate":"invoice_date",
    "UnitPrice":"unit_price",
    "CustomerID":"cust_id",
    "country":"country"
}

print(df.rename(columns=d,inplace=True))

#After changing column names checking new columns
print(df.columns)

#Again Accessing column names one by one
for i in df.columns:
    print(i)

#lets check inital data
print(df.head())

#DATA CLEANING
#checking column types
print(df.dtypes)

#Data Information
print(df.info())

#Checking missing values for each column
print(df.isnull)

#Checking number of columns
print(len(df.columns))

print(df.shape)

#Checking missing values count on each column
print(df.isnull().sum())

#Checking missing values count on each column and applying sort method
print(df.isnull().sum().sort_values())

print(df.isnull().sum().sort_values(ascending=False))

#Checking type of invoice_date column
print(df.dtypes)

#Converting invoice_date data type into datetime data type
df["invoice_date"]=pd.to_datetime(df.invoice_date,format="%m/%d/%Y %H:%M")

#Checking type of invoice_date
print(df.dtypes)

#Let us check description column
print(df.description)

#Lets call lower() method for description column

df["description"]=df.description.str.lower()

print(df.head())

#Missing values
#we need to handle missing values according to the requirements
print(df.isna().sum().sort_values(ascending=False))

#Dropping missing values
df.dropna(inplace=True)

#Now check missing values for each columns
print(df.isnull().sum())

#Get DataFrame Information
print(df.info())

#Lets check type of cust_id data type
df["cust_id"]

df["cust_id"]=df["cust_id"].astype("int64")

#Access first five rows
print(df.head())

#DataFrame information
print(df.info())

#DataFrame description
print(df.describe())

#Rounding the values in DataFrame
print(df.describe().round(2))

#Lets do Analysis
#Here quantity column having negative values
#we need to remove or delete negative values

#for example
a=[1,2,3,4,5,6]
for k in a:
    if k>=0:
        print(k)

#Removing Negative values from quantity column
condition= df.quantity > 0

df=df[condition]

df.describe().round(2)

#Access inital data
print(df.head())

#Check total no of rows and columns
df.shape

#Lets Add a New Column - amount_spent
df["amount_spent"]=df["quantity"]*df["unit_price"]

print(df.head())

#Check the new column from DataFrame
for j in df.columns:
    print(j)



#Rearranging columns for more readability
column_order=["invoice_num","invoice_date","stock_code","description","quantity","unit_price","amount_spent","cust_id","Country"]
df=df[column_order]

#Access five rows
print(df.head())

#Number of rows and columns
print(df.shape)

#Let us do Analysis on invoice_date column
#Number of columns

print(len(df.columns))

#Accessing invoice_date column
#Method 1 to access column
print(df["invoice_date"])

#Method 2 to access column
print(df.invoice_date)

#Access year value from invoice_date
print(df['invoice_date'].dt.year)

#Accessing month value from invoice_date column
print(df["invoice_date"].dt.year)

#Access inital data
print(df.head())

#Lets insert year_month column in 2nd position
#Let us do small calculation
#y=2010
#m=12
#y_m=100*2010+12
#y_m=201012 Here 2010 year, 12 month
c="year_month"
r=df["invoice_date"].map(lambda col: 100*(col.year) + (col.month))
df.insert(loc=2, column=c,value=r)
print(df)

#Access inital data
print(df.head())

#Adding month column to the existing dataframe
c2="month"
r2=df["invoice_date"].dt.month
df.insert(loc=3,column=c2,value=r2)
print(df.head())

#Lets Access invoice_date column
print(df.invoice_date)

#We can also get day of the week
print(df.invoice_date.dt.dayofweek)

#In Pandas the day format starts from 0 to 6
#By Applying +1 to Monday = 1 till sunday = 7

c3="day"
r3=(df.invoice_date.dt.dayofweek)+1
df.insert(loc=4,column=c3,value=r3)

print(df.head())

#Accessing hour column to existing dataframe
c4="hour"
v4=df.invoice_date.dt.hour
r4=df.invoice_date.dt.hour
df.insert(loc=5,column=c4,value=v4)
print(df.head())

#Lets display all columns
for s in df.columns:
    print(s)

#EXPLONATORY DATA ANALYSIS(EDA)
print(df.groupby(by=["cust_id"]).count())

print(df.groupby(by=["cust_id","Country"]).count())

print(df.groupby(by=["cust_id","Country"])["invoice_num"].count())

print(df.groupby(by=["cust_id","Country"],as_index=False)["invoice_num"].count())

print(df.groupby(by=["cust_id","Country"],as_index=False)["invoice_num"].count().head())

#DATA VISUALIZATION
orders=df.groupby(by=["cust_id","Country"],as_index=False)["invoice_num"].count()
print(orders)

#Check top 5 most number of orders
print(orders.sort_values(by="invoice_num",ascending=False).head())

#Visualizing - number of orders for different customers
orders=df.groupby(by=["cust_id","Country"],as_index=False)["invoice_num"].count()
plt.subplots(figsize=(15,6))
plt.plot(orders.cust_id,orders.invoice_num)

plt.xlabel("Customer Id")
plt.ylabel("Number of orders")
plt.title("Number of Orders for different customers")
plt.show()

print(df.info())

#How much money spent by each customer
f = df.groupby(by=['cust_id', 'Country'])[df.select_dtypes(include='number').columns].sum()
print(f)


print(df.groupby(by=["cust_id","Country"])["amount_spent"].sum())

print(df.groupby(by=["cust_id","Country"],as_index=False)["amount_spent"].sum())
      
money_spent= df.groupby(by=["cust_id","Country"],as_index=False)["amount_spent"].sum()

#Lets see top 5 customers who spent highest money
print(money_spent.sort_values(by="amount_spent",ascending=False).head())

#Lets see Top 10 customers who spent highest money
print(money_spent.sort_values(by="amount_spent",ascending=False).head(10))

#Visualize - Money spent for different customers 
money_spent=df.groupby(by=["cust_id","Country"],as_index=False)["amount_spent"].sum()

plt.subplots(figsize=(15,6))

plt.plot(money_spent.cust_id,money_spent.amount_spent)

plt.xlabel("Customer Id")
plt.ylabel("Money Spent (Dollars)")
plt.title("Money Spent for different customers")

plt.show()

#Number of orders for different months
print(df.groupby("invoice_num"))

print(df.groupby("invoice_num")["year_month"])

print(df.groupby("invoice_num")["year_month"].unique())

print(df.groupby("invoice_num")["year_month"].unique().value_counts())

print(df.groupby("invoice_num")["year_month"].unique().value_counts().sort_index())
color = sns.color_palette()

#Lets visualize number of orders for different months
ax=df.groupby("invoice_num")["year_month"].unique().value_counts().sort_index().plot(kind="bar",color=color[0],figsize=(15,6))

ax.set_xlabel("Number of year",fontsize=15)
ax.set_ylabel("Number of Orders",fontsize=15)
ax.set_title("Number of orders for different months (1st Dec 2010 - 9th Dec 2011)",fontsize=15)

t=("Dec_10","Jan_11","Feb_11","Mar_11","Apr_11","May_11","Jun_11","Jul_11","Aug_11","Sep_11","Oct_11","Nov_11","Dec_11")
ax.set_xticklabels(t,rotation="horizontal",fontsize=13)
plt.show()

#lets see how many orders per day
print(df.groupby("invoice_num"))

print(df.groupby("invoice_num")["day"])

print(df.groupby("invoice_num")["day"].unique())

print(df.groupby("invoice_num")["day"].unique().value_counts())

print(df.groupby("invoice_num")["day"].unique().value_counts().sort_index())

#Day wise sales count/business
print(df.head())

print(df.groupby("invoice_num"))

print(df.groupby("invoice_num")["day"])

print(df.groupby("invoice_num")["day"].unique())

print(df.groupby("invoice_num")["day"].unique().value_counts())

print(df.groupby("invoice_num")["day"].unique().value_counts().sort_index())

#Lets visualize day wise sales count/business
ax=df.groupby("invoice_num")["day"].unique().value_counts().sort_index().plot(kind="bar",color=color[0],figsize=(15,6))

ax.set_xlabel("Day",fontsize=15)
ax.set_ylabel("Number of orders",fontsize=15)
ax.set_title("Number of orders for different days",fontsize=15) 
d=("Mon","Tue","Wed","Thu","fri","Sun")
ax.set_xticklabels(d,rotation="horizontal",fontsize=15)
plt.show()

#Discover patterns for Unit price
print(df.unit_price.describe())

#Here minimum value for product is zero,so there are some free products
plt.subplots(figsize=(12,6))
sns.boxplot(df.unit_price)
plt.show()

#Filtering free products(cost=0)
df_free=df[df.unit_price==0]

print(len(df_free))

print(df_free.year_month)

print(df_free.year_month.value_counts())

print(df_free.year_month.value_counts().sort_index())

#Visualize frequency for different months
ax=df_free.year_month.value_counts().sort_index().plot(kind="bar",figsize=(12,6),color=color[0])

ax.set_xlabel("Month",fontsize=15)
ax.set_ylabel("Frequency",fontsize=15)
ax.set_title("Frequency for different Months",fontsize=15)

m=("Dec_10","Jan_11","Feb_11","Mar_11","Apr_11","May_11","Jul_11","Aug_11","Sep_11","Oct_11","Nov_11")
ax.set_xticklabels(m,rotation="horizontal",fontsize=13)
plt.show()

#How many orders for each country?
print(df.groupby("Country"))

print(df.groupby("Country")["invoice_num"])

print(df.groupby("Country")["invoice_num"].count())

print(df.groupby("Country")["invoice_num"].count().sort_values())

#Visualize - How many orders for each country?
country_orders=df.groupby("Country")["invoice_num"].count().sort_values()
plt.subplots(figsize=(15,8))
country_orders.plot(kind="barh",fontsize=12,color=color[0])
plt.xlabel("Number of orders",fontsize=12)
plt.ylabel("Country",fontsize=12)
plt.title("Number of orders for different countries",fontsize=12)
plt.show()

#Just Delete United kingdom from country_orders then visualize how many orders for each country
country_orders=df.groupby("Country")["invoice_num"].count().sort_values()
del country_orders["United Kingdom"]
plt.subplots(figsize=(15,8))
country_orders.plot(kind="barh",fontsize=12,color=color[0])
plt.xlabel("Number of orders",fontsize=12)
plt.ylabel("Country",fontsize=12)
plt.title("Number of orders for different countries",fontsize=12)
plt.show()

#How much money spent by each country?
print(df.groupby("Country"))

print(df.groupby("Country")["amount_spent"])

print(df.groupby("Country")["amount_spent"].sum())

print(df.groupby("Country")["amount_spent"].sum().sort_values())

#Visualize - How much money spent by each country?
country_spent=df.groupby("Country")["amount_spent"].sum().sort_values()
del country_spent["United Kingdom"]

plt.subplots(figsize=(15,8))
country_spent.plot(kind="barh",fontsize=12,color=color[0])
plt.xlabel("Money spent (Dollars)",fontsize=12)
plt.ylabel("country")
plt.title("Money spent by each country",fontsize=12)
plt.show()

#This is Data Analysis
#step 1: Importing libraries
#step 2: loading the dataset and initial inspection
#        checked shape,head/tail
#        printed column names and renamed column names 
#        verified changes by checked updated column names
#step 3: Data Cleaning
#        converted invoice_date to datetime format
#        converted description column to lower case
#        checked for missing values isna().sum() and dropped missing values 
#        converted cust_id to int64 datatype 
#        Removed negative values from quantity column
#        created new column  amount_spent as quantity * unit_price
#step 4: Feature engieneering
#        created new date related columns 
#        year_month,month,day,hour columns 
#step 5: Explonatory Data Anlysis
#        Grouped data to analyze customer-wise and country-wise orders and amount spent.
#        Identified top customers by number of orders and money spent.
#        Analyzed monthly and daily sales patterns - Number of orders per month - Number of orders per day
#        Examined unit_price distribution to spot outliers and free products (0 price).
#        Filtered free products and analyzed their monthly trend.
#step 6: Data Visualization
#        Used Matplotlib and Seaborn for visualizing key metrics
#        Line plots for: Orders and money spent by different customers
#        Bar plots for: Orders by month, day, and country and Money spent by country
#        Boxplot for analyzing unit price distribution
#        Horizontal bar plots for better readability on country-based data
#        Special visualization of data excluding the United Kingdom to see smaller markets.
#step 7: Country-level Analysis
#        Identified number of orders and total money spent per country.
#        Visualized spending distribution, excluding dominant regions like the UK for better clarity.



