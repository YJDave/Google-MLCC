# This file generates data to use in `intro_to_pandas.py` file.

# NOTE: This file is used to generate random data in csv file. You can modify this file
# according to your requirement. Add/update/delete values in `list_of_columns`, which
# stores column detail and generate data for that column according to given detail.

#### Import libraries ####
# To get current directory
import os
# To generate random numbers
import random
# To work with csv files
import csv

#### Variables you can modify according to your requirement ####
# You can modify following variables for different cases
# Add new dict in list to add new column in data

# Variable Name   : Description
# list_of_columns : stores csv column meta data
# name  		  : name of column or header
# min_value 	  : minimum value column data can have
# max_value 	  : maximum value column data can have
# no_of_value 	  : no of experimental data in each column
# file_name 	  : file to store data into
list_of_columns = [
	{
		'name': 'age',
		'min_value': 0,
		'max_value': 100,
	},
	{
		'name': 'annual_income',
		'min_value': 0,
		'max_value': 24000000,
	},
	{
		'name': 'weight',
		'min_value': 1,
		'max_value': 200,
	},
]
# TODO: Allow to add list of choices and randomly allocate values from give choices
# TODO: use dict() to declare dictionary

# All coulmns will have same no of values
no_of_values = 10
# TODO: Allow to generate different number of values for each column and set NaN
# for remaining empty values in other columns

# TODO: Allow to create file in sub or other directory
file_name = 'data.csv'

#### Script to generate random csv data and store in file ####

get_dict_key_values = lambda key: [column[key] for column in list_of_columns]

# Generate list of random values
coulmn_labels = get_dict_key_values('name')
columns_min_values = get_dict_key_values('min_value')
columns_max_values = get_dict_key_values('max_value')

# DEBUG print(coulmn_labels, columns_max_values, columns_min_values)
list_of_values = [random.sample(range(columns_min_values[i], columns_max_values[i]), no_of_values)
				 for i in range(len(list_of_columns))]
# DEBUG print(list_of_values)

# Get path to file where data will be stored
current_dir = os.getcwd()
data_file_path = os.path.join(current_dir, file_name)

# TODO: Add new flag to column value to indicate how to store vallues in csv
# file--in quote or not. And use `wr_quote_value` wrtier or `wr_unquote_value`
# writer according to given flag for column value.

# Store data(list of random values) as comma seprated values to csv file
with open(data_file_path, 'w+') as file_to_write:
	wr_quote_value = csv.writer(file_to_write, quoting=csv.QUOTE_ALL)
	wr_unquote_value = csv.writer(file_to_write)

	# Add column header value with quote in csv
	wr_quote_value.writerow(coulmn_labels)
	for row_no in range(no_of_values):
		# DEBUG: print(row_no)
		wr_unquote_value.writerow([column_val[row_no] for column_val in list_of_values])
