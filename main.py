import eel
import sys
from src.scripts import repoInfo, utils


@eel.expose
def getpara(arg):
    return f"You passed {arg}"


@eel.expose
def getInfo(path):
    info = repoInfo.checkinfoInDir(path)
    print(info)
    return info


@eel.expose
def checkPath(path):
    return utils.checkPath(path)


@eel.expose
def init(url, branch, path):
    from src.scripts import main
    main.init(url, branch, path)

@eel.expose
def commitAndUpdate(path , file , url , branch):
    from src.scripts.utils import commitAndUpdate
    commitAndUpdate(path , file , url , branch)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == '--develop':
            eel.init('client')
            eel.start({
                'port': 3000,
            }, options={
                'port': 8888,
                'host': 'localhost',
            }, suppress_error=True, size=(1000, 600))
    else:
        eel.init('build')
        eel.start('', options={
                'port': 8888,
                'host': 'localhost',
            }, suppress_error=True, size=(1000, 600))
