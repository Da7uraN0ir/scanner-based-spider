import os
import sys
sys.path.append('C:\Users\Administrator.SG-20170616FAOE\Desktop\PYSCANER\scanner-based-spider\script')
class spiderplus(object):
    def __init__(self,plugin,disallow=[]):
        self.dir_exploit = []
        self.disallow = ['__init__']
        self.disallow.extend(disallow)
        self.plugin = os.getcwd()+'/'+plugin
    def list_plusg(self):
        def fliter_func(file):
            if not file.endswith(".py"):
                return False
            for disfile in self.disallow:
                if disfile in file:
                    return False
            return True
        dir_exploit = filter(fliter_func,os.listdir(self.plugin))
        return list(dir_exploit)
    def work(self,url,html):
        for _plugin in self.list_plusg():
            try:
                m = __import__(_plugin.split('.')[0])
                spider = getattr(m,'spider')
                p = spider()
                s = p.run(url,html)
            except Exception,e:
                print (e)
            # m = __import__(_plugin.split('.')[0])
            # spider = getattr(m, 'spider')
            # p = spider()
            # s = p.run(url, html)