# -*- coding:utf-8 -*-
"""
* Author      : wangpeng
* Email       : wangpeng@cnpc.com.cn
* Create time : 2024/3/1 16:48
* File name   : db_util
* Reference   :
* Description : 数据库连接工具类
"""
import pymysql
import configparser
import os

class DB:
    """数据库连接"""

    _instance = None

    def __new__(cls, config_file=None):
        if config_file is None:
            # config_file = os.path.join(os.path.dirname(__file__), '..', 'conf', 'database_config.ini')  # 开发环境
            config_file = '/data/cplhtools/conf/database_config.ini'  # 服务器环境

        if cls._instance is None:
            cls._instance = super(DB, cls).__new__(cls)
            cls._instance.config = configparser.ConfigParser()

            cls._instance.config.read(config_file)
            print("Initializing database configuration from ", config_file)
            database_name = cls._instance.config.get('Doris', 'database')
            print("Database name:", database_name)

            db_config = cls._instance.config['Doris']
            cls._instance.connection = pymysql.connect(
                host=db_config.get('host'),
                port=db_config.getint('port'),
                user=db_config.get('username'),
                password=db_config.get('password'),
                database=db_config.get('database')
            )
        return cls._instance

    def get_connection(self):
        return self.connection

    def get_cursor(self):
        return self.get_connection().cursor()
