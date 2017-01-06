# coding=utf-8

import time
import requests
import urllib

from util import Util
from config import Config


class Trader:
    '''
    获取期货资产详情
    @param coinType
    '''


    def __init__(self):
        pass

    @staticmethod
    def get_balance_info(coinType, url):
        timestamp = long(time.time())
        params = {"accessKey": Config.ACCESS_KEY, "secretKey": Config.SECRET_KEY, "created": timestamp,
                  "coinType": coinType}
        sign = Util.signature(params)
        params['sign'] = sign
        del params['secretKey']

        payload = urllib.urlencode(params)
        headers = {"content-type": "application/x-www-form-urlencoded"}
        r = requests.post(url, params=payload, headers=headers)
        if r.status_code == 200:
            data = r.json()
            return data
        else:
            return None

    '''
    获取用户持仓记录
    @param coinType
    @param contractType
    '''
    @staticmethod
    def get_hold_order_list(coinType, contractType, url):
        timestamp = long(time.time())

        params = {"accessKey": Config.ACCESS_KEY, "secretKey": Config.SECRET_KEY, "created": timestamp,
                  "coinType": coinType}
        sign = Util.signature(params)
        params['sign'] = sign
        del params['secretKey']
        params['contractType'] = contractType
        payload = urllib.urlencode(params)
        headers = {"content-type": "application/x-www-form-urlencoded"}
        r = requests.post(url, params=payload, headers=headers)
        if r.status_code == 200:
            data = r.json()
            return data
        else:
            return None

    '''
    获取用户持仓记录（汇总）
    @param coinType
    @param contractType
    '''
    @staticmethod
    def get_hold_order_sum(coinType, contractType, url):
        timestamp = long(time.time())
        params = {"accessKey": Config.ACCESS_KEY, "secretKey": Config.SECRET_KEY, "created": timestamp,
                  "coinType": coinType}
        sign = Util.signature(params)
        params['sign'] = sign
        del params['secretKey']
        params['contractType'] = contractType
        payload = urllib.urlencode(params)
        headers = {"content-type": "application/x-www-form-urlencoded"}
        r = requests.post(url, params=payload, headers=headers)
        if r.status_code == 200:
            data = r.json()
            return data
        else:
            return None

    '''
    获取所有正在进行的委托
    @param coinType
    @param contractType
    '''
    @staticmethod
    def get_order_list(coinType, contractType, url):
        timestamp = long(time.time())
        params = {"accessKey": Config.ACCESS_KEY, "secretKey": Config.SECRET_KEY, "created": timestamp,
                  "coinType": coinType}
        sign = Util.signature(params)
        params['sign'] = sign
        del params['secretKey']
        params['contractType'] = contractType

        payload = urllib.urlencode(params)
        headers = {"content-type": "application/x-www-form-urlencoded"}
        r = requests.post(url, params=payload, headers=headers)
        if r.status_code == 200:
            data = r.json()
            return data
        else:
            return None

    '''
    委托单详情
    @param id
    @param coinType
    @param contractType
    '''
    @staticmethod
    def get_order_info(id, coinType, contractType, url):
        timestamp = long(time.time())
        params = {"accessKey": Config.ACCESS_KEY, "secretKey": Config.SECRET_KEY, "created": timestamp,
                  "coinType": coinType,
                  "id": id,
                  'contractType': contractType}
        sign = Util.signature(params)
        params['sign'] = sign
        del params['secretKey']

        payload = urllib.urlencode(params)
        headers = {"content-type": "application/x-www-form-urlencoded"}
        r = requests.post(url, params=payload, headers=headers)
        if r.status_code == 200:
            data = r.json()
            return data
        else:
            return None

    '''
    开仓
    @param coinType
    @param contractType
    @param orderType
    @param tradeType
    @param price
    @param money
    @param leverage
    '''
    @staticmethod
    def save_order(coinType, contractType, orderType, tradeType, price, money, leverage, url):
        timestamp = long(time.time())
        params = {"accessKey": Config.ACCESS_KEY, "secretKey": Config.SECRET_KEY, "created": timestamp, "coinType": coinType,
                  "orderType": orderType, "tradeType": tradeType, "price": price, "money": money,
                  "contractType": contractType}
        sign = Util.signature(params)
        params['sign'] = sign
        del params['secretKey']
        params['leverage'] = leverage
        params['tradePassword'] = 'Dawning@123'

        payload = urllib.urlencode(params)
        headers = {"content-type": "application/x-www-form-urlencoded"}
        r = requests.post(url, params=payload, headers=headers)
        if r.status_code == 200:
            data = r.json()
            return data
        else:
            return None

    '''
    撤销订单
    @param id
    @param coinType
    @param contractType
    '''
    @staticmethod
    def cancel_order(coinType, contractType, id, url):
        timestamp = long(time.time())
        params = {"accessKey": Config.ACCESS_KEY, "secretKey": Config.SECRET_KEY, "created": timestamp, "coinType": coinType,
                  "id": id,
                  "contractType": contractType}
        sign = Util.signature(params)
        params['sign'] = sign
        del params['secretKey']

        payload = urllib.urlencode(params)
        headers = {"content-type": "application/x-www-form-urlencoded"}
        r = requests.post(url, params=payload, headers=headers)
        if r.status_code == 200:
            data = r.json()
            return data
        else:
            return None
