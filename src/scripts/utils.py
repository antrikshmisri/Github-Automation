from os.path import isdir


def getMaxSpaces(file):
    max = float('-inf')
    for ele in file:
        ele = ele.strip()
        if(len(ele) > max):
            max = len(ele)
    return max

def getNestedFiles(rootDir,ignoredirs):
    from os import walk
    from os.path import join
    nestfiles = []
    for path, subdirs, files in walk(rootDir):
        if(all(ele not in path for ele in ignoredirs)):
            for name in files:
                nestfiles.append(join(path, name))
    return nestfiles


def read_file(onlyfiles):
    filecontent = []
    for file in onlyfiles:
        with open(onlyfiles[onlyfiles.index(file)], "r") as f:
            try:
                filecontent.append(f.readlines())
            except UnicodeDecodeError:
                continue
    return filecontent

def initCommands(info, path):
    from .gitcommands import git_commands
    from . import filechange
    git = git_commands(path)
    git.initRepository(info)
    filechange.ischanged(path)

def commitAndUpdate(path,file,idx,msg,url,branch):
    from .gitcommands import git_commands
    from .logger import updatedata
    from .colors import logcolors
    # from .filechange import changedfile,diffarr
    # print(changedfile , diffarr)
    git = git_commands(path)
    git.add(file)
    commit_response = git.commit(msg)
    if(not commit_response):
        print(f'{logcolors.ERROR}Reverting Push{logcolors.ENDC}')
        updatedata(idx)
    else:
        print(f'{logcolors.SUCCESS}Updating Logs{logcolors.ENDC}')
        updatedata(idx)
        git.push(url, branch)
    return commit_response


def checkPath(path):
    return isdir(path)
