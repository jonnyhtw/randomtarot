import linecache
import random

i = random.randint(1,78)
print(i)

print('your random tarot card is...\n')

print(linecache.getline('cards.txt', int(i)))

