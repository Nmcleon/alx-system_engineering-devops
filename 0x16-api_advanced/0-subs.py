#!/usr/bin/python3
"""Function that returns number of subscribers for a given subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        no_subs = data.get("data").get("subscribers")
        return no_subs
    else:
        return 0
