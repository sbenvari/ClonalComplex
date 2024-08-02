import pandas as pd
import re
import os

def calculate_matches(profile1, profile2):
    # Function to calculate the number of matches between two profiles
    matches = sum(gene1 == gene2 for gene1, gene2 in zip(profile1, profile2) if gene1 != '?' and gene2 != '?')
    return matches

def extract_number(allele):
    # Adjusted regex to capture numbers and ignore the trailing '?'
    match = re.search(r'\b\d+[-]?\d*\b', allele)
    if match:
        return match.group()
    else:
        return None

def identify_clonal_complexes(dataframe, threshold):
    # Initialize list to store groups
    groups = []
    
    # Replace "?" with NaN for better handling of missing values
    dataframe.replace("?", pd.NA, inplace=True)
    
    # Iterate over each row (ST) in the dataframe
    for index, row in dataframe.iterrows():
        matched = False  # Flag to indicate if the current ST is added to any existing group
        
        # Iterate over existing groups to check for similarity
        for group in groups:
            for member in group:
                # Calculate similarity between the current ST and group members
                if calculate_matches(row[1:], dataframe.loc[member][1:]) >= threshold:
                    group.append(index)  # Add the current ST to the group
                    matched = True
                    break  # Stop searching for this group if similarity is found
            if matched:
                break  # Stop searching for other groups if similarity is found
        
        # If no similarity is found, create a new group with the current ST
        if not matched:
            groups.append([index])
    
    # Merge groups with similar members
    merged_groups = []
    for group in groups:
        merged = False
        for merged_group in merged_groups:
            for member in group:
                for merged_member in merged_group:
                    if calculate_matches(dataframe.loc[member][1:], dataframe.loc[merged_member][1:]) >= threshold:
                        merged_group.extend(group)
                        merged = True
                        break
                if merged:
                    break
            if merged:
                break
        if not merged:
            merged_groups.append(group)
    
    return merged_groups

# Ask the user for the file path and similarity threshold
file_path = input("Please enter the path to the CSV file: ")
threshold = int(input("Please enter the similarity threshold (number of matching alleles required): "))

# Read the input CSV file
df = pd.read_csv(file_path)

# Identify clonal complexes
clonal_complexes = identify_clonal_complexes(df, threshold)

# Assign numbers to clonal complexes
complex_numbers = {}
for i, group in enumerate(clonal_complexes, start=1):
    for st_index in group:
        complex_numbers[df.loc[st_index]["St"]] = i

# Create a DataFrame for the clonal complex numbers
complex_df = pd.DataFrame.from_dict(complex_numbers, orient='index', columns=['Clonal Complex'])

# Get the directory of the input file and create the output file path
input_dir = os.path.dirname(file_path)
output_file = os.path.join(input_dir, "clonal_complex.csv")

# Save the DataFrame to a new CSV file
complex_df.to_csv(output_file)

print(f"Clonal complexes have been saved to '{output_file}' file.")
