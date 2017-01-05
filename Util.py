#coding=utf-8

import urllib
import hashlib
import hmac
import base64

#在此添加您的key
ACCESS_KEY="f5ca5300-8657051e-0b37292b-2680043f"
SECRET_KEY="983691ad-7925f03c-08010420-02ac1921"


def signature(params):
    params = sorted(params.iteritems(), key=lambda d:d[0], reverse=False)
    message = urllib.urlencode(params)
    m = hashlib.md5()
    m.update(message)
    m.digest()
    sig=m.hexdigest()
    return sig