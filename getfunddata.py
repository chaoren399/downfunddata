#!/usr/bin/python
# -*- coding: utf8 -*-

import pandas as pd
import urllib2
import json
import time
import logging
import os

f_path = os.path.dirname(os.path.abspath(__file__))

def getdata(fundpool_path):
#1. 打开基金池表格
    df_1 = pd.read_csv(fundpool_path,dtype=object)



    # print 'df_1', df_1
    df_1.columns = ['order', 'code','name','tar_value','net_value','jzrq','zhongdian','url','pingji','guimo',
                    'chenglirq']



#2.  将表格数据与 互联网基金净值 合并成 pd 格式.
    # print  df_1
    for index ,row in df_1.iterrows():
        # print row['code']

        'http://fundgz.1234567.com.cn/js/000172.js'

        code = row['code'].zfill(6)
        # code = '0001721'

        df_1.iloc[index, 1] = code  # 把 776转成 000776

        jsondata = getNetValue(code)


        jsondata =  jsondata[8:-2]
        jsondata = json.loads(jsondata)
        netValue = jsondata['dwjz'] # 净值
        jzrq= jsondata['jzrq'] # 日期


        f = open(f_path+'/data/' + code + '.csv', 'a+')

        f.write(jzrq + ',' + netValue+ '\n')
        logging.warning('writer data' + '--' + jzrq+'--'+netValue )
        f.close()




'http://fundgz.1234567.com.cn/js/001186.js'

def getNetValue(fundcode):
    try:
        url = 'http://fundgz.1234567.com.cn/js/' + str(fundcode) + '.js'

        time.sleep(1)
        request = urllib2.Request(url)
        response = urllib2.urlopen(url = request,timeout=15)
        return response.read().decode('utf-8')

    except urllib2.URLError, e:
        if hasattr(e, "reason"):
            print u"获取基金数据失败,错误原因", e.reason
            logging.error(fundcode+'--'+e.reason)
            return None

    # print  array
if __name__ == '__main__':

    '/Users/zzy/PycharmProjects/python-workspace/downfunddata/基金池.csv'

    logging.basicConfig(level=logging.WARNING,  # 控制台打印的日志级别
                        filename=f_path+'/fund.log',
                        filemode='a',  ##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                        # a是追加模式，默认如果不写的话，就是追加模式
                        format=
                        '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                        # 日志格式
                        )

    fundpool_path = os.path.dirname(os.path.abspath(__file__))
    fundpool_path = fundpool_path+'/基金池.csv'
    print fundpool_path
    getdata(fundpool_path)