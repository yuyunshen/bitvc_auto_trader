# coding=utf-8

from trader.Trader import *
from market.Market import Market
from config import Config
import time


# order_type=1那么平多单，order_type=2那么平空单
def close_all_trades(order_type):
    order_list = Trader.get_order_list(1, "week", Config.FUTURES_HOLD_ORDER_LIST)
    market_tick = Market.get_ticker_week(Config.FUTURES_TICKER_MD)
    limit_lowest_price = float(market_tick['limit_lowest_price']) + 50
    limit_highest_price = float(market_tick['limit_highest_price']) - 50

    for i in range(len(order_list['week'])):
        amount = order_list['week'][i]['money']
        # 如果是空单，那么平仓
        if order_list['week'][i]['tradeType'] == 2 and order_type == 2:
            print '-----close short----'
            print Trader.save_order(1, "week", 2, 1, limit_highest_price, amount, 10, Config.FUTURES_ORDER_SAVE)

        # 如果是多单，那么平仓
        if order_list['week'][i]['tradeType'] == 1 and order_type == 1:
            print '-----close long------'
            print Trader.save_order(1, "week", 2, 2, limit_lowest_price, amount, 10, Config.FUTURES_ORDER_SAVE)


if __name__ == "__main__":

    ma_slow = -1.0
    ma_fast = -1.0

    # 长短均线周期，秒
    fast_length = 180.0
    slow_length = 600.0
    count = 0

    TRADE_TYPE_LONG = 1
    TRADE_TYPE_SHORT = 2

    ORDER_TYPE_OPEN = 1
    ORDER_TYPE_CLOSE = 2

    while 1:

        try:
            # 如果有挂单，将现有订单全部取消
            hold_orders = Trader.get_hold_order_list(1, "week", Config.FUTURES_ORDERS_LIST)
            for i in range(len(hold_orders['week'])):
                Trader.cancel_order(1, "week", hold_orders['week'][i]['id'], Config.FUTURES_CANCEL_ORDER)

            # 获取当前最新价
            cur_last = float(Market.get_ticker_week(Config.FUTURES_TICKER_MD)['last'])

            # 保存均线上一时刻的状态
            ma_slow_old = ma_slow
            ma_fast_old = ma_fast

            if ma_slow < 0 or ma_fast < 0:
                ma_slow = cur_last
                ma_fast = cur_last
            else:
                # 更新均线
                ma_slow = ma_slow * (slow_length - 1) / slow_length + cur_last / slow_length
                ma_fast = ma_fast * (fast_length - 1) / fast_length + cur_last / fast_length

            if count > slow_length:
                # 快速均线上穿
                if ma_fast_old < ma_slow_old and ma_fast > ma_slow:
                    # 如果有空单，先平掉
                    close_all_trades(2)
                    # 开多单
                    print '-------buy--------'
                    print 'ma_slow: ' + str(ma_slow) + '   ma_fast: ' + str(ma_fast)
                    print 'old_ma_slow: ' + str(ma_slow_old) + '   old_ma_fast: ' + str(ma_fast_old)
                    print Trader.save_order(1, "week", 1, 1, cur_last + 10, 1000, 10, Config.FUTURES_ORDER_SAVE)

                # 快速均线下穿
                if ma_fast_old > ma_slow_old and ma_fast < ma_slow:
                    close_all_trades(1)
                    # 如果有多单，那么先平仓，在开空单
                    print '-------sell-------'
                    print 'ma_slow: ' + str(ma_slow) + '   ma_fast: ' + str(ma_fast)
                    print 'old_ma_slow: ' + str(ma_slow_old) + '   old_ma_fast: ' + str(ma_fast_old)
                    print Trader.save_order(1, "week", 1, 2, cur_last - 10, 1000, 10, Config.FUTURES_ORDER_SAVE)
        except Exception, e:
            print(e)

        count += 1
        time.sleep(1)
