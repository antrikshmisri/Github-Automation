import json
import os
from .colors import logcolors
from . import filechange

buildpath = os.path.join(os.getcwd() , 'build')
jsonpath = ''
if(not os.path.isdir(buildpath)):
    jsonpath = os.path.join(os.getcwd(), 'public','tmp.json')
else:
    jsonpath = os.path.join(os.getcwd() , 'build','tmp.json')


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


def updatedata(file, diff):
    if(os.path.getsize(jsonpath) > 0):
        with open(jsonpath, 'r') as file:
            readdata = json.load(file)
        if(len(readdata) == 0):
            print('No changed file left')
        else:
            tmpdata = readdata.copy()
            print('Found some changed files')
            for obj in readdata:
                if obj['path'] == file and obj['changes'] == diff:
                    tmpdata.remove(obj)
            writedata(buffer=tmpdata)

    else:
        print('No data to read')


def checkdata(url , branch ,path):
    if(os.path.getsize(jsonpath) > 0):
        with open(jsonpath, 'r') as file:
            initdata = json.load(file)
        if(len(initdata) == 0):
            print(f'{logcolors.SUCCESS}Change tree clean{logcolors.ENDC}')
            filechange.ischanged( url , branch , path)
        else:
            print(f'{logcolors.SUCCESS}Found Some Changes{logcolors.ENDC}')
            filechange.ischanged( url , branch , path)
    else:
        print(f'{logcolors.ERROR}No changes found from previous session{logcolors.ENDC}')
