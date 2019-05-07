# This file generates data to use in `intro_to_pandas.py` file.

# Import libraries
# To get current directory
import os
# To generate random numbers
import random
# To work with csv files
import csv

# Variables
# You can modify following variables for different cases
min_value = 800000
max_value = 2400000
no_of_values = 1000
file_name = 'data.csv'

# Generate list of random values
list_of_values = random.sample(range(min_value, max_value), no_of_values)

# Get path to file where data will be stored
current_dir = os.getcwd()
data_file_path = os.path.join(current_dir, file_name)

# Store data(list of random values) as comma seprated values to csv file
with open(data_file_path, 'w+', newline="") as file_to_write:
	wr = csv.writer(file_to_write)
	wr.writerow(list_of_values)
