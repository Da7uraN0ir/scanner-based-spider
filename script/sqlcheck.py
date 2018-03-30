#-*- coding:utf-8 -*-
import re,random
import sys
sys.path.append('C:\Users\Administrator.SG-20170616FAOE\Desktop\PYSCANER\scanner-based-spider')
from lib.core import downloader
class spider:
    def run(self,url,html):
        if(not url.find("?")):
            return False
        download = downloader.downloader()
        BOOLEAN_TESTS = (" AND %d=%d","OR NOT (%d=%d)")
        DBMS_ERRORS = {  # regular expressions used for DBMS recognition based on error message response
            "MySQL": (r"SQL syntax.*MySQL", r"Warning.*mysql_.*", r"valid MySQL result", r"MySqlClient\."),
            "PostgreSQL": (r"PostgreSQL.*ERROR", r"Warning.*\Wpg_.*", r"valid PostgreSQL result", r"Npgsql\."),
            "Microsoft SQL Server": (
            r"Driver.* SQL[\-\_\ ]*Server", r"OLE DB.* SQL Server", r"(\W|\A)SQL Server.*Driver", r"Warning.*mssql_.*",
            r"(\W|\A)SQL Server.*[0-9a-fA-F]{8}", r"(?s)Exception.*\WSystem\.Data\.SqlClient\.",
            r"(?s)Exception.*\WRoadhouse\.Cms\."),
            "Microsoft Access": (r"Microsoft Access Driver", r"JET Database Engine", r"Access Database Engine"),
            "Oracle": (r"\bORA-[0-9][0-9][0-9][0-9]", r"Oracle error", r"Oracle.*Driver", r"Warning.*\Woci_.*",
                       r"Warning.*\Wora_.*"),
            "IBM DB2": (r"CLI Driver.*DB2", r"DB2 SQL error", r"\bdb2_\w+\("),
            "SQLite": (
            r"SQLite/JDBCDriver", r"SQLite.Exception", r"System.Data.SQLite.SQLiteException", r"Warning.*sqlite_.*",
            r"Warning.*SQLite3::", r"\[SQLITE_ERROR\]"),
            "Sybase": (r"(?i)Warning.*sybase.*", r"Sybase message", r"Sybase.*Server message.*"),
        }
        # with open("sqldict.txt", "rb") as fd:
        #     sqlerr = None
        #     for line in fd:
        #         line = line.strip()
        #         if ':' in line:
        #             sqlerr = re.findall(r'\(.*\)',line)[0]
        #             # print ('sqlerr:'+sqlerr)
        #             sqltype = re.findall(r'\".*?\"',line)[0]
        #             # print ("sqltype"+sqltype)
        #             DBMS_ERRORS.setdefault(sqltype, sqlerr)
        #         else:
        #             continue
        # print(json.dumps(DBMS_ERRORS, indent = 1).decode("unicode-escape"))
        _url = url + "%29%28%22%27" # )("'
        _content = download.get(_url)
        for (dbms, err) in ((dbms, err) for dbms in DBMS_ERRORS for err in DBMS_ERRORS[dbms]):
            if(_content):
                if(re.search(err,_content)):
                    return True
            # else:
            #     print (_url+":status_code!=200")
        content = {}
        content["origin"] = download.get(url)
        for test_payload in BOOLEAN_TESTS:
            RANDINI = random.randint(1,255)
            _url = url + test_payload%(RANDINI,RANDINI)
            content["ture"] = download.get(_url)
            _url = url +test_payload%(RANDINI,RANDINI+1)
            content["false"] = download.get(_url)
            if content["origin"]==content["ture"]!=content["false"]:
                return "sql found: %s"%url
        print (url+" : sqlcheck finish!")