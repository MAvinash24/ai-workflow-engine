import requests

def call_api(url):
    res = requests.get(url)
    return res.json()[:3]