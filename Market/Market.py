# coding=utf-8
__author__ = 'qinfeizhang'

import requests


class Market:
    def __init__(self):
        pass

    '''
    得到tick数据
    @param url
    '''

    @staticmethod
    def get_ticker_week(url):
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            return data
        else:
            return None

    '''
    得到行情深度
    @param url
    '''

    @staticmethod
    def get_depths_week(url):
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            return data
        else:
            return None

    '''
    得到成交数据
    @param url
    '''

    @staticmethod
    def get_trades_week(url):
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            return data
        else:
            return None

    '''
    得到价格指数
    @param url
    '''

    @staticmethod
    def get_index_price(url):
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            return data
        else:
            return None

    '''
    得到汇率
    @param url
    '''

    @staticmethod
    def get_exchange_rage(url):
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            return data
        else:
            return None
