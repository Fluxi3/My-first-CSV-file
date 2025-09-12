# Capstone BSDA Project - Data Exploration Notes

## ✅ Environment Setup
- Installed **Python 3.13**
- Added Python to **PATH** so `python` works in terminal
- Installed libraries with pip:
  ```bash
  python -m pip install pandas matplotlib
  ```
- Running scripts in **VS Code Terminal** (not Output).

---

## 📂 Project Files
- `storm_data_search_results.csv` → NOAA Storm Events (Kansas Tornado Data)
- `analyze_tornadoes.py` → Python analysis script
- `notes.md` → This notebook of progress and tips

---

## 🐼 Pandas Cheat Sheet (Core Patterns)

### 1. Load Data
```python
import pandas as pd
df = pd.read_csv("storm_data_search_results.csv")
```

### 2. Preview Data
```python
df.head()        # first 5 rows
df.head(10)      # first 10 rows
df.tail()        # last 5 rows
df.columns       # list column names
df.shape         # (rows, columns)
```

### 3. Explore Values
```python
df["EVENT_TYPE"].unique()        # all unique event types
df["EVENT_TYPE"].value_counts()  # frequency of each type
```

### 4. Filter Rows
```python
tornadoes = df[df["EVENT_TYPE"] == "Tornado"]
```

### 5. Group + Count
```python
tornadoes["CZ_NAME_STR"].value_counts().head(10)  # top 10 counties
```

or step-by-step chaining:
```python
counts = (
    tornadoes.groupby("CZ_NAME_STR")
    .size()
    .reset_index(name="tornado_count")
    .sort_values("tornado_count", ascending=False)
)
print(counts.head(10))
```

### 6. Plot Data
```python
import matplotlib.pyplot as plt

counts.head(10).plot(kind="bar", x="CZ_NAME_STR", y="tornado_count")
plt.title("Top 10 Kansas Counties by Tornado Events (last 5 years)")
plt.ylabel("Tornado Count")
plt.show()
plt.savefig("tornado_counts.png")   # save chart as PNG
```

---

## 🕵️ Data Sniffing Checklist (when opening a new dataset)
1. `df.shape` → how many rows & columns?
2. `df.columns` → what are the column names?
3. `df.head()` → what do first few rows look like?
4. `df["col"].unique()` → what unique values are in a column?
5. `df["col"].value_counts()` → quick counts sorted by frequency.

---

## 🚀 Next Questions to Explore
- Tornadoes **per year** (which years were most active?)
- Tornadoes by **EF scale** (severity distribution)
- Counties with **highest property damage**
- Compare tornado counts to other event types (hail, flood)

---

_This is your first lab notebook entry 🎉 — you’ve now gone from raw CSV → analysis → chart!_
