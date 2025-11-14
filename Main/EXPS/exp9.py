import pandas as pd
import numpy as np
from datetime import datetime
import kagglehub
import os

print("Downloading dataset from Kaggle...") 
try:
   dataset_path = kagglehub.dataset_download("puneetbhaya/online-retail")
   file_name = None
   for item in os.listdir(dataset_path):
      if "retail" in item.lower() and (
         item.endswith(".csv") or item.endswith(".xlsx")
      ):
         file_name = item
         break

   if file_name is None:
      raise FileNotFoundError(
         "Could not find the main transaction file (csv or xlsx) in the downloaded directory."
      )

   file_path = os.path.join(dataset_path, file_name)

   if file_name.endswith(".csv"):
      df = pd.read_csv(file_path, encoding="unicode_escape")
   elif file_name.endswith(".xlsx"):
      df = pd.read_excel(file_path)

except Exception as e:
   print(f"An error occurred during download or loading: {e}")
   print(
      "Please ensure you have a valid Kaggle API key configured and the file exists."
   )
   exit()

print(f"Data Loaded from: {file_path}")
print("Initial Data Check (First 5 Rows):")
print(df.head())
print("-" * 70)

df["Sales"] = df["Quantity"] * df["UnitPrice"]

df.dropna(subset=["CustomerID"], inplace=True)
df["CustomerID"] = df["CustomerID"].astype(int)

df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]

date_col = "InvoiceDate" if "InvoiceDate" in df.columns else "InvoiceDate"
df[date_col] = pd.to_datetime(df[date_col])

NOW = df[date_col].max() + pd.Timedelta(days=1)

customer_data = (
   df.groupby("CustomerID")
   .agg(
      Recency=(date_col, lambda x: (NOW - x.max()).days),
      Frequency=("InvoiceNo", "nunique"),
      Monetary=("Sales", "sum"),
      TotalItemsPurchased=("Quantity", "sum"),
      Last_Purchase_Date=(date_col, "max"),
   )
   .reset_index()
)

customer_data.rename(columns={"Monetary": "Total Amount Spent"}, inplace=True)

customer_data["Average Purchase Value"] = (
   customer_data["Total Amount Spent"] / customer_data["Frequency"]
)

print("Customer Segmentation Features (First 5 Rows):")
print(customer_data.head())
print("-" * 70)

print("Descriptive Statistics for Segmentation Features (Task 3):")
stats = (
   customer_data[["Total Amount Spent", "TotalItemsPurchased", "Recency", "Frequency"]]
   .describe()
   .T
)
print(stats)
