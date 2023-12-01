from collections import defaultdict
from pprint import pprint
import re

with open("input.txt") as f:
    content = f.readlines()
    #content = [int(x) for x in f.readlines()]

words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
valid = {"one": 1,
         "two": 2,
         "three": 3,
         "four": 4,
         "five": 5,
         "six": 6,
         "seven": 7,
         "eight": 8,
         "nine": 9
         }


def find_first(wordList, bigString, startIndex=0):
    return re.search('|'.join(wordList), bigString[startIndex:])


sum = 0
working = []
for l in content:
    print(l, end="")
    while True:
        result = find_first(words, l)
        if result:
            index = l.index(result[0])
            l = l[:index+1] + str(valid[result[0]]) + l[index+2:]
            #l = l.replace(result[0], str(valid[result[0]]))

        else:
            print(l, end="")
            work = []
            for char in l:
                if char.isnumeric():
                    work.append(char)
            print(work[0], work[-1])
            print()
            sum += int(str(work[0]) + str(work[-1]))
            break

print(sum)
