#!/usr/bin/env python

import linecache
import random
import os

os.chdir(os.path.expanduser('~/randomtarot'))

i = random.randint(1,78)


thecard = linecache.getline('cardnames.txt', int(i))
print('... random tarot card ...\n' + str(thecard))

thefile = str(linecache.getline('cardfiles.txt', int(i)))

os.system('display '+thefile)

