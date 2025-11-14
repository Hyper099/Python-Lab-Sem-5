import matplotlib.pyplot as plt
import numpy as np


#! ========= BAR ============
# # Sales data
# region_1_sales = [50, 85, 90, 60, 30]
# region_2_sales = [70, 65, 80, 95, 55]

# products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
# x = np.arange(len(products))  # numeric x positions
# bar_width = 0.35

# # Plot bars
# plt.bar(x - bar_width/2, region_1_sales, width=bar_width, label='Region 1')
# plt.bar(x + bar_width/2, region_2_sales, width=bar_width, label='Region 2')

# # Labels & title
# plt.xlabel("Products")
# plt.ylabel("Number of Sales")
# plt.title("Sales Comparison by Product and Region")
# plt.legend()

# plt.show()


#! ======== PIE ========
import matplotlib.pyplot as plt
import numpy as np

import matplotlib.pyplot as plt

cars = ['AUDI', 'BMW', 'FORD', 'TESLA', 'JAGUAR', 'MERCEDES']
data = [23, 17, 35, 29, 12, 41]

plt.figure(figsize=(8, 6))

plt.pie(
   data,
   labels=cars,
   autopct='%1.1f%%',
   startangle=90,
   explode=[0.0, 0.1, 0.3, 0.2, 0.0, 0.1],
   shadow=True
)

plt.title("Car Sales Pie Chart")

plt.show()


#! ======= Automation with python ========




