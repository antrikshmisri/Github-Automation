from os.path import join, isfile, isdir

def makeIgnore(path):
    f = open(join(path , '.gitignore') , "x")
    f.write('.git\n.idea\nnode_modules\n__pycache__\n')
    f.close()

def getIgnoreFiles(path):

    if not(isfile(join(path, '.gitignore'))):
        makeIgnore(path)

    ignorepath = join(path, '.gitignore')
    ignorefiles = []
    with open(ignorepath) as ignore:
        files = ignore.readlines()
        for file in files:
            file = ''.join(file.splitlines())
            if(file != ''):
                filepath = join(path , file)
                if(isfile(filepath) or isdir(filepath)):
                    ignorefiles.append(file)
    return ignorefiles
