import requests
import json
from elasticsearch import Elasticsearch, RequestsHttpConnection
import json
import uuid
import re
import codecs
import random
import datetime
from dateutil import parser
import time

es = Elasticsearch()
# es.indices.delete(index='products', ignore=[400, 404])
#nhớ create lúc đầu
# res = es.indices.create(index='products', ignore=400)
# print(res)
# with open('C:\Users\admin\Downloads\Coderschool\\PhongVu.json', "r", encoding='utf-8') as read_file:
# search = es.search(index="products", body={
#         "query": {
#         "match_all": {}
#     },
#     "size": 10})
# print(search['hits']['hits'][0])
# query_body = {
#   "query": {
#       "match": {
#         "name": {
#             "query": "máyyi assusss",
#             "fuzziness": 2,
#             "prefix_length": 1
#         }
#       }
#     }
# }
# ans = es.search(index="products", body=query_body)['hits']['hits']
# for product in ans:
#     print(product['_source']['name'])
# print(ans[0])
with open('D:\Document\Python\\PhongVu.json', 'r', encoding='utf-8') as read_file:
    data = read_file.readlines()
    for line in (data):
        document = json.loads(line)
        # print(document['sku'])
        # print(line)
        es.index(index='products', id = document['sku'], body = document)
        print("Done reading json file ", document['sku'])