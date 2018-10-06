

#Search&replace is done using re.sub

import re


def main():
    fh = open('raven.txt')

    #search and replace in one step
   # for line in fh.readlines():
   #     print(re.sub('(Neverm|Len)ore', '###', line), end = '')

    #search and replace in two steps
    for line in fh:
        match = re.search('(Neverm|Len)ore',line)
        if match:
            print(line.replace(match.group(), '###'), end = '')

if __name__ == '__main__':
    main()
    