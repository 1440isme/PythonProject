import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('student_sleep_patterns.csv')

columns = df.columns[1:7]  # Điều chỉnh số lượng cột để phù hợp với số lượng đồ thị con

plt.figure(figsize=(15, 10))

for i, column in enumerate(columns, 1):
    plt.subplot(3, 2, i)  # Đảm bảo rằng không có nhiều hơn 6 đồ thị con
    sns.countplot(x=column, data=df, palette='viridis')  # Vẽ biểu đồ countplot
    plt.title(column)

plt.tight_layout()
plt.show()
print(pd.DataFrame(df[columns].describe()))  # In ra bảng thống kê mô tả
