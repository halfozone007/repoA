


class Egg:
    def __init__(self, kind='fried'):
        self.kind = kind
    

    def whatKind(self):
        return self.kind


def main():
   
    fried = Egg()
    scrambled = Egg('scrambled')

    for o in (fried, scrambled):
        print(o.whatKind())
    
if __name__ == '__main__':
    main()