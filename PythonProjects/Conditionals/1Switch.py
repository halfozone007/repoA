
#There is no switch conditional in Python
#We can use dict as a hack to implement swithc



def main():
    choices = dict(
        one  = 'hello',
        two = 'three'
    )

    v = 'one'
    print(choices.get(v,'other' ))
    w = 'three'
    print(choices.get(w,"other" ))







if __name__ == '__main__':
    main()
    