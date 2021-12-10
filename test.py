import grequests
from datetime import datetime
import requests


urls = [
    'https://zhm5v3fgp5.execute-api.us-east-2.amazonaws.com/dev/getcats?cat_id=3',
    'https://zhm5v3fgp5.execute-api.us-east-2.amazonaws.com/dev/getbreeders',
]


def t1():
    s = datetime.now()
    rs = (grequests.get(u) for u in urls)
    x = grequests.map(rs)
    e = datetime.now()

    print("T1")
    print("Elapsed time = ", e-s)
    print(x)
    for r in x:
        print(r.url, r.status_code, r.json()['message']['data'])



t1()
