import csv
import os
import shutil
from datetime import datetime

import matplotlib.pyplot as plt
import pandas as pd

FILENAME = "expenses.csv"
BACKUP_FILE = "expenses_backup.csv"

def log_expense():
   print("\n=== Log a New Expense ===")
   name = input("Enter your name: ")
   date = input("Enter date (YYYY-MM-DD): ")
   description = input("Enter expense description: ")
   amount = float(input("Enter amount spent: "))
   category = input("Enter category (e.g., Groceries, Utilities, Entertainment): ")

   file_exists = os.path.isfile(FILENAME)

   with open(FILENAME, "a", newline="", encoding="utf-8") as file:
      writer = csv.writer(file, quoting=csv.QUOTE_ALL)
      if not file_exists:
         writer.writerow(["Name", "Date", "Description", "Amount", "Category"])
      writer.writerow([name, date, description, amount, category])
   print("Expense logged successfully!\n")

def analyze_expenses():
   if not os.path.exists(FILENAME):
      print("No expenses found.")
      return

   df = pd.read_csv(FILENAME)
   print("\n=== Expense Analysis ===")
   total_by_person = df.groupby("Name")["Amount"].sum()
   print("\nTotal Expenses by Family Member:")
   print(total_by_person)

   avg_daily_expense = df.groupby("Date")["Amount"].sum().mean()
   print(f"\nAverage Daily Household Expense: ₹{avg_daily_expense:.2f}\n")

def plot_expense_trends():
   if not os.path.exists(FILENAME):
      print("No expenses found.")
      return

   df = pd.read_csv(FILENAME)
   df["Date"] = pd.to_datetime(df["Date"])
   df.sort_values("Date", inplace=True)
   df_grouped = df.groupby("Date")["Amount"].sum().cumsum()

   plt.figure(figsize=(10, 5))
   plt.plot(df_grouped.index, df_grouped.values, marker="o", linestyle="-", color="b")
   plt.title("Expense Trends Over Time")
   plt.xlabel("Date")
   plt.ylabel("Cumulative Expenses (₹)")
   plt.grid(True)
   plt.tight_layout()
   plt.show()

def expense_report():
   if not os.path.exists(FILENAME):
      print("No expenses found.")
      return

   df = pd.read_csv(FILENAME)
   df["Date"] = pd.to_datetime(df["Date"])
   df["Month"] = df["Date"].dt.strftime("%Y-%m")

   print("\n=== Monthly Expense Report ===")
   total_by_person = df.groupby(["Month", "Name"])["Amount"].sum()
   print("\nTotal Expenses per Member per Month:")
   print(total_by_person)

   category_breakdown = df.groupby("Category")["Amount"].sum()
   print("\nExpense Breakdown by Category:")
   print(category_breakdown)

   monthly_expenses = df.groupby("Month")["Amount"].sum()
   monthly_expenses.plot(kind="bar", color="teal", figsize=(8, 4))
   plt.title("Monthly Expense Comparison")
   plt.xlabel("Month")
   plt.ylabel("Total Expenses (₹)")
   plt.tight_layout()
   plt.show()

def manage_budget():
   if not os.path.exists(FILENAME):
      print("No expenses found.")
      return

   df = pd.read_csv(FILENAME)
   categories = df["Category"].unique()

   print("\n=== Set Monthly Budgets ===")
   budgets = {}
   for cat in categories:
      budgets[cat] = float(input(f"Enter budget for {cat}: ₹"))

   spent = df.groupby("Category")["Amount"].sum()
   print("\n=== Budget Report ===")
   for cat in budgets:
      spent_amt = spent.get(cat, 0)
      remaining = budgets[cat] - spent_amt
      print(f"{cat}: Spent ₹{spent_amt:.2f} / Budget ₹{budgets[cat]:.2f}")
      if remaining < 0:
         print(f"Over budget by ₹{-remaining:.2f}!")
      else:
         print(f"Remaining budget: ₹{remaining:.2f}")
      print("-" * 40)

def backup_data():
   if not os.path.exists(FILENAME):
      print("No expense data found to back up.")
      return
   shutil.copy(FILENAME, BACKUP_FILE)
   print("Data backup created successfully!\n")

def restore_data():
   if not os.path.exists(BACKUP_FILE):
      print("No backup file found.")
      return
   shutil.copy(BACKUP_FILE, FILENAME)
   print(" Data restored successfully!\n")

def main():
   while True:
      print(
         """
========= Household Expense Tracker =========
1. Log a new expense
2. Analyze expenses
3. View expense trends
4. Generate monthly report
5. Manage budget
6. Backup data
7. Restore data
8. Exit
"""
      )
      choice = input("Enter your choice (1-8): ")

      if choice == "1":
         log_expense()
      elif choice == "2":
         analyze_expenses()
      elif choice == "3":
         plot_expense_trends()
      elif choice == "4":
         expense_report()
      elif choice == "5":
         manage_budget()
      elif choice == "6":
         backup_data()
      elif choice == "7":
         restore_data()
      elif choice == "8":
         print("Exiting... Goodbye!")
         break
      else:
         print("Invalid choice! Try again.\n")

if __name__ == "__main__":
   main()

