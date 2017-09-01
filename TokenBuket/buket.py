# coding:utf-8
import time
import threading

__doc__ = """
假如用户配置的平均发送速率为r，则每隔1/r秒一个令牌被加入到桶中（每秒会有r个令牌放入桶中）；

假设桶中最多可以存放b个令牌。如果令牌到达时令牌桶已经满了，那么这个令牌会被丢弃；

当一个n个字节的数据包到达时，就从令牌桶中删除n个令牌（不同大小的数据包，消耗的令牌数量不一样），并且数据包被发送到网络；

如果令牌桶中少于n个令牌，那么不会删除令牌，并且认为这个数据包在流量限制之外（n个字节，需要n个令牌。该数据包将被缓存或丢弃）；

算法允许最长b个字节的突发，但从长期运行结果看，数据包的速率被限制成常量r。对于在流量限制外的数据包可以以不同的方式处理：
  （1）它们可以被丢弃；
  （2）它们可以排放在队列中以便当令牌桶中累积了足够多的令牌时再传输；
  （3）它们可以继续发送，但需要做特殊标记，网络过载的时候将这些特殊标记的包丢弃。
"""


class Token(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            _instance = object.__new__(cls, *args, **kwargs)
            cls._instance = _instance
            cls._instance.__dict__['size'] = 2
            cls._instance.__dict__['token_last'] = 0
            cls._instance.__dict__['time_limit'] = 10
            cls._instance.__dict__['last_check'] = time.time()

        return cls._instance

    def __init__(self):
        pass

    def get_token(self):
        with threading.Lock():
            now = time.time()
            inteval = now - self.last_check
            add_tokens = int(inteval * self.size / self.time_limit)
            tokens = self.token_last + add_tokens
            self.token_last = tokens if tokens < self.size else self.size

            if self.token_last >= 1:
                self.last_check = now  # while get token successed, update check time
                self.token_last -= 1
                return True

            else:
                return False



