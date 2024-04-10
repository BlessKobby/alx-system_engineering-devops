#!/usr/bin/python3
""" Reddit API Queries """

import json
import requests


def count_words(subreddit, word_list: str, after="", count=[]):
    """
    A recursive function that queries the Reddit API, parses the title
    of all hot articles, and prints a sorted count of given keywords
    (case-insensitive, delimited by spaces. Javascript should count
    as javascript, but java should not).
    """

    if after == "":
        count = [0] * len(word_list)

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    request = requests.get(url,
                           params={'after': after},
                           allow_redirects=False,
                           headers={'user-agent': 'bhalut'})

    if request.status_code == 200:
        data = request.json()

        for topic in (data['data']['children']):
            for word in topic['data']['title'].split():
                for u in range(len(word_list)):
                    if word_list[u].lower() == word.lower():
                        count[u] += 1

        after = data['data']['after']
        if after is None:
            save = []
            for u in range(len(word_list)):
                for v in range(u + 1, len(word_list)):
                    if word_list[u].lower() == word_list[v].lower():
                        save.append(v)
                        count[u] += count[v]

            for u in range(len(word_list)):
                for v in range(u, len(word_list)):
                    if (count[v] > count[u] or
                            (word_list[u] > word_list[v] and
                             count[v] == count[u])):
                        aux = count[u]
                        count[u] = count[v]
                        count[u] = aux
                        aux = word_list[u]
                        word_list[u] = word_list[v]
                        word_list[v] = aux

            for u in range(len(word_list)):
                if (count[u] > 0) and u not in save:
                    print("{}: {}".format(word_list[u].lower(), count[u]))
        else:
            count_words(subreddit, word_list, after, count)
