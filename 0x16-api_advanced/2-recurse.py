#!/usr/bin/python3
"""
    a recursive function that queries the Reddit API,
    returns a list with the titles of all hot articles for a given subreddit.
    If no results are found for the subreddit, the function should return None.
"""
import json
import requests


def recurse(subreddit, hot_list=[]):
    """ The recursive function """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'user-agent': 'custom'}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 200:
        r = r.json()
        for post in r.get('data').get('children'):
            hot_list.append(post.get('data').get('title'))
        if r.get('data').get('after'):
            recurse(subreddit, hot_list)
        return hot_list
    else:
        return None

recurse('programming', hot_list=[])
