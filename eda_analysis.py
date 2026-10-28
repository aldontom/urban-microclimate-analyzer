import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Load the cleaned merged dataset
data_path = r"C:\mobility_inefficiency_analyzer\cleaned_merged_data.csv"
df = pd.read_csv(data_path)

print(f"Dataset loaded successfully with shape: {df.shape}")

# 1. Inspect Top Subway Lines Used Most Often
print("\n--- Top Subway Lines Used Most Often ---")
print(df["subway_line_used_most_often"].value_counts().head(10))

# 2. Analyze Delay Frequencies
print("\n--- Frequency of Delays Reported ---")
if "frequency_of_delays" in df.columns:
    print(df["frequency_of_delays"].value_counts())

# 3. Visualization: Top Complaints vs Subway Lines
plt.figure(figsize=(12, 6))
top_lines = df["subway_line_used_most_often"].value_counts().head(8).index
subset_df = df[df["subway_line_used_most_often"].isin(top_lines)]

sns.countplot(
    data=subset_df,
    x="subway_line_used_most_often",
    hue="frequency_of_delays",
    order=top_lines,
)
plt.title(
    "Delay Frequency Across Top Subway Lines (NYC Rider Survey - July 2019)"
)
plt.xlabel("Subway Line Used Most Often")
plt.ylabel("Number of Responses")
plt.legend(title="Frequency of Delays", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.xticks(rotation=45)
plt.tight_layout()

plot_path = r"C:\mobility_inefficiency_analyzer\subway_delays_eda.png"
plt.savefig(plot_path)
print(
    f"\nEDA visualization saved successfully to: {plot_path}"
)
plt.show()