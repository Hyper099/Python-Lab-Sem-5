import os
import json

base = "../Data/Covid/"
covid_data = []

for root, _, files in os.walk(base):
    for file in files:
        if file.endswith(".json"):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    covid_data.append(data)
            except Exception as e:
                print(f"Error reading {file_path}: {e}")

print(f"Total JSON files read: {len(covid_data)}")

total_confirmed_cases = 0
total_deaths = 0
total_recovered_cases = 0
total_active_cases = 0

country_stats = {}

for data in covid_data:
    country = data["country"]
    confirmed = data["confirmed_cases"]["total"]
    deaths = data["deaths"]["total"]
    recovered = data["recovered"]["total"]

    if country not in country_stats:
        country_stats[country] = {
            "total_confirmed": 0,
            "total_deaths": 0,
            "total_recovered": 0
        }

    country_stats[country]["total_confirmed"] += confirmed
    country_stats[country]["total_deaths"] += deaths
    country_stats[country]["total_recovered"] += recovered

with open("../Outputs/covid_summary.json", "w", encoding="utf-8") as f:
    json.dump(country_stats, f, indent=4, ensure_ascii=False)
print(country_stats)