import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("data/datafile.xlsx")
plt.figure(figsize=[10,6])
plt.bar(df['District'].value_counts().index,df['District'].value_counts().values)
plt.xlabel("District")
plt.xticks(rotation = "vertical")
plt.ylabel('Count of District')
plt.yticks(range(0,65,5))
plt.title("District Population")
plt.savefig("F:/CI CD Pipeline/output/output1.png")
print("Saved images !!!")