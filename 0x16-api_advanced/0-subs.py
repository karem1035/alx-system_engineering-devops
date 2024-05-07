#!/usr/bin/python3
""" returns the number of subscribers for a given subreddit. """

import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API
    """

    res = requests.get(
        f'https://www.reddit.com/r/{subreddit}/about.json',
        headers={"User-Agent": "Custom"})
    if res.status_code != 200:
        return 0
    data = res.json().get('data').get('subscribers')
    return (data)
