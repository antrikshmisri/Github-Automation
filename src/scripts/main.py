from .repoInfo import *
from .colors import logcolors
import pyfiglet
from .logger import *
import sys


def init(path):
    checkdata(path)


if __name__ == '__main__':
    if sys.argv[1] == '--cli':
        f = pyfiglet.figlet_format('G - AUTO', font='5lineoblique')
        print(f"{logcolors.BOLD}{f}{logcolors.ENDC}")
        init()
