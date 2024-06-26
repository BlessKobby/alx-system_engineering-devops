#!/usr/bin/python3
"""
Quering of the Reddit API
"""
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """A recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit.
    """
    global after
    usr_agent = {'User-Agent': 'api_advanced-project'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    results = requests.get(url, params=parameters, headers=usr_agent,
                           allow_redirects=False)

    if results.status_code == 200:
        after_data = results.json().get("data").get("after")
        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)
        all_article_titles = results.json().get("data").get("children")
        for title_ in all_article_titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return (None)
