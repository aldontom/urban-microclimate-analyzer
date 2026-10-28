import pandas as pd

# Define exact file paths
transit_path = (
    r"C:\mobility_inefficiency_analyzer\Subway_Rider_Survey_(2019)_20261027.csv"
)
weather_path = r"C:\mobility_inefficiency_analyzer\4420613.csv"

print("--- Inspecting Transit / Survey Data ---")
transit_df = pd.read_csv(transit_path)
print(transit_df.info())
print("\nFirst 2 rows of Transit Data:")
print(transit_df.head(2))

print("\n" + "=" * 50 + "\n")

print("--- Inspecting Weather Data ---")
weather_df = pd.read_csv(weather_path)
print(weather_df.info())
print("\nFirst 2 rows of Weather Data:")
print(weather_df.head(2))