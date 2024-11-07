import pandas as pd
import matplotlib.pyplot as plt
# Đọc dữ liệu từ tệp CSV
df = pd.read_csv("company_sales_data.csv")
# Lấy dữ liệu bán kem đánh răng mỗi tháng
monthlist = df['month_number'].tolist()
toothpaste_sales = df['toothpaste'].tolist()
# Tạo biểu đồ phân tán
plt.figure(figsize=(10, 6))
plt.scatter(monthlist, toothpaste_sales, color='b', label='Kem đánh răng')
# Thiết lập các thuộc tính biểu đồ
plt.xlabel('Số tháng')
plt.ylabel('Số đơn vị đã bán')
plt.title('Số lượng kem đánh răng bán được mỗi tháng')
plt.legend(loc='upper left')
plt.grid(True, linestyle='--') 
plt.xticks(monthlist)
plt.yticks([4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000])

plt.show()