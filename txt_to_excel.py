import os
import pandas as pd

# Define the directory containing the text files
directory_path = r'C:\Users\shric\Desktop\dsmz_bacteria_2'

# Define the path for the output Excel file
output_excel_path = r'C:\Users\shric\Desktop\dsmz.xlsx'

# Define the column names
columns = ['Name', 'DSM No.', 'Strain designation', 'Other collection no. or WDCM no.',
           'Isolated from', 'Country', 'Date of sampling', 'Nagoya Protocol Restrictions',
           'History', 'Genbank accession numbers', 'Cultivation conditions',
           'Summary and additional information', 'Literature', 'Risk group', 'Supplied as']

# Initialize a list to hold the data
data = []

# Iterate over each file in the directory
for filename in os.listdir(directory_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(directory_path, filename)
        
        # Initialize a dictionary to hold the details of the current file
        details = {col: 'Not found' for col in columns}
        
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if line.strip():  # Skip empty lines
                    parts = line.split('\t', 1)  # Split using tab character
                    if len(parts) == 2:
                        key = parts[0].strip()
                        value = parts[1].strip()
                        if key in details:
                            details[key] = value
        
        # Add the details to the data list
        data.append(details)

# Create a DataFrame from the data list
df = pd.DataFrame(data, columns=columns)

# Save the DataFrame to an Excel file
df.to_excel(output_excel_path, index=False)

print(f"Details from text files have been written to {output_excel_path}")
