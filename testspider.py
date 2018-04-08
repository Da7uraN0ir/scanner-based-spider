#!/usr/bin/Python
import sys
from lib.core.spider import spidermain
from lib.core import webcms,common,portscan
reload(sys)
sys.setdefaultencoding('utf-8')
def main():
    url = "http://localhost/wordpress/wp-login.php"
    tnum = 10
    ip = common.gethostbyname(url)
    print "IP:",ip
    print "Start Port Sccan:"
    pp = portscan.portscan(ip)
    pp.work()
    #webcms
    ww = webcms.webcms(url,tnum)
    ww.run()
    #spider
    test = spidermain(url,tnum)
    test.craw()
if __name__=='__main__':
    main()
