import eel
import sys

@eel.expose
def getpara(arg):
    return f"You passed {arg}"


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