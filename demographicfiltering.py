import pandas as pd
import numpy as np

df = pd.read_csv("article.csv")

articles = df.sort_values("totalEvents",ascending=False)
output = articles[["title","totalEvents","text"]].head(20).values.tolist()
print(output)