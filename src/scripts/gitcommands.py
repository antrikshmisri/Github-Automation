import os
from subprocess import call, Popen, PIPE
from .colors import logcolors
from os.path import join


class git_commands:
    """Class that provides various git operations as functions.
    
    Attributes
    ----------
    current_directory: str
        Current working directory
    path: str
        Path of the git repository
    git_path: str
        Path of the .git repository
    git_command: str
        Base git command which is used in all git operations.
    """

    def __init__(self, path):
        self.current_directory = os.getcwd()
        self.path = path
        self.git_path = join(self.path, '.git')
        self.git_command = f'git --git-dir={self.git_path} --work-tree={self.path}'

    def init(self):
        """Initializes git repository by calling git init"""
        os.chdir(self.path)
        call(f'git init')
        os.chdir(self.current_directory)

    def createReadme(self):
        """Creates README.md if during the git repository initialization"""
        readme_path = os.path.join(self.path, 'README.md')
        dir = self.path.split('\\')[-1]
        with open(readme_path, 'w') as readme:
            readme.write(f'# {dir}')
            readme.close()

    def add(self, file):
        """
        Stages a changed file by calling git add <filename>

        Parameters
        ----------
        file: str
            filename that needs to be staged
        """
        # perform git add on file
        call(f'{self.git_command} add {file}')

    # git commit -m "passed message"

    def commit(self, msg):
        """
        Commits the changed file with a message by calling git commit -m <message>

        Parameters
        ----------
        msg: str
            commit the changed file with the specified message
        """
        # if msg == -r reject commit
        if(msg == '-r'):
            return False
        # else execute git commit for the file
        else:
            try:
                call(f'{self.git_command} commit -m "{msg}" {self.path}')
                return True
            except Exception as e:
                print(f"{logcolors.ERROR} {e} {logcolors.ENDC}")
                return False

    def setRemote(self, url):
        """
        Set the remote repository to the specified URL

        Parameters
        ----------
        url: str
            URL of the remote repository
        """
        call(f'{self.git_command} remote add origin {url}')

    def setBranch(self, branch):
        """
        Set the working branch to the specified branch

        Parameters
        ----------
        branch: str
            Working branch 
        """
        call(f'{self.git_command} branch -M {branch}')

    def push(self, url, branch):
        """
        Push the staged and commited changes to the remote URL/branch

        Parameters
        ----------
        url: str
            URL of the remote repository
        branch: str
            Working branch
        """
        call(f'{self.git_command} push -u {url} {branch}')

    def getRemote(self):
        """Get the remote URL from the local directory"""
        remote = Popen(f'{self.git_command} config --get remote.origin.url',
                       stdout=PIPE).stdout.read().decode('utf-8')
        return remote

    def getBranch(self):
        """Get the working branch from the local directory"""
        branch = Popen(f'{self.git_command} rev-parse --symbolic-full-name HEAD',
                       stdout=PIPE).stdout.read().decode('utf-8')
        return branch

    def pull(self, url, branch):
        """
        Pull the changes from the remote URL/branch

        Parameters
        ----------
        url: str
            URL of the remote repository
        branch: str
            Working branch
        """
        call(f'{self.git_command} pull {url} {branch}')

    def diff(self, file):
        """
        Get the diff of the file
        
        Parameters
        ----------
        file: str
            Name of the file whose diff is to be fetched
        """
        diff = Popen(f'{self.git_command} diff {file}',
                     stdout=PIPE).stdout.read().decode('utf-8')
        return diff

    def initRepository(self, info):
        """
        If directory is git initialized, perform starting git commands

        Parameters
        ----------
        info: list
            Contains URL at 0th, branch at 1st index
        """
        url, branch = info
        self.init()
        self.createReadme()
        self.add('.')
        self.commit('initial commit')
        self.setBranch(branch)
        self.setRemote(url)
        self.push(url, branch)
