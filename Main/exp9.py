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
   
   # Create a sample DataFrame
   products, orders, shipments, returns = create_data_frame()
   
   # 1. Identify which orders are pending delivery.
   merge_orders = pd.merge(orders, shipments, on='OrderID', how='left')
   pending_orders = merge_orders[(merge_orders['Status'] == 'Pending')]
   print(pending_orders)
   
   # 2. List products that were returned most often
   merged_return_products = pd.merge(returns, orders, on='OrderId')
   print(merged_return_products)
   
   # 3. Show top 2  customers by total revenue
   
   
   # 4. Export full data to CSV and reload it using pandas
   
   
if __name__ == "__main__":
   main()