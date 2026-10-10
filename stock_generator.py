
import pandas as pd

# Step 1: Read stock market data
df = pd.read_csv("stock_market_data.csv")

# Convert Date into date format
df["Date"] = pd.to_datetime(df["Date"])

# Step 2: Calculate traded value
# Close price multiplied by trading volume
df["Traded_Value"] = df["Close"] * df["Volume"]

# Step 3: Estimate change in traded value
# This is NOT actual investor profit
df["Estimated_Change_Value"] = (
    df["Price_Change"] * df["Volume"]
)


# 1. Company with highest traded value
print("\n--- Company-wise Traded Value ---")

company_sales = df.groupby("Company").agg(
    Total_Volume=("Volume", "sum"),
    Total_Traded_Value=("Traded_Value", "sum"),
    Average_Close=("Close", "mean")
).sort_values("Total_Traded_Value", ascending=False)

print(company_sales.round(2))

print("\nCompany with Highest Traded Value:")
print(company_sales.index[0])

print("Traded Value:")
print(round(company_sales.iloc[0]["Total_Traded_Value"], 2))


# 2. Stock-wise estimated change
print("\n--- Stock-wise Estimated Change ---")

stock_profit = df.groupby("Symbol").agg(
    Total_Volume=("Volume", "sum"),
    Total_Price_Change=("Price_Change", "sum"),
    Estimated_Change_Value=("Estimated_Change_Value", "sum")
).sort_values("Estimated_Change_Value", ascending=False)

print(stock_profit.round(2))


# 3. Stock with highest positive estimated change
print("\n--- Best Stock by Estimated Change ---")

print(stock_profit.head(1))


# 4. Stock with lowest estimated change
print("\n--- Lowest Stock by Estimated Change ---")

print(stock_profit.tail(1))


# 5. Highest average percentage change by company
print("\n--- Average Percentage Change ---")

percentage = df.groupby("Company")["Change_Percent"].mean()
percentage = percentage.sort_values(ascending=False)

print(percentage.round(2))

print("\nHighest Average Percentage Change:")
print(percentage.index[0])


# 6. Daily market analysis
print("\n--- Daily Traded Value ---")

daily_sales = df.groupby("Date")["Traded_Value"].sum()
print(daily_sales.sort_values(ascending=False).head(10))


# 7. Overall market summary
print("\n--- Overall Summary ---")

print("Total Records:", len(df))
print("Number of Companies:", df["Company"].nunique())
print("Total Trading Volume:", df["Volume"].sum())
print("Total Traded Value:", round(df["Traded_Value"].sum(), 2))
