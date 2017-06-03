#!/usr/bin/python
#-*- coding:utf8 -*-

from multiprocessing import Process,Manager
import requests
from  bs4 import BeautifulSoup
import random
import re
import time

#子进程代码
def write_data_proc(dest_url_no,dest_url_over,dest_ftp_path,dest_file):
    time.sleep(1)
    num = random.randint(1,100)
    print('子进程开始执行--%d'%num)
    dest_url_file = dest_file["dest_url_file"]
    dest_ftp_file = dest_file["dest_ftp_file"]
    dest_url_handle = open(dest_url_file,"a+",encoding="utf-8")
    dest_ftp_handle = open(dest_ftp_file,"a+",encoding="utf-8")
    while len(dest_url_no) > 0:
        dest_url = dest_url_no.pop(0)
        try:
            reponse = requests.get(dest_url,timeout=1.0)
        except (TimeoutError,ConnectionError,requests.exceptions.ReadTimeout,requests.exceptions.ConnectionError,requests.exceptions.InvalidURL):
            continue
        reponse.encoding = 'gb2312'
        soup = BeautifulSoup(reponse.text,"html.parser")
        for tag in soup.find_all(re.compile(r"^a")):
            if "href" in  tag.attrs:
                if tag.attrs["href"][0:3] == "ftp":
                    #获取分析出的ftp地址
                    ftp_path = tag.attrs["href"]
                    #判断ftp_path是否已经存在于dest_ftp_path中
                    if ftp_path not in dest_ftp_path:
                        dest_ftp_path.append(ftp_path)
                        #将ftp_path写入到文件中
                        dest_ftp_handle.write(ftp_path+"\n")
                else:
                    #普通的url
                    url_path = tag.attrs["href"]
                    #url过滤条件
                    if url_path[0:4] == "http" or url_path[0:4] == "#" or url_path[0:4] =="/":
                        continue
                    if url_path[0:10] == "index.html" or url_path[0:10] == "javascript":
                        continue
                    if url_path[0:8] == "/support" or url_path[0:8] == "/webPlay" :
                        continue
                    if (url_path.find("game") != -1) or (url_path.find("magnet:?xt") != -1) or (url_path.find("thunder") != -1) or(url_path.find("ed2k://") != -1):
                        continue
                    url_path = "http://....."+url_path
                    #检测该url是否经过处理
                    if (url_path not in dest_url_over) and (url_path not in dest_url_no):
                        dest_url_no.append(url_path)
                        #将获取的url写入到文件中
                        dest_url_handle.write(url_path+"\n")
        #将处理完毕的url添加到dest_url_over中
        dest_url_over.append(dest_url)
    print("子进程执行完毕--%d"%num)


if __name__=='__main__':

    print("主进程开始执行")
    manager = Manager()

    #还没有处理的url
    dest_url_no = manager.list()
    dest_url = "http://"
    dest_url_no.append(dest_url)

    #已经处理完毕的url
    dest_url_over = manager.list()

    #获取到的ftp地址
    dest_ftp_path = manager.list()

    #url/ftp存储文件
    dest_file = manager.dict()
    dest_file = {"dest_url_file":"./movic_url_bak.txt","dest_ftp_file":"./movic_ftp_bak.txt"}

    #创建过个子进程
    process_list = [];
    for i in range(10):
        p = Process(target=write_data_proc, args=(dest_url_no,dest_url_over,dest_ftp_path,dest_file))
        p.start()
        process_list.append(p)
    for item in process_list:
        item.join()
    print('执行完毕')