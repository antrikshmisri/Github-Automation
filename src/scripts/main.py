from .repoInfo import *
from .filechange import ischanged
from .colors import logcolors
import pyfiglet
from .logger import *
import sys
from .utils import initCommands

def init(url , branch , path):
    checkdata(url , branch,path)



if __name__ == '__main__':
    if sys.argv[1] == '--cli':
        f = pyfiglet.figlet_format('G - AUTO', font='5lineoblique')
        print(f"{logcolors.BOLD}{f}{logcolors.ENDC}")
        init()
