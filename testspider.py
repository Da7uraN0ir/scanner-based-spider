#!/usr/bin/Python
from lib.core.spider import spidermain
def main():
    url = "http://localhost/wordpress"
    tnum = 10
    test = spidermain(url,tnum)
    test.craw()
if __name__=='__main__':
    main()
