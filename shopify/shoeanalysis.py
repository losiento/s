import csv
from IPython.display import display
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('shoedata.csv')

display(df)

revenue = df['order_amount'].sum()
print(revenue)

num_orders = len(df.index)
print(num_orders)

aov = revenue/num_orders

print(aov)

df2 = df[df.shop_id != 78]
df3 = df2[df2.shop_id != 42]
new_revenue = df3['order_amount'].sum()
print(new_revenue)

new_num_orders = len(df3.index)
print(new_num_orders)

new_aov = new_revenue/new_num_orders

print(new_aov)
