import requests
from multiprocessing import Pool
import datetime

url = "http://127.0.0.1:9000/"
def send_requests(data):
    r = requests.get(url,
         params={'name': 'test', 'a': 1, 'b': 2})

r = requests.get(url,
        params={'name': 'test', 'a': 1, 'b': 2})
print r.text

pool = Pool(100)
a = datetime.datetime.now()
pool.map(send_requests, xrange(1, 10000))
b = datetime.datetime.now()
print b - a


