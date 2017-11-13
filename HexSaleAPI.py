import logging
import requests
import json


def _url(path):
    return 'https://api.hexsales.net/v1' + path

def get_articles():
    response = requests.get(_url('/articles'))
    data = response.content.decode("utf-8")
    return data

def get_summaries():
    return requests.get(_url('/summaries'))

def get_histories():
    return requests.get(_url('/histories'))

def get_pricelist():
    return requests.get(_url('/stats/pricelist'))

def get_mostsold():
    return requests.get(_url('/stats/mostsold'))

def post_search(article, limit=25,offset=0):
    response = requests.post(_url('/articles/search'), json={"name":article,"limit":limit, "offset":offset})

def get_articles_uuid(uuid):
    return requests.get(_url('/articles/{}'.format(uuid)))

def get_articles_histories(uuid):
    return requests.get(_url('/articles/{}/histories'.format(uuid)))

def get_articles_summaries(uuid):
    return requests.get(_url('/articles/{}/summaries'.format(uuid)))

def get_sets():
    return requests.get(_url('/sets'))

#print(post_search('Runebind').content)