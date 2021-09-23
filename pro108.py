import csv
import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("pro108.csv")

Avg = df["Avg"].tolist()

fig = ff.create_distplot([Avg],["Brand Name"], show_hist = False)
fig.show()