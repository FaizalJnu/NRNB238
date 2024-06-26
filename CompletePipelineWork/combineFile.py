import pandas as pd
import glob
import os

# Define the base path to your files
base_path = '../BEELINE-data/inputs/Curated/mCAD'

# Generate the full paths to the ExpressionData.csv files in each GSD-2000-* directory
csv_files = [os.path.join(base_path, f'mCAD-2000-{i}/ExpressionData.csv') for i in range(1, 11)]

# Initialize an empty list to store individual DataFrames
data_frames = []

# Read each CSV file and append it to the list
for file in csv_files:
    df = pd.read_csv(file, index_col=0)  # Assuming the first column is the gene identifiers
    data_frames.append(df)

# Concatenate all DataFrames along the columns
combined_df = pd.concat(data_frames, axis=1)

# Save the combined DataFrame to a new CSV file
combined_df.to_csv('../BEELINE-data/inputs/curated/mCAD/mCAD_data.csv')

print("Files combined successfully!")