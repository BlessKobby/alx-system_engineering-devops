#!/usr/bin/python3

"""
prints the titles of the first 10 hot posts listed for a given subreddit
"""

from requests import get


def top_ten(subreddit):
    """
    This function queries the Reddit API and prints the titles of the top
    10 hot posts listed for a given subreddit
    """

    if subreddit is not isinstance(subreddit, str) or None:
        print("None")

    usr_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    params = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    response = get(url, headers=usr_agent, params=params)
    results = response.json()

    try:
        my_data = results.get('data').get('children')

        for u in my_data:
            print(u.get('data').get('title'))

    except Exception:
        print("None")
