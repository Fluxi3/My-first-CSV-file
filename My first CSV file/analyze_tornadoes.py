import pandas as pd
import matplotlib.pyplot as plt


# Load the CSV file (must be in the same folder as this script)
df = pd.read_csv("storm_data_search_results.csv")

# Make sure we only look at Tornado events
tornadoes = df[df["EVENT_TYPE"] == "Tornado"]

# Count by county
counts = (
    tornadoes.groupby("CZ_NAME_STR")
    .size()
    .reset_index(name="tornado_count")
    .sort_values("tornado_count", ascending=False)
)

print(counts.head(10))  # Show top 10 counties

counts.head(10).plot(kind="bar", x="CZ_NAME_STR", y="tornado_count", legend=False)
plt.title("Top 10 Kansas Counties by Tornado Events (last 5 years)")
plt.ylabel("Tornado Count")
plt.show()