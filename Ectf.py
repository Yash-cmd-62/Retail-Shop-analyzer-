#Retail Store Daily Revenue vs Customer Count Analysis
#● From: Minor 1 – EDA
#● Extension: Analyze revenue vs footfall correlation.
#● Add-ons: Scatter plots, line charts.
#● Difficulty: Medium

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("retail_daily_data.csv")

plt.figure(figsize=(7,5))
sns.scatterplot(x="Customer_Count", y="Revenue", data=df)
plt.title("Revenue vs Customer footfall")
plt.xlabel("Customer Count")
plt.ylabel("Revenue")
plt.show()

correlation = df["Customer_Count"].corr(df["Revenue"])
print("Correlation between Revenue and Customer Count:", correlation)

plt.figure(figsize=(10,5))
plt.plot(df["Date"], df["Revenue"], label="Revenue")
plt.plot(df["Date"], df["Customer_Count"], label="Customer Count")
plt.legend()
plt.title("Daily Revenue and Customer Count Trend")
plt.xticks(rotation=45)
plt.show()

df["Revenue_per_Customer"] = df["Revenue"] / df["Customer_Count"]
print(df[["Date", "Revenue_per_Customer"]].head())
