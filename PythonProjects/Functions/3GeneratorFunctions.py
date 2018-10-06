
def main():
    for x in inclusiveRange(1, 10 ):
        print (x, end = " ")
    print()

    for x in inclusiveRange(10):
        print(x, end = " ")
    print()
    
    for x in inclusiveRange(1, 10, 1):
        print(x, end = " ")
    print()

def inclusiveRange(*args):
    numArgs = len(args)
    if numArgs < 1: raise TypeError("Expects at least one argument")
    elif numArgs == 1:
        stop = args[0]
        start = 1
        step = 1
    elif numArgs == 2:
        (start, stop) = args
        step = 1
    elif numArgs == 3:
        (start, stop, step) = args
    else: raise TypeError("Expects at most three argumes, got {}", format(numArgs) )

    i = start
    while i <= stop:
       yield i 
       i += step 





if __name__ == '__main__':
    main()
    