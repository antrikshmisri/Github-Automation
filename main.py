import os
import sys
import threading
from subprocess import Popen, PIPE
import eel
import eel.browsers

from src.scripts import repoInfo, main, gitcommands, utils
from src.scripts.utils import initCommands
from src.scripts.gitcommands import git_commands


# Bind the docstring of original function to the exposed function.
DOCSTRING_DICT = {}
DOCSTRING_DICT['getInfo'] = repoInfo.checkinfoInDir.__doc__
DOCSTRING_DICT['checkPath'] = utils.checkPath.__doc__
DOCSTRING_DICT['init'] = gitcommands.git_commands.pull.__doc__
DOCSTRING_DICT['commitAndUpdate'] = utils.commitAndUpdate.__doc__
DOCSTRING_DICT['initRepository'] = initCommands.__doc__
DOCSTRING_DICT['getDiff'] = gitcommands.git_commands.diff.__doc__


def fetch_npm_package(package_name):
    """Fetch a package using node package manager.
    
    Parameters
    ----------
    package_name: str
        Name of the package.
    """
    npm_out = Popen(f'npm install --global {package_name}',
                    stdout=PIPE, shell=True).stdout.read().decode('utf-8')

    if 'npm ERR!' in npm_out:
        print(f'Error installing {package_name}')
        return ""

    return npm_out


def get_electron_bin():
    """Get the binaries for electron using npm.
    
    Returns
    -------
    path
        The path to the electron binaries.
    """
    os_name = os.name
    if os_name == 'nt':
        user_path = os.path.expanduser('~')
        node_modules_path = os.path.join(
            user_path, 'AppData', 'Roaming', 'npm', 'node_modules')
        electron_path = os.path.join(
            node_modules_path, 'electron', 'dist', 'electron.exe')
        return electron_path
    elif os_name == 'posix':
        user_path = 'root'
        node_modules_path = os.path.join(
            user_path, 'local', 'lib', 'node_modules')
        electron_path = os.path.join(
            node_modules_path, 'electron', 'dist', 'electron')
        return electron_path
    else:
        raise ValueError(f'{os_name} currently not supported.')


@eel.expose
def getInfo(path):
    info = repoInfo.checkinfoInDir(path)
    return info


@eel.expose
def checkPath(path):
    return utils.checkPath(path)


@eel.expose
def init(path):
    url, branch = getInfo(path)
    git = gitcommands.git_commands(path)
    git.pull(url, branch)
    t1 = threading.Thread(target=main.init, args=(path,))
    t1.start()


@eel.expose
def commitAndUpdate(path, file, diff, msg, url, branch):
    utils.commitAndUpdate(path, file, diff, msg, url, branch)


@eel.expose
def initRepository(info, path):
    initCommands(info, path)


@eel.expose
def getDiff(path, file):
    git = git_commands(path)
    return git.diff(file)


def bind_function_docstrings():
    """Bind the docstring of original function to the exposed function."""
    all_exposed_functions = list(eel._exposed_functions.values())
    for function in all_exposed_functions:
        function_name = function.__name__
        function.__doc__ = DOCSTRING_DICT[function_name] or ""


if __name__ == '__main__':
    bind_function_docstrings()

    if len(sys.argv) > 1:
        if sys.argv[1] == '--develop':
            _electron_path = os.path.join(
                os.getcwd(), "node_modules/electron/dist/electron.exe")
            if not os.path.isfile(_electron_path):
                raise Exception(
                    f'Electron not found in path {_electron_path}.\nPlease install using npm i electron')

            eel.init('src')
            eel.browsers.set_path('electron', _electron_path)
            eel.start({
                'port': 3000,
            }, options={
                'port': 8888,
                'host': 'localhost',
                'args': [_electron_path, '.'],
            }, suppress_error=True, size=(1000, 600), mode="electron")
    else:
        _electron_path = get_electron_bin()

        if not os.path.isfile(_electron_path):
            print('Warning: Electron not found in global packages\n'
                  'Trying to install through npm....')

            npm_out = fetch_npm_package('electron')
            if not len(npm_out):
                raise Exception(
                    "Something went wrong, couldn't install electron.")
            else:
                print(npm_out[:100] + '...')

        print(_electron_path)
        eel.init('build')
        eel.browsers.set_path('electron', _electron_path)
        eel.start('',
                  options={
                      'port': 8888,
                      'host': 'localhost',
                      'args': [_electron_path, '.'],
                  }, suppress_error=True, size=(1000, 600), mode="electron")
