import eel
import sys
from src.scripts import repoInfo,utils


@eel.expose
def getpara(arg):
    return f"You passed {arg}"

@eel.expose
def getInfo(path):
    info = repoInfo.checkinfoInDir(path)
    return info

    
@eel.expose
def checkPath(path):
    return utils.checkPath(path)

@eel.expose
def init(url , branch):
    from src.scripts import main
    return main.init(url , branch)

if __name__ == '__main__':
    if sys.argv[1] == '--develop':
        eel.init('client')
        eel.start({
            'port': 3000,
        }, options={
            'port': 8888,
            'host': 'localhost',
        } , suppress_error = True , size=(1000,600))
    else:
        eel.init('build')
        eel.start('index.html')