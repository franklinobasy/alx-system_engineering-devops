#!/usr/bin/python3
'''
Write a function that queries the Reddit API and prints the
titles of the first 10 hot posts listed for a given subreddit.

Requirements:
- Prototype: def top_ten(subreddit)
- If not a valid subreddit, print None.
- NOTE: Invalid subreddits may return a redirect to search results.
  Ensure that you are not following redirects.
'''

import requests


def top_ten(subreddit: str) -> str:
    '''
    prints the titles of the first 10 hot posts listed for a given subreddit.
    '''

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Franklin"}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(None)

    response = response.json()["data"]["children"][:10]
    for item in response:
        print(item["data"]["title"])
