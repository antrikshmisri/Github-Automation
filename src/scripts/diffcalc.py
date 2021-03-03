from difflib import ndiff




def calcDiff(firstFile, secondFile):
    # calculate raw diff
    diff = ndiff(firstFile, secondFile)
    # calculate unique lines in secondfile
    deltainit = ''.join(x[2:] for x in diff if x.startswith('+ '))
    return deltainit
