import pandas
import numpy
import matplotlib.pyplot as plt

from downloadData import target_path

# OBS: For most of the following examples work just add a print(example)

""" A simple series of examples of pre-created datasets manipulation
    Using the nba dataset from Real Python "Using Pandas and Python
    to Explore Your Dataset" tutorial.
"""

# Read dataset, also works with other data types, kike json, html and sql tables
nba_data = pandas.read_csv(target_path)

type(nba_data)  # Dataset type check
nba_data.shape  # Dataset rows X columns quantity info

# nba_data.info()  # Display all column types. Commented to avoid bash pollution
nba_data.head()  # Show the first 5 rows
nba_data.tail()  # Show the last 5 rows
nba_data.describe()  # Show basic descriptive data, for numeric columns only, but...
nba_data.describe(include=numpy.object)  # Other data types can be included too

""" Creating dataseries from scratch """

# A Series is a 1-dimensional data structure, like a python list
series = pandas.Series(
    ["Python", "Flask", "Django"],
    index=[1, 2, 3]  # Sets a custom index for Series
)

# A DataFrame is a 2-dimensional data structure, like a python dictionary,
# and each column of a DataFrame is a Series
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

# Iterating through the columns of a DataFrame
for column in dataframe.columns:
    new_series = dataframe[column]  # Assign the column series to a new Series

""" Plot data on a more graphical way

    I recomend to use the following commands on the jupyter notebook, because
    bro, charts are REALLY cool.

    OBS: If the requirements.txt is installed just run 'jupyter network'
         to start the jupyter service
"""

numeric_dataframe = pandas.DataFrame({
    "Random Label 1": [1, 3, 56, 23],
    "Random Label 3": [12, 43, 21, 10]
})

# Plots a basic line based chart, but there's other options, like .bar(),
# .area(), .scatter() and more, just add them w/ dataframe.plot.*
numeric_dataframe.plot()
