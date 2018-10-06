



def main():
    testFun(1, 2, 3, 4, 5, 6, seven = 7, eight = 8, nine = 9)


def testFun(this, that, other, *args, **kwargs):
    print(this, that, other)
    for x in args:
        print(x, end = " " )
    print()
    for y in kwargs.values():
        print (y, end = " " )
    print()

if __name__ == '__main__':
    main()
    