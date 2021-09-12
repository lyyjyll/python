import requests
import pandas as pd
import numpy as np
from lxml import etree

def read_table(url_table):
    df = pd.read_csv(url_table)
    #print(df.head(5))
    proxy_list = np.array(df.iloc[:,[1]]).flatten().tolist()
    return proxy_list


def visit_web(url,proxy):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}

    proxies = {'http':'http://{ip}'.format(ip=proxy),'https':'https://{ip}'.format(ip=proxy)}

    try:
        response = requests.get(url,headers=headers,proxies=proxies,timeout=5)
        if response.status_code == 200:
            print(proxy)
            response.encoding = 'utf-8'
            html = etree.HTML(response.text)
            info = html.xpath('/html/body/p[1]//text()')
            print(info())

    except Exception as e:
        pass
        #print('错误异常信息为：',e)

def test_proxy(proxy_list,url='https://www.baidu.com'):

    for pro in proxy_list:

        visit_web(url,pro)

if __name__ == '__main__':
    urltable = './nima_proxy.csv'
    proxylist = read_table(urltable)

    test_proxy(proxylist,url='http://www.xiladaili.com/https/')