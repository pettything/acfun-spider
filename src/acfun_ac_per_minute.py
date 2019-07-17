# -*- coding: UTF-8 -*-
#!/usr/bin/python

import requests
import datetime
import time
import csv
import os

path = os.path.abspath(os.path.join(
    os.getcwd(),'..','csv'))
acid = 100000000
per_minute = 10


def doSth():
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN',
        'Connection': 'Keep-Alive',
        'Cookie': '',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
    }
    response = requests.get(
        'https://www.acfun.cn/content_view.aspx?contentId='+str(acid), headers=headers)
    if response.status_code == requests.codes.ok:
        with open(os.path.abspath(os.path.join(path, 'ac'+str(acid)+'.csv')), "a+", newline='', encoding="utf-8") as f:
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
            result = [(now+','+response.text[1:-1],)]
            print(result)
            f_csv = csv.writer(f)
            f_csv.writerows(result)


def main():
    while True:
        # 判断是否达到设定时间，例如23:00
        while True:
            now = datetime.datetime.now()
            # 到达设定时间，结束内循环
            if now.minute % int(per_minute) == 0:
                break
            # 不到时间就等20秒之后再次检测
            time.sleep(20)
        # 做正事
        doSth()
        time.sleep(60)


if __name__ == '__main__':
    acid = input('请输入要爬取数据的ac号:')
    per_minute = input('请输入爬取频率(分钟):')
    main()
