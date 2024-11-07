from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
df = pd.read_csv("company_sales_data.csv")
products = [col for col in df.columns if col not in ['month_number', 'total_profit', 'total_units']]
plt.figure(figsize=(10, 6))
for product in products:
    plt.plot(df['month_number'], df[product], marker='o', linestyle='-', label=product)
plt.xlabel('Số tháng')
plt.ylabel('Số đơn vị đã bán')
plt.title('Số lượng đơn vị bán được mỗi tháng cho mỗi sản phẩm')
plt.legend(loc='upper left')
plt.grid(True)
plt.xticks(df['month_number'])
plt.yticks([1000, 2000, 4000, 6000, 8000, 10000, 12000, 15000, 18000])
plt.show()