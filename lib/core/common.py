import re
def urlsplit(url):
    if re.search(url,"?"):
        domain = url.split("?")[0]
        _url = url.split("?")[1]
        pararm = {}
        for val in _url.split("&"):
            pararm[val.split("=")[0]] = val.split("=")[-1]

        #combine
        urls = []
        for val in pararm.values():
            new_url = domain +_url.replace(val,"my_payload")
            urls.append(new_url)
        return urls
    return None