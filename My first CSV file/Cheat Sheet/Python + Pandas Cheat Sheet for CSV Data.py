#1. Load a CSV
import pandas as pd

df = pd.read_csv("mydata.csv")   # replace with your filename

#2. Peek at your data
print(df.head())       # first 5 rows
print(df.columns)      # list column names
print(len(df))         # number of rows

#3. Filter rows (like WHERE in SQL)
# Only tornado events
tornadoes = df[df["EVENT_TYPE"] == "Tornado"]

# Only EF2 or stronger
ef2_up = df[df["TOR_F_SCALE"].isin(["EF2","EF3","EF4","EF5"])]

#4. Group + Count or Aggregate
# Count tornadoes by county
counts = tornadoes.groupby("CZ_NAME_STR").size()

# Average property damage by year
avg_damage = tornadoes.groupby("BEGIN_DATE")["DAMAGE_PROPERTY_NUM"].mean()

#5. Sort + View Top Results
print(counts.sort_values(ascending=False).head(10))
