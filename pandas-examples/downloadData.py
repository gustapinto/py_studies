from sys import exc_info

import requests

""" A simple example of downloading a .csv with Python using the nba dataset
    from Real Python "Using Pandas and Python to Explore Your Dataset" tutorial.
"""

download_url = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv'
target_path = 'nba_all_elo.csv'

response = requests.get(download_url)
response.raise_for_status()  # Checks for request success

if __name__ == "__main__":
    with open(target_path, 'wb') as f:
        f.write(response.content)

    print("Download complete")
