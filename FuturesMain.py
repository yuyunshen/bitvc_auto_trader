# coding=utf-8

from trader.Trader import *
from config import Config

if __name__ == "__main__":
    print "获取期货资产信息"
    print Trader.get_balance_info(1, Config.FUTURES_BALANCE_INFO)
    print "获取用户持仓记录，week 周 quarter 季"
    print Trader.get_hold_order_list(1, "week", Config.FUTURES_HOLD_ORDER_LIST)
    print "获取用户持仓记录，汇总"
    print Trader.get_hold_order_sum(1, "week", Config.FUTURES_HOLD_ORDER_SUM)
    print "获取所有正在进行的委托"
    print Trader.get_hold_order_list(1, "week", Config.FUTURES_ORDERS_LIST)
    print "委托单详情"
    print Trader.get_order_info(3757870, 1, "week", Config.FUTURES_ORDER_INFO)
    print "下委托单"
    price = 2470
    money = 100
    # 1开2平，1买2卖
    print Trader.save_order(1, "week", 1, 1, price, money, 10, Config.FUTURES_ORDER_SAVE)
    print "取消订单接口"
    print Trader.cancel_order(1, "week", 3757870, Config.FUTURES_CANCEL_ORDER)
