
from .diffcalc import *
from .ignore import getIgnoreFiles
from .utils import getNestedFiles, read_file
import time


def ischanged(url, branch, path):
    from .logger import writedata
    ignoredirs = getIgnoreFiles(path)
    # gets the list of all nested files
    onlyfiles = getNestedFiles(path,ignoredirs)
    # if uncommited data found perform git commands on them
    initial = list(read_file(onlyfiles))
    while True:
        current = list(read_file(onlyfiles))
        changeditem = []
        previtem = []
        time.sleep(5)
        if(current != initial):
            # Calculating Previous Version of File
            for ele in initial:
                if ele not in current:
                    for item in ele:
                        previtem.append(item)
            # Calculating New Version of File
            for ele in current:
                if ele not in initial:
                    changeditem.append(ele)
            # calculating changed file's name
            filename = onlyfiles[current.index(changeditem[0])]
            print(changeditem[0], filename)
            # Calculating Diff for previous and changed version of file
            diff = calcDiff(previtem, changeditem[0])
            writedata(path=filename, diff=diff)

            initial = current
