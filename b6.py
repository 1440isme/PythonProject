import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Đọc dữ liệu từ tệp CSV
df = pd.read_csv("company_sales_data.csv")
monthlist = df['month_number'].tolist()
bathingsoap_sales = df['bathingsoap'].tolist()
plt.plot(monthlist, bathingsoap_sales, marker='o', linestyle='-', color='r', linewidth=3, markerfacecolor='r', markersize=8, label='Lợi nhuận')
# Tạo biểu đồ cột với số liệu mỗi tháng
fig = plt.figure(figsize=(10, 6))
X = np.arange(len(monthlist))  # Tạo mảng các chỉ số cho từng tháng
plt.xlabel('sales dât of a facewash')
plt.ylabel('Tổng lợi nhun')
plt.xticks(monthlist)
plt.yticks([7500,10000,12500])