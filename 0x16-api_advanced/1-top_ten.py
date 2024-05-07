#!/usr/bin/python3
"""
A function that queries the API and prints the first 10 hot posts.
"""
import requests


def top_ten(subreddit):
    """The function responsile for getting the top 10 titles

    Args:
        subreddit (string): the subreddit to get it's titles

    Returns:
        None: in case error with response
    """
    res = requests.get(f'https://www.reddit.com/r/{subreddit}/hot/.json')
    if res.status_code == 200:
        data = res.json().get('data').get('children')
        for i in range(10):
            print(data[i].get('data').get('title'))
    else:
        print('None')
