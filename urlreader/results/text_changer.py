import json

def changer(text):
    for i in text.values():
        i = str(i)
        i = i+' ' 

    i = i.replace('[' , '')
    i = i.replace(',' , '')
    i = i.replace('\'' , '')
    i = i.replace(']' , '')

    return i
