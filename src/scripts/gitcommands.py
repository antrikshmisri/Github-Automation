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

    def add(self, file):
        # perform git add on file
        call(f'{self.git_command} add {file}')

    # git commit -m "passed message"

    def commit(self, msg , *args, **kwargs):
        diffarr = kwargs.get('diffarr', -1)
            # if msg == -r reject commit
        if(msg == '-r'):
            return False
        # else execute git commit for the file
        # added a comment
        else:
            try:
                call(f'{self.git_command} commit -m "{msg}" {self.path}')
                return True
            except Exception as e:
                print(f"{logcolors.ERROR} {e} {logcolors.ENDC}")
                return False
            

    def setremote(self, url):
        call(f'{self.git_command} remote add origin {url}')

    def setBranch(self, branch):
        call(f'{self.git_command} git branch -M {branch}')

    # git push

    def push(self, url, branch):
        call(f'{self.git_command} push -u {url} {branch}')
        

    def getremote(self):
        remote = Popen(f'{self.git_command} config --get remote.origin.url',
                       stdout=PIPE).stdout.read().decode('utf-8')
        return remote

    def getbranch(self):
        branch = Popen(f'{self.git_command} rev-parse --symbolic-full-name HEAD',
                       stdout=PIPE).stdout.read().decode('utf-8')
        return branch
