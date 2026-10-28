import pandas as pd

# Define file paths
transit_path = (
    r"C:\mobility_inefficiency_analyzer\Subway_Rider_Survey_(2019)_20261027.csv"
)
weather_path = r"C:\mobility_inefficiency_analyzer\4420613.csv"

print("Loading datasets...")
transit_df = pd.read_csv(transit_path)
weather_df = pd.read_csv(weather_path)

# 1. Clean transit dates: split by ' @ ' to drop the time, then parse
date_strings = transit_df["submitted_at"].astype(str).str.split(" @ ").str[0]
transit_dt = pd.to_datetime(date_strings, dayfirst=True, errors="coerce")
transit_df["year_month"] = transit_dt.dt.to_period("M").astype(str)

# 2. Parse weather dates and extract Year-Month
weather_dt = pd.to_datetime(weather_df["DATE"], errors="coerce")
weather_df["year_month"] = weather_dt.dt.to_period("M").astype(str)

# Print unique values to verify matching keys
print(
    "Transit Year-Months sample:",
    transit_df["year_month"].dropna().unique()[:5],
)
print(
    "Weather Year-Months sample:",
    weather_df["year_month"].dropna().unique()[:5],
)

# 3. Merge datasets on 'year_month'
merged_df = pd.merge(transit_df, weather_df, on="year_month", how="inner")

print(f"\nSuccessfully merged! Final dataset shape: {merged_df.shape}")

if len(merged_df) > 0:
    merged_df.to_csv(
        r"C:\mobility_inefficiency_analyzer\cleaned_merged_data.csv", index=False
    )
    print("Saved merged dataset as 'cleaned_merged_data.csv' in your folder!")
else:
    print(
        "\n⚠️ Result is still 0 rows. Check the printed samples above to see why they differ."
    )