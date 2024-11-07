import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Đọc dữ liệu từ tệp CSV
df = pd.read_csv("company_sales_data.csv")
monthlist = df['month_number'].tolist()
facecream_sales = df['facecream'].tolist()
facewash_sales = df['facewash'].tolist()

# Tạo biểu đồ cột với số liệu mỗi tháng
fig = plt.figure(figsize=(10, 6))
X = np.arange(len(monthlist))  # Tạo mảng các chỉ số cho từng tháng

# Vẽ biểu đồ cột
plt.bar(X - 0.15, facecream_sales, color='b', width=0.3, label='Face Cream Sales')
plt.bar(X + 0.15, facewash_sales, color='r', width=0.3, label='Face Wash Sales')

# Thiết lập các thuộc tính biểu đồ
plt.xlabel('Số tháng')
plt.ylabel('Số đơn vị đã bán')
plt.title('Số lượng sản phẩm kem dưỡng da mặt và sữa rửa mặt bán được mỗi tháng')
plt.legend(loc='upper left')
plt.grid(True, linestyle='--')
plt.xticks(X, monthlist)
plt.yticks([500, 1000, 1500, 2000, 2500, 3000, 3500])

plt.show()
