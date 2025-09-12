import pandas as pd

df = pd.read_csv("storm_data_search_results.csv")

print(df.columns)
print(df["DAMAGE_CROPS_NUM"].head(10))

print(df[["EVENT_NARRATIVE", "DAMAGE_CROPS_NUM"]].sample(5))
