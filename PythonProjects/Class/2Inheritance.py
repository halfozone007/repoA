

#Use super() to access parent class methods in base class


class Animal:
    def talk(self): print("I have something to say")
    def walk(self): print("Hey! I'm walkin'' here")
    def clothes(self):print("I have some really nice clothes")
    
class Duck(Animal):
    def quack(self): print("Quaccckkkk! Quaccckkk!")
    def walk(self):
        super().walk() 
        print("Walk like a duck")


def main():
    donald = Duck()
    donald.quack()
    donald.talk()
    donald.clothes()
    donald.walk()


if __name__ == '__main__':
    main()
    