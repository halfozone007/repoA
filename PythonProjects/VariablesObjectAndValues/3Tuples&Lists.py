

# x : Tuple is an immutable object. Once I created it, I can't delete it.Append to it. Or In any way modify it
# y : List is an mutable object. You can modify it

def main():
    x = (1, 2, 3)
    y = [1, 2, 3]

    print(type(x), x)

    y.append(4)
    y.insert(0, 0)

    print(type(y), y)




if __name__ == '__main__':   main()
    