#Regular Expressions are a very powerful method of matching patterns in a text
import re


def main():
    fh = open('raven.txt')

    for line in fh.readlines():
       if re.search('(Neverm|Len)ore', line):
           print(line, end = '')

    for line in fh.readlines():
        match = re.search('(Neverm|Len)ore', line)
        if match:
            print(match.group())

if __name__ == '__main__':
    main()
    