import pandas as pd
import os

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "LA", "Chicago"]
}

df = pd.DataFrame(data)

new_row_loc = {"Name": "GF1", "Age": 35, "City": "City1"}
df.loc[len(df.index)] = new_row_loc

#new_row_loc2 = {"Name": "V3", "Age": 45, "City": "City2"}
#df.loc[len(df.index)] = new_row_loc2

data_dir = "data"
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, "sample_data.csv")

df.to_csv(file_path, index=False)

print("Saved Dataset to the data folder")
