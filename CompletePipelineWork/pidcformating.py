import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import KBinsDiscretizer

# Function to read the CSV file
def read_gene_embeddings(file_path):
    # Read the CSV file
    # Assuming the first column contains gene names and should be used as index
    df = pd.read_csv(file_path, index_col=0)
    return df

# Equal-width binning function
def equal_width_binning(df, n_bins=10):
    discretizer = KBinsDiscretizer(n_bins=n_bins, encode='ordinal', strategy='uniform')
    discretized_data = discretizer.fit_transform(df)
    return pd.DataFrame(discretized_data, index=df.index, columns=df.columns)

# Equal-frequency binning function
def equal_frequency_binning(df, n_bins=10):
    discretizer = KBinsDiscretizer(n_bins=n_bins, encode='ordinal', strategy='quantile')
    discretized_data = discretizer.fit_transform(df)
    return pd.DataFrame(discretized_data, index=df.index, columns=df.columns)

# Main process
def main():
    # Specify the path to your input CSV file
    input_file = './KaggleGen_GE_MS_combined/gene_embeddings_combined-GSD-allhuman_model_1024.csv'
    
    # Read the gene embeddings
    df = read_gene_embeddings(input_file)
    
    # Print some information about the data
    print(f"Loaded data shape: {df.shape}")
    print(f"First few rows:\n{df.head()}")
    
    # Apply discretization
    df_equal_width = equal_width_binning(df)
    df_equal_freq = equal_frequency_binning(df)
    
    # Save the discretized data
    df_equal_width.to_csv('discretized_equal_width_GSD.csv')
    df_equal_freq.to_csv('discretized_equal_freq_GSD.csv')
    
    print("Discretization complete. Files saved as 'discretized_equal_width.csv' and 'discretized_equal_freq.csv'")

if __name__ == "__main__":
    main()