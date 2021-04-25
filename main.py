import eel
import sys
import threading


@eel.expose
def getInfo(path):
    from src.scripts import repoInfo
    info = repoInfo.checkinfoInDir(path)
    return info


@eel.expose
def checkPath(path):
    from src.scripts import  utils
    return utils.checkPath(path)


@eel.expose
def init(url, branch, path):
    from src.scripts import main
    t1 = threading.Thread(target=main.init , args=(url, branch, path)) 
    t1.start()


@eel.expose
def commitAndUpdate(path , file , diff , msg , url , branch):
    from src.scripts.utils import commitAndUpdate
    commitAndUpdate(path , file , diff , msg , url , branch)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == '--develop':
            eel.init('src')
            eel.start({
                'port': 3000,
            }, options={
                'port': 8888,
                'host': 'localhost',
            }, suppress_error=True, size=(1000, 600))
    else:
        eel.init('build')
        eel.start('', 
            options={
                'port': 8888,
                'host': 'localhost',
            }, suppress_error=True, size=(1000, 600))
