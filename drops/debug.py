# coding=utf-8

import os 
from os import listdir, remove 
from os.path import isfile, join
import shutil

mypath = './'

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) if '.html' in f]
print onlyfiles

for x in onlyfiles:
    count = 0
    path = mypath + x
    temp = mypath + 'temp'
    try:
        with open(temp, 'w') as f_temp:
            with open(path, 'r') as f:
                for line in f.readlines():
                    if "dropsjs/" in line:
                        line = line.replace("dropsjs/", "drops/js/")
                        count += 1
                    if "static/drops/" in line:
                        line = line.replace("static/drops/", "drops/")
                        count += 1
                    f_temp.write(line)
                    
        print path + ': replaced ' + str(count) + ' times'
        os.remove(path)
        shutil.copy(temp, path)
        os.remove(temp)
    except:
        print error





