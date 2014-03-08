import requests
from multiprocessing import Pool
import datetime


def send_requests(data):
    # r = requests.get("http://127.0.0.1:8888/")
    r = requests.get("http://127.0.0.1:9000/")
    # r = requests.get("http://127.0.0.1:8080/")

pool = Pool(100)
a = datetime.datetime.now()
pool.map(send_requests, xrange(1, 10000))
b = datetime.datetime.now()
print b - a


