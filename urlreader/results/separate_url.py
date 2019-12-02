import json
import re

def separate_url(jsondata,tf=True):
    json_list = []
    if tf == True:
        for i in jsondata:
            search = re.search(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-]+', i)
            if search == None:
                pass
            else:
                json_list.append(search.group())
    else:
        for i in jsondata:
            json_list.append(i)
    return json_list
