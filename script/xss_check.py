#-*- coding:utf-8 -*-
import sys,os,re
sys.path.append('C:\Users\Administrator.SG-20170616FAOE\Desktop\PYSCANER\scanner-based-spider')
from lib.core import downloader,common

payload = []
filename = os.path.join(sys.path[0],"data","xsspayload.txt")
f = open(filename)
for i in f:
    # print i.strip()
    payload.append(i.strip())
class spider():
    def run(self,url,html):
        download = downloader.downloader()
        urls = common.urlsplit(url)
        if urls is None:
            print url + " : xsscheck finished!"
            return False
        for _urlp in urls:
            for _payload in payload:
                _url = _urlp.replace("my_payload",_payload)
                print "[xss test]:",_url
                _str = download.get(url)
                if str is None:
                    return False
                if(_str.find(_payload)!=-1):
                    print "xss found:%s"%url
        return False