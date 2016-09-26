import gevent
from gevent import monkey
monkey.patch_all()
from gevent.pool import Pool
import random
import requests

names = ['Ashiwn', 'Rags', 'Venkatesh', 'Vivek', 'Chandra', 'Abhi', 'Trey']

def func():
    name = random.choice(names)
    r = requests.get('http://127.0.0.1:9007/happy?name=' + name)
    print r.text

gpool = Pool(100)

while True:
    gpool.spawn(func)
