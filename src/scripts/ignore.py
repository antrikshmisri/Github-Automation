import os


def getIgnoreFiles(path):
    ignorepath = os.path.join(path, '.gitignore')
    ignorefiles = []
    with open(ignorepath) as ignore:
        files = ignore.readlines()
        for file in files:
            file = ''.join(file.splitlines())
            if(file != ''):
                filepath = os.path.join(path , file)
                if(os.path.isfile(filepath) or os.path.isdir(filepath)):
                    ignorefiles.append(file)
    return ignorefiles
