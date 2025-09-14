import requests
import pandas as pd

url = "https://data.nsw.gov.au/data/api/3/action/datastore_search"
resource_id = "3e6d5f6a-055c-440d-a690-fc0537c31095"

all_records = []
limit = 1000
offset = 0

while True:
    params = {"resource_id": resource_id, "limit": limit, "offset": offset}
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    records = data["result"]["records"]
    
    if not records:
        break  # stop when no more data
    
    all_records.extend(records)
    offset += limit

print(f"Fetched {len(all_records)} records")

# Save to CSV
df = pd.DataFrame(all_records)
df.to_csv("nsw_schools_raw.csv", index=False)
df.head()
df.to_csv("nsw_schools.csv", index=False)
print("Data saved to nsw_schools.csv")

