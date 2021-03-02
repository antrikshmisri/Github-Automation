import os
from .gitcommands import git_commands
from .diffcalc import *
from .ignore import getIgnoreFiles
from .logger import *
from .utils import getNestedFiles,read_file,commitAndUpdate
from .colors import logcolors
mypath = os.getcwd()

git = git_commands(mypath)

ignoredirs = getIgnoreFiles()
# gets the list of all nested files
onlyfiles = getNestedFiles(mypath,ignoredirs)



def ischanged(url, branch,*args,**kwargs):
    changedfile = []
    diffarr = []
    # if uncommited data found perform git commands on them
    initbuffer = kwargs.get('initbuffer' , -1)
    if(initbuffer != -1):
        for obj in initbuffer:
            file = obj['path']
            diff = obj['changes']
            diffarr.append(diff)
            changedfile.append(file)

        # Performing Git Commands for changed files
        commitAndUpdate(changedfile,diffarr,url,branch)
    print('Listening for changes....')
    initial = list(read_file(onlyfiles))
    while True:
        current = list(read_file(onlyfiles))
        changeditem = []
        previtem = []
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
            for i in range(0, len(changeditem)):
                print('loop :-', i)
                changedfile.append(onlyfiles[current.index(changeditem[i])])
            print(f"Changed file is {logcolors.BOLD}{changedfile}{logcolors.ENDC}\n")

            # Calculating Diff for previous and changed version of file
            diff = calcDiff(previtem, changeditem[0])
            diffarr.append(diff)
            for file in changedfile:
                writedata(path=file, diff=diff)

            # Performing Git Commands for changed files
            commitAndUpdate(changedfile,diffarr,url,branch)

            initial = current
            # time.sleep(5)
