import os
import pandas as pd


def process_sales_data(root_dir):
    product_names_path = os.path.join(root_dir, "/Data/product_names.csv")
    product_names_df = pd.read_csv(product_names_path)
    product_dict = dict(zip(product_names_df["Product ID"], product_names_df["Product Name"]))

    sales_data = {}  
    months = set()   

    for dirpath, _, filenames in os.walk(root_dir):
        for file in filenames:
            if file.endswith(".csv") and file != "product_names.csv":
                file_path = os.path.join(dirpath, file)

                df = pd.read_csv(file_path)

                if not {"Date", "Product ID", "Quantity sold"}.issubset(df.columns):
                    continue

                df["Month"] = pd.to_datetime(df["Date"]).dt.to_period("M")
                months.update(df["Month"].unique())

                for _, row in df.iterrows():
                    pid = row["Product ID"]
                    qty = int(row["Quantity sold"])
                    sales_data[pid] = sales_data.get(pid, 0) + qty

    num_months = len(months)
    summary_data = []
    for pid, total_qty in sales_data.items():
        avg_qty = total_qty / num_months if num_months > 0 else 0
        pname = product_dict.get(pid, "Unknown Product")
        summary_data.append([pid, pname, total_qty, round(avg_qty, 2)])
        
    summary_df = pd.DataFrame(summary_data, columns=[
        "Product ID", "Product Name", "Total Quantity Sold", "Average Quantity Sold per Month"
    ])

    summary_df.sort_values(by="Total Quantity Sold", ascending=False, inplace=True)
    top5_df = summary_df.head(5)

    output_path = os.path.join(root_dir, "/Outputs/sales_summary.csv")
    summary_df.to_csv(output_path, index=False)

    print("\n📊 Top 5 Best-Selling Products:")
    print(top5_df.to_string(index=False))


if __name__ == "__main__":
    process_sales_data("path_to_sales_data")  