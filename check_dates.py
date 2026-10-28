import pandas as pd

transit_path = (
    r"C:\mobility_inefficiency_analyzer\Subway_Rider_Survey_(2019)_20261027.csv"
)
weather_path = r"C:\mobility_inefficiency_analyzer\4420613.csv"

transit_df = pd.read_csv(transit_path)
weather_df = pd.read_csv(weather_path)

print("--- TRANSIT SURVEY DATES ---")
print("Column 'submitted_at' sample:")
print(transit_df["submitted_at"].head(3))

print("\n--- WEATHER DATA DATES ---")
print("Column 'DATE' sample:")
print(weather_df["DATE"].head(3))