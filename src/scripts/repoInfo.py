import subprocess
import os
from .gitcommands import git_commands
def takeInfo(url , branch):
    print('No Existing repo info found\n')
    if(not (url and branch)):
        url = str(input('Enter the Github Repo URL: '))
        branch = str(input('Enter the branch: '))
    info = [url, branch]
    return info


def checkinfoInDir(path , *args , **kwargs):
    url = kwargs.get('url' , None)
    branch = kwargs.get('branch' , None)
    infofile = os.path.join(path , '.git/config')
    git = git_commands(path)
    if (os.path.exists(infofile)):
        url = git.getRemote()
        branch = git.getBranch()                          
        url, branch = url.split('\n')[0], branch.split('\n')[0].split('/')[2]
        info = [url, branch]
        return info
    else:
        return ['n']
