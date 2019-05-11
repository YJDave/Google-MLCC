# Course Page: https://colab.research.google.com/notebooks/mlcc/intro_to_pandas.ipynb?utm_source=mlcc&utm_campaign=colab-external&utm_medium=referral&utm_content=pandas-colab&hl=en#scrollTo=JndnmDMp66FL

from __future__ import print_function

import pandas as pd


# Given data
city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])
cities = pd.DataFrame({ 'City name': city_names, 'Population': population })
cities['Area square miles'] = pd.Series([46.87, 176.53, 97.92])
cities['Population density'] = cities['Population'] / cities['Area square miles']

# Task
"""
	Modify the cities table by adding a new boolean column that is True if and only if both of the following are True:

	* The city is named after a saint.
	* The city has an area greater than 50 square miles.

"""

city_name_validator = lambda city_name: True if 'San' in city_name else False
city_area_validator = lambda city_area: True if city_area > 50 else False

cities['Is wide and has saint name'] = (cities['Area square miles'].apply(city_area_validator) &
									    cities['City name'].apply(city_name_validator))

print(cities)
