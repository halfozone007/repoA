
try:
    fh = open('xlines.txt')
    for lines in fh.readlines():
        print(lines)
except:
    print("something bad happened")

    