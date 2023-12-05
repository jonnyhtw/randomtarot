import linecache
import random
import os

os.chdir(os.path.expanduser('~/randomtarot'))

#print(os.getcwd())

i = random.randint(1,78)

print('your random tarot card is...\n')

linenumber = linecache.getline('cardnames.txt', int(i))
print(str(linenumber))

thecard = str(linecache.getline('cardfiles.txt', int(i)))
#print(thecard)


os.system('display '+thecard)

