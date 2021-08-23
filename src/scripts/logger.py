import json
import os
from .colors import logcolors
from . import filechange

buildpath = os.path.join(os.path.dirname(os.getcwd()) , 'build')
if(not os.path.isdir(buildpath)):
    jsonpath = os.path.join(os.getcwd(), 'public','tmp.json')
else:
    jsonpath = os.path.join(buildpath ,'tmp.json')

buffer = []


def writedata(*args, **kwargs):
    data = {}
    global buffer
    readdata = []
    updatedbuffer = kwargs.get('buffer', -1)
    path = kwargs.get('path', None)
    diff = kwargs.get('diff', None)
    if(updatedbuffer != -1):
        buffer = updatedbuffer
        with open(jsonpath, 'w') as file:
            json.dump([obj for obj in buffer], file, indent=4)
    elif(path and diff):
        data['path'] = path
        data['changes'] = diff
        with open(jsonpath , 'r') as file:
            readdata = json.load(file)
        with open(jsonpath, 'w') as file:
            readdata.append(data)
            json.dump(readdata, file, indent=4)


def updatedata(idx):
    if(os.path.getsize(jsonpath) > 0):
        with open(jsonpath, 'r') as file:
            readdata = json.load(file)
        if(len(readdata) == 0):
            print('No changed file left')
        else:
            tmpdata = readdata.copy()
            print('Found some changed files')
            del tmpdata[idx]
            writedata(buffer=tmpdata)

    else:
        print('No data to read')


def checkdata(path):
    if(os.path.getsize(jsonpath) > 0):
        with open(jsonpath, 'r') as file:
            initdata = json.load(file)
        if(len(initdata) == 0):
            print(f'{logcolors.SUCCESS}Change tree clean{logcolors.ENDC}')
        else:
            print(f'{logcolors.SUCCESS}Found Some Changes{logcolors.ENDC}')
            
        filechange.ischanged(path)
    else:
        print(f'{logcolors.ERROR}No changes found from previous session{logcolors.ENDC}')
