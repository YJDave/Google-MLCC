# Course Page: https://colab.research.google.com/notebooks/mlcc/intro_to_pandas.ipynb?utm_source=mlcc&utm_campaign=colab-external&utm_medium=referral&utm_content=pandas-colab&hl=en#scrollTo=JndnmDMp66FL

# If you are using <3.* Python version, this line allows to use Python as function instead of keyword
# which is not supported in <3.* Python versions.
from __future__ import print_function

# Import pandas library
# Make sure you already have installed pandas
import pandas as pd

# Print installed pandas version number
print(pd.__version__)

# Create Series object -- single column data structure in pandas
city_name = pd.Series(['Bhavnagar', 'Ahemdabad', 'Mumbai'])
population = pd.Series([852469, 1015785, 485199])

# Create DataFrames using Series objects -- row-column relational data structure in pandas
population_city_wise = pd.DataFrame({
							'City name': city_name,
							'population': population,
						})
# NOTE: If the Series don't match in length, missing values are filled with special NA/NaN values.

# Create DataFrames by loading entire file
city_population = pd.read_csv("https://download.mlcc.google.com/mledu-datasets/california_housing_train.csv", sep=",")

# .describe function returns statistics of data
print(city_population.describe())
# .head function returns few intial row-data
print(city_population.head())

# TODO: Fix error on below line: ImportError: matplotlib is required for plotting. 
#print(city_population.hist('housing_median_age'))

# Accessing data from DataFrames
print(type(population_city_wise['City name']))
# Get all values of column `City name`
print(population_city_wise['City name'])
# Get second value of column `City name`(list starts with index 0)
print(population_city_wise['City name'][1])
# Get values between index 0(including) to 2(not including) from column `City name`
print(population_city_wise['City name'][0:2])