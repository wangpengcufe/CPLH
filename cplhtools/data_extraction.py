# -*- coding:utf-8 -*-
"""
* Author      : wangpeng
* Email       : wangpeng@cnpc.com.cn
* Create time : 2024/3/1 16:49
* File name   : data_extraction
* Reference   :
* Description : 数据提取
"""
from cplhtools import DB
import logging as logger
import pandas as pd

def query_by_sql(sql):
    db = DB()
    cursor = db.get_cursor()
    logger.info(sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    column_names = [column[0] for column in cursor.description]
    result_df = pd.DataFrame(result, columns=column_names)
    return result_df

if __name__ == '__main__':
    sql = 'select * from HDB_ALARM limit 1'
    data = query_by_sql(sql)
    print(data)
