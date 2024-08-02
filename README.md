# Clonal Complex Identification

This repository contains a Python script for identifying clonal complexes in microbial strain data based on allele profiles. The script reads data from a CSV file, groups similar strains into clonal complexes based on a configurable similarity threshold, and outputs the results to a new CSV file.

## Requirements

- Python 3.6 or higher
- Required Python packages:
  - `pandas`
  - `re` (part of Python's standard library)

You can install the necessary packages using `pip`:

```pip install pandas```

## Script Overview

The main script, `clonal_complex.py`, performs the following tasks:

1. **Reads Input Data:** Reads strain data from a CSV file provided by the user.
2. **Calculates Similarities:** Computes the number of matching alleles between strains.
3. **Identifies Clonal Complexes:** Groups strains into clonal complexes based on a user-defined similarity threshold.
4. **Outputs Results:** Saves the identified clonal complexes to a new CSV file in the same directory as the input file.

## Usage

1. **Clone the Repository:**

```
git clone https://github.com/sbenvari/ClonalComplex.git
cd ClonalComplex
```

3. **Run the Script:**

```
python clonal_complex.py
```
3. **Provide Input and Configuration:**

   - When prompted, enter the path to the CSV file containing your data.
   - Enter the similarity threshold (number of matching alleles required) when prompted.

   Example input:

   Please enter the path to the CSV file: /path/to/your/data.csv
   Please enter the similarity threshold (number of matching alleles required): 5

4. **Output File:**

   The script will generate a CSV file named `clonal_complex.csv` in the same directory as the input file. This file contains the clonal complex numbers for each strain.

## CSV File Format

The input CSV file should have the following format:

- **Header:** The first row should contain column names.
- **Columns:**
  - `St`: The column with unique identifiers for each strain.
  - Subsequent columns: Each column should represent a different allele profile.

Example CSV format:

```csv
St,gen1,gene1,gene2,gene3,gene4,gene5,gene6,gene7
ST1,78,45,23,12,34,56,78,90
ST2,78,44,23,12,34,56,78,91
ST3,79,45,24,13,35,57,79,92
...
```

**Imprtant** 

Allels with `~` and `?` are considered the same as the base allele. For instance, `78~` and `78?` should be treated as `78`.


## Contact

For questions or issues, please contact [sb474@st-andrews.ac.uk](mailto:sb474@st-andrews.ac.uk).

