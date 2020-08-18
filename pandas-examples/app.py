import pandas
import numpy

from downloadData import target_path

# OBS: For most of the following examples work just add a print(example)

""" A simple series of examples of pre-created datasets manipulation
    Using the nba dataset from Real Python "Using Pandas and Python
    to Explore Your Dataset" tutorial.
"""

# Read dataset, also works with other data types, kike json, html and sql tables
data = pandas.read_csv(target_path)

type(data)  # Dataset type check
data.shape  # Dataset rows X columns quantity info

# data.info()  # Display all column types. Commented to avoid bash pollution
data.head()  # Show the first 5 rows
data.tail()  # Show the last 5 rows
data.describe()  # Show basic descriptive data, for numeric columns only, but...
data.describe(include=numpy.object)  # Other data types can be included too

""" Creating dataseries from scratch """

# A series is like a python list
series = pandas.Series(
    ["Python", "Flask", "Django"],
    index=[1, 2, 3]  # Sets a custom index for Series
)

# A dataframe is a 2-dimensional data structure, like a python dictionary
dataframe = pandas.DataFrame({
    "Animal": ["Python", "Elephant"],
    "Language": ["Python", "PHP"]
})

# Access data the virgin way, with data[value]
series[1]

# Access data the chad way, with .loc(label index) and .iloc (positional index)
# SPOILER ALERT: the results will be different
series.loc[1]  # Return the element that owns label(index) '1'
series.iloc[1]  # Return element thay owns position '1'
