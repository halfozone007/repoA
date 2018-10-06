
# "self" is the reference to the object

class AnimalActions:
    def bark(self): return self._doaction('bark')
    def quack(self): return self._doaction('quack')
    def fur(self): return self._doaction('fur')
    def feathers(self): return self._doaction('feathers')
    strings =dict()
    def _doaction(self, action):
        if action in self.strings:
            return self.strings[action]
        else:
            return 'The {} has no {}'.format(self.animalName(), action)

    def animalName(self):
        return self.__class__.__name__.lower()
    

class Duck(AnimalActions):
    strings = dict(
        quack = "Quaackkkkk!",
        feathers = "Duck has gray and white feathers"
    )

class Person(AnimalActions):
    strings = dict(
        quack = "The person imitates a duck",
        bark = "The person says woof!",
        fur = "The person puts on a fur coat",
        feathers = "The person takes a feather from the ground and shows it."
    )

class Dog(AnimalActions):
    strings = dict(
        bark = "Arfff!",
        fur = "The dog has a white fur with black spots"
    )


def in_the_dog_house(dog):
    print(dog.bark())
    print(dog.fur())

def in_the_forest(duck):
    print(duck.quack())
    print(duck.feathers())
    

def  main():
    Donald = Duck()
    Gaurav = Person()
    Snow = Dog()

    print("IN the Dog house ::")
    for o in (Donald, Gaurav, Snow):
        in_the_dog_house(o)

    print("IN the Forest ::")
    for o in (Donald, Gaurav, Snow):
        in_the_forest(o)
    

if __name__ == '__main__':main()
