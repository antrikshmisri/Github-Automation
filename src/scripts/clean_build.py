import os
from shutil import rmtree

if __name__ == "__main__":
    cwd = os.getcwd()
    build_path = os.path.join(cwd, "build")
    dist_path = os.path.join(cwd, "dist")

    if os.path.isdir(build_path):
        print('Removing build directory')
        rmtree(build_path)
    
    if os.path.isdir(dist_path):
        print('Removing dist directory')
        rmtree(dist_path)
else:
    raise ImportError("clean_build.py is not intended to be imported")