
import pandas as pd
from pathlib import Path

#1.Open the Excel file
folder = Path(__file__).parent
file = folder / "Global Superstore clean Data Set _EDA.xlsx"

df = pd.read_excel(file, sheet_name="Orders")

#---------------------------------------------

#2. Show first 5 rows
print(df.head())

#---------------------------------------------

#3. Count rows and columns
print("Rows and columns:", df.shape)

#---------------------------------------------

#4. Show column names
print("Column names:")
print(df.columns.tolist())

#---------------------------------------------

#5. Show dataset information
df.info()

#---------------------------------------------

#6. count the rows and columns
print("Dataset size:")
print(df.shape)

#---------------------------------------------

#7. Display column names
print("Column names:")
print(df.columns.tolist())

#---------------------------------------------

#8.Understand data types
print("Dataset information:")
df.info()

#---------------------------------------------

#9.check data types
print("Data types:")
print(df.dtypes)

#---------------------------------------------

#10. Find/countmissing values
print("Missing values in each column:")
print(df.isnull().sum())

#---------------------------------------------

#11. count all missing cells
print("Total missing values:", df.isnull().sum().sum())

#---------------------------------------------

#12.count duplicate rows
print("Duplicate rows:", df.duplicated().sum())

#---------------------------------------------

#=======================================================
#13. Calculate important statistics
print("Sales statistics:")
print(df["Sales"].describe())

print("Profit statistics:")
print(df["Profit"].describe())

print("Quantity statistics:")
print(df["Quantity"].describe())

#---------------------------------------------

#14. calculate totals
print("Total Sales:", df["Sales"].sum())
print("Total Profit:", df["Profit"].sum())
print("Total Quantity:", df["Quantity"].sum())

#---------------------------------------------

#15. Calculate Average
print("Average Sales:", df["Sales"].mean())
print("Average Profit:", df["Profit"].mean())

#---------------------------------------------

#16. Calculate Medians
print("Median Sales:", df["Sales"].median())
print("Median Profit:",df["Profit"].median())

#---------------------------------------------

#17. Convert Order date into date format
df["Order Date"]=pd.to_datetime(
    df["Order Date"], errors="coerce"
)

print("Invalid dates:", df["Order Date"].isnull().sum())

#---------------------------------------------

#18. Extract the year
df["Year"]=df["Order Date"].dt.year

#---------------------------------------------

#19. Calculate Yearly Sales
Yearly_Sales = df.groupby("Year")["Sales"].sum()

print("Yearly Sales:")
print(Yearly_Sales)

#---------------------------------------------

#20. Calculate Yearly profit
Yearly_Profit = df.groupby("Year")["Profit"].sum()
print("Yearly_Profit:")
print(Yearly_Profit)

#---------------------------------------------

#21: Calculate sales by category
category_sales = df.groupby("Category")["Sales"].sum()

#---------------------------------------------

#22. Sort from highest to lowest
category_sales = category_sales.sort_values(ascending=False)

print("Sales by Category:")
print(category_sales)

#---------------------------------------------

#23: Calculate profit by category
category_profit = df.groupby("Category")["Profit"].sum()

category_profit = category_profit.sort_values(ascending=False)

print("Profit by Category:")
print(category_profit)

#---------------------------------------------

#24. Calculate profit by region
region_profit = df.groupby("Region")["Profit"].sum()

region_profit = region_profit.sort_values(ascending=False)
print(region_profit)

#---------------------------------------------

#25. Calculate sales by region
region_sales = df.groupby("Region")["Sales"].sum()

#---------------------------------------------

#26. Sort from highest to lowest
region_sales = region_sales.sort_values(ascending=False)

print("Sales by Region:")
print(region_sales)

#---------------------------------------------

#27. Find the 5 lowest-profit records
lowest_profit = df.nsmallest(5, "Profit")

print("5, Lowest Profit Records:")
print(lowest_profit)

#---------------------------------------------

#28. Find the 5 highest-profit records
highest_profit = df.nlargest(5, "Profit")

print("5 Highest Profit Records:")
print(highest_profit)

#---------------------------------------------

#29: Find the 5 highest-sales records
highest_sales = df.nlargest(5, "Sales")

print("5 Highest Sales Records:")
print(highest_sales)

import matplotlib.pyplot as plt

#---------------------------------------------

#30. Create a Yearly sales chart

Yearly_Sales.plot(kind="line", marker="o")

plt.title("Yearly sales Trend")
plt.xlabel("Year")
plt.ylabel("Total Sales")
plt.grid(True)

plt.tight_layout()
plt.savefig("yearly_sales.png")
plt.show()

#---------------------------------------------

#31. sales by category chart

category_sales.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("Category_Sales.png")
plt.show()

#---------------------------------------------

#32. Profit by category chart
category_profit.plot(kind="bar")

plt.title("Profit by category")
plt.xlabel("Category")
plt.ylabel("Total Profit")
plt.tight_layout()
plt.savefig("Category_profit.png")
plt.show()

#---------------------------------------------

#33. profit by region chart
region_profit.plot(kind="bar")

plt.title("Profit by region")
plt.xlabel("region")
plt.ylabel("Total Profit")
plt.tight_layout()
plt.savefig("region_profit.png")
plt.show()  

#---------------------------------------------

#34. Yearly Profit Chart
Yearly_Profit.plot(kind="line", marker="o")

plt.title("Yearly Profit Trend")
plt.xlabel("Year")
plt.ylabel("Total Profit")
plt.grid(True)
plt.tight_layout()
plt.savefig("Yearly_Profit.png")
plt.show()

#---------------------------------------------

#35. Sales by Region Chart

region_sales.plot(kind="bar")

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")

plt.tight_layout()
plt.savefig("region_sales.png")
plt.show()

#---------------------------------------------

#36. Business Insights

print("\n========== BUSINESS INSIGHTS ==========")

# Insight 1: Yearly Sales Trend
highest_sales_year = Yearly_Sales.idxmax()
lowest_sales_year = Yearly_Sales.idxmin()

print("\nInsight 1: Yearly Sales Trend")
print("Highest sales year:", highest_sales_year)
print("Total sales in that year:", round(Yearly_Sales.max(), 2))
print("Lowest sales year:", lowest_sales_year)
print("Total sales in that year:", round(Yearly_Sales.min(), 2))


# Insight 2: Best-Selling Category
best_category = category_sales.idxmax()

print("\nInsight 2: Best-Selling Category")
print("Category with highest sales:", best_category)
print("Total sales:", round(category_sales.max(), 2))


# Insight 3: Most Profitable Category
best_profit_category = category_profit.idxmax()

print("\nInsight 3: Most Profitable Category")
print("Category with highest profit:", best_profit_category)
print("Total profit:", round(category_profit.max(), 2))


# Insight 4: Best-Performing Region by Sales
best_sales_region = region_sales.idxmax()

print("\nInsight 4: Best-Performing Region by Sales")
print("Region with highest sales:", best_sales_region)
print("Total sales:", round(region_sales.max(), 2))


# Insight 5: Lowest-Profit Transaction
worst_transaction = df.loc[df["Profit"].idxmin()]

print("\nInsight 5: Lowest-Profit Transaction")
print("Product:", worst_transaction["Product Name"])
print("Region:", worst_transaction["Region"])
print("Sales:", round(worst_transaction["Sales"], 2))
print("Profit:", round(worst_transaction["Profit"], 2))


print("\n========== END OF INSIGHTS ==========")
