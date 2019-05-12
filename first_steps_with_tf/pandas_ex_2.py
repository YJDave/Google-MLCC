# Course Page: https://colab.research.google.com/notebooks/mlcc/intro_to_pandas.ipynb?utm_source=mlcc&utm_campaign=colab-external&utm_medium=referral&utm_content=pandas-colab&hl=en#scrollTo=JndnmDMp66FL

from __future__ import print_function

import pandas as pd
import numpy as np

# Given data
# By default, at construction, pandas assigns index values that reflect the ordering of the source data.
# Once created, the index values are stable; that is, they do not change when data is reordered.

# Task
"""
	The reindex method allows index values that are not in the original DataFrame's index values.
	Try it and see what happens if you use such values! Why do you think this is allowed?

"""

city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento', 'Bhavnagar', 'Ahmedabad', 'Baroda'])
population = pd.Series([852469, 1015785, 485199, 345234, 345234, 1345234])
cities = pd.DataFrame({ 'City name': city_names, 'Population': population })
cities = cities.reindex([0, 3, 3, 2, 34])
print(cities)
