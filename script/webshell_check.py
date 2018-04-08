import os
import sys,os,re
sys.path.append('C:\Users\Administrator.SG-20170616FAOE\Desktop\PYSCANER\scanner-based-spider')
from lib.core import downloader
filename = os.path.join(sys.path[0],"C:\Users\Administrator.SG-20170616FAOE\Desktop\PYSCANER\scanner-based-spider\data","webshell.dic")
payload = []
f = open(filename)
a = 0
for i in f:
    payload.append(i.strip())
    a=a+1
    if(a==999):
        break
class spider:
    def run(self,url,html):
        if(not url.endswith(".php")):
            print url," : webshellcheck finished!"
            return False
        print "[webshell check]:",url
        post_data = {}
        for _payload in payload:
            post_data[_payload] = 'echo "password is %s";'%_payload
            r = downloader.downloader()
            res = r.post(url,post_data)
            # print _payload
            # print res
            if(res.find(_payload)==1):
                print ("webshell:%s"%res)
                return True
        print url, " : webshellcheck finished!"
        return False