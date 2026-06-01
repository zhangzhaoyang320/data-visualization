import pandas as pd
import numpy as np

np.random.seed(42)
months = ["1月","2月","3月","4月","5月","6月","7月","8月","9月","10月","11月","12月"]
products = ["产品A","产品B","产品C"]

rows = []
for month in months:
    for product in products:
        rows.append({
            "月份": month,
            "产品": product,
            "销售额": round(np.random.uniform(1000, 10000), 2),
            "利润": round(np.random.uniform(100, 2000), 2),
            "销量": np.random.randint(50, 500)
        })

df = pd.DataFrame(rows)
df.to_excel("D:\\222\\projects\\dataviz\\sample_data.xlsx", index=False)
print("Done")
