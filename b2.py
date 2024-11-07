from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
df = pd.read_csv("company_sales_data.csv")
profitlist = df['total_profit'].tolist()
monthlist = df['month_number'].tolist()
plt.plot(monthlist, profitlist, marker='o', linestyle='--', color='r', linewidth=3, markerfacecolor='blue', markersize=8, label='Lợi nhuận')
# Thêm nhãn và tiêu đề
plt.xlabel('Số tháng')
plt.ylabel('Tổng lợi nhuận')
plt.title('Biểu đồ đường biểu diễn tổng lợi nhuận theo từng tháng')
plt.legend(loc='lower right')
plt.xticks(monthlist)
plt.yticks([100000,200000,300000,400000,500000])
plt.show()