# -*- coding:utf-8 -*-
"""
* Author      : wangpeng
* Email       : wangpeng@cnpc.com.cn
* Create time : 2024/03/02 21:48
* File name   : time_util
* Reference   :
* Description : 时间工具类
"""
import time

class Timer:
    def __init__(self):
        self.start_time = None

    def start(self):
        self.start_time = time.time()

    def elapsed_time(self):
        if self.start_time is None:
            raise ValueError("Timer is not started. Call start() first.")
        return f'{time.time() - self.start_time: .2f} s'
