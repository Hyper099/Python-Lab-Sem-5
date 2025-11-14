import pandas as pd


def create_data_frame():
   products = pd.DataFrame({
      'PID': [101,102,103,104,105],
      'ProductName': ['Laptop','Mobile','Headphones','Microwave','Fridge'],
      'Category': ['Electronics','Electronics','Electronics','Home','Home'],
      'Price': [60000,20000,3000,8000,35000]
   })

   orders=pd.DataFrame({
      'OrderID': [1,2,3,4,5],
      'Customer': ['Alice','Bob','Charlie','David','Eve'],
      'Product_ID': [101,102,101,104,106],
      'Quantity': [1,2,1,1,1]
   })

   shipments=pd.DataFrame({
      'OrderID': [1,2,3,5],
      'ShippedDate':['2025-09-20','2025-09-21','2025-09-22','2025-09-23'],
      'Status': ['Delivered','Delivered','In Transmit','Pending']
   })

   returns=pd.DataFrame({
      'OrderID': [2,5],
      'ReturnReason': ['Damaged Item','Wrong Product']
   })

   return products, orders, shipments, returns

def main():
   print("=== Pandas DataFrame Manipulation ===\n")
   
   # Create sample DataFrames
   products, orders, shipments, returns = create_data_frame()
   
   # 1. Detect undelivered orders (pending or not shipped)
   print("1. UNDELIVERED ORDERS:")
   print("-" * 40)
   merge_orders_shipments = pd.merge(orders, shipments, on='OrderID', how='left')
   undelivered_orders = merge_orders_shipments[
      (merge_orders_shipments['Status'] == 'Pending') | 
      (merge_orders_shipments['Status'].isna()) |
      (merge_orders_shipments['Status'] == 'In Transmit')
   ]
   print(undelivered_orders[['OrderID', 'Customer', 'Product_ID', 'Status']])
   print()
   
   # 2. Find the most frequently returned products
   print("2. MOST FREQUENTLY RETURNED PRODUCTS:")
   print("-" * 40)
   merged_return_products = pd.merge(returns, orders, on='OrderID', how='inner')
   merged_return_products = pd.merge(merged_return_products, products, left_on='Product_ID', right_on='PID', how='left')
   return_counts = merged_return_products['ProductName'].value_counts()
   print(return_counts.to_string())
   print()
   
   # 3. Identify top 2 customers by total revenue
   print("3. TOP 2 CUSTOMERS BY TOTAL REVENUE:")
   print("-" * 40)
   orders_with_price = pd.merge(orders, products, left_on='Product_ID', right_on='PID', how='left')
   orders_with_price['TotalRevenue'] = orders_with_price['Quantity'] * orders_with_price['Price']
   customer_revenue = orders_with_price.groupby('Customer')['TotalRevenue'].sum().sort_values(ascending=False)
   top_2_customers = customer_revenue.head(2)
   print(top_2_customers.to_string())
   print()
   
   # 4. Merge multiple datasets into one
   print("4. MERGED DATASET (All DataFrames Combined):")
   print("-" * 40)
   merged_all = pd.merge(orders, products, left_on='Product_ID', right_on='PID', how='left')
   merged_all = pd.merge(merged_all, shipments, on='OrderID', how='left')
   merged_all = pd.merge(merged_all, returns, on='OrderID', how='left')
   print(merged_all)
   print()
   
   # 5. Save and reload data in CSV format
   print("5. SAVE AND RELOAD DATA:")
   print("-" * 40)
   
   # Save to CSV
   csv_filename = './Main/IA2_assignment/merged_data.csv'
   merged_all.to_csv(csv_filename, index=False)
   print(f"Data saved to: {csv_filename}")
   
   # Reload from CSV
   reloaded_data = pd.read_csv(csv_filename)
   print(f"Data reloaded successfully! Shape: {reloaded_data.shape}")
   print("\nFirst 3 rows of reloaded data:")
   print(reloaded_data.head(3))
   print()
   
   print("="*60)
   print("Analysis Complete!")
   
   
if __name__ == "__main__":
   main()