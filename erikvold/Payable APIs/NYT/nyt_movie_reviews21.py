#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import platform
import requests
import shutil
import sys
import urllib.parse

__all__ = ["reviews21"]

settings_data = open('settings.json')
apiKey = json.load(settings_data)['key']

def get_json(uri):
    raw = requests.get(uri)
    data = raw.json()
    return data


def reviews21(query):
    json = get_json("".join([
      'http://api.nytimes.com/svc/movies/v2/reviews/search.json?api-key=',
      apiKey,
      '&query=',
      urllib.parse.quote(query)
    ]))

    info = {
        'results': json['results'],
    }

    return info

if __name__ == '__main__':
    url = sys.argv[1]
    data = reviews21(url)
    formatted_data = json.dumps(data, indent=2, sort_keys=True)
    print(formatted_data)
