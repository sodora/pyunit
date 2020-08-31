import requests
import json


def rest_get(url):
    r = requests.get(url, timeout=30)
    return r.json()

def rest_post(url, json_data):
    r = requests.post(url, headers={'Content-Type': 'application/json'}, data=json.dumps(json_data), timeout=30)
    return r.json()