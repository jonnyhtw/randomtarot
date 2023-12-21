#!/usr/bin/env python

import linecache
import random
import platform
import os

os.chdir(os.path.expanduser('~/randomtarot'))

i = random.randint(1,78*2)


thecard = linecache.getline('cardnames.txt', int(i))
print('... random tarot card ...\n' + str(thecard))

thefile = str(linecache.getline('cardfiles.txt', int(i)))

if platform.system() == 'Darwin':
    os.system('open '+thefile)
elif platform.system() == 'Linux':
    os.system('display '+thefile)

