import pandas as pd
import plotly.express as ps

df = pd.read_csv("Covid.csv")

fig = ps.line(df, x = "date", y = "cases", color = "country")
fig.show()