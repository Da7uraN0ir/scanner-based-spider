import json,os,sys,hashlib,threading,Queue
from lib.core import downloader
class webcms(object):
    workqueue = Queue.Queue()
    url = ""
    threadnum = 0
    notfound = True
    download = downloader.downloader()
    result = ""
    def __init__(self,url,threadnum = 10):
        self.url = url
        self.threadnum = threadnum
        filename = os.path.join(sys.path[0],"data","data.json")
        fp = open(filename)
        webdata = json.load(fp,encoding="utf-8")
        for i in webdata:
            self.workqueue.put(i)
        fp.close()
    def getmd5(self,body):
        m2 = hashlib.md5()
        m2.update(body)
        return m2.hexdigest()
    def th_whatweb(self):
        if(self.workqueue.empty()):
            self.notfound = False
            return False
        if(self.notfound is False):
            return False
        cms = self.workqueue.get()
        _url = self.url + cms["url"]
        html = self.download.get(_url)
        print "[whatweb log]:checking %s"%_url
        if(html is None):
            return False
        if cms["re"]:
            if(html.find(cms["re"])!=-1):
                self.result = cms["name"]
                self.notfound = False
                return True
        else:
            md5 = self.getmd5(html)
            if(md5==cms["md5"]):
                self.result = cms["name"]
                self.notfound = False
                return True
    def run(self):
        try:
            while(self.notfound):
                th = []
                for i in range(self.threadnum):
                    t = threading.Thread(target=self.th_whatweb)
                    t.start()
                    th.append()
                for t in th:
                    t.join()
            if(self.result):
                print "[webcms]:%s cms is %s"%(self.url,self.result)
            else:
                print "[webcms]:%s cms notfound!"%self.url
        except Exception,e:
            print (e)