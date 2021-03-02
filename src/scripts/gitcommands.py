from subprocess import call, Popen, PIPE
from sys import platform as _platform
from .colors import logcolors
from os.path import join


class git_commands:
    def __init__(self, path):
        self.path = path
        self.git_path = join(self.path, '.git')
        self.git_command = f'git --git-dir={self.git_path} --work-tree={self.path}'

    def init(self):
        call(f'{self.git_command} init')

    def createReadme(self):
        if _platform == "linux" or _platform == "linux2":
            call('touch README.md')
        elif _platform == "darwin":
            call('touch README.md')
        elif _platform == "win32":
            call('type nul>README.md')

    def add(self, filelist):
        for file in filelist:
            # perform git add on file
            print(f"{logcolors.SUCCESS}Adding{logcolors.ENDC}",
                  file.split('\\')[-1])
            call(f'{self.git_command} add {file}')

    # git commit -m "passed message"

    def commit(self, msglist:list, filelist:list, *args, **kwargs):
        diffarr = kwargs.get('diffarr', -1)
        for file in filelist:
            # ask user for commit message

            # msg = str(input(f'{logcolors.BOLD}Enter the commit message for{logcolors.ENDC} ' +
            #                 file.split('\\')[-1] + f' {logcolors.BOLD}or enter {logcolors.ERROR}-r{logcolors.ENDC} to reject commit{logcolors.ENDC}'))
            msg = msglist[filelist.index(file)]
            # if msg == -r reject commit
            if(msg == '-r'):
                print(f'{logcolors.ERROR}commit rejected{logcolors.ENDC}')
                if(diffarr != -1):
                    diffarr.remove(diffarr[filelist.index(file)])
                filelist.remove(file)
                msglist.remove(msg)
                call('cls', shell=True)
                return False
            # else execute git commit for the file
            # added a comment
            else:
                call(f'{self.git_command} commit -m "{msg}"')
                msglist.remove(msg)
                call('cls', shell=True)
                print(
                    f'Commited {logcolors.CYAN}{file}{logcolors.ENDC} with msg: {logcolors.BOLD}{msg}{logcolors.ENDC}')

    def setremote(self, url):
        call(f'{self.git_command} remote add origin {url}')

    def setBranch(self, branch):
        call(f'{self.git_command} git branch -M {branch}')

    # git push

    def push(self, url, branch):
        call(f'{self.git_command} push -u {url} {branch}')
        call('cls', shell=True)
        print(f'{logcolors.SUCCESS}Successfully Pushed Changes{logcolors.ENDC}')

    def getremote(self):
        remote = Popen(f'{self.git_command} config --get remote.origin.url',
                       stdout=PIPE).stdout.read().decode('utf-8')
        return remote

    def getbranch(self):
        branch = Popen(f'{self.git_command} rev-parse --symbolic-full-name HEAD',
                       stdout=PIPE).stdout.read().decode('utf-8')
        return branch
