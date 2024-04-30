class Animal(object):

    def speak(self):
        print('动物的叫声')
        pass

class Cat(Animal):

    def speak(self):
        print('喵喵')

class Dog(Animal):

    def speak(self):
        print('汪汪')

class Test(object):
    def speak(self):
        print('test')

def speak(object):  # animal
    object.speak()

animal = Animal()
kitty = Cat()
puppy = Dog()
t = Test()
speak(animal)
speak(kitty)
speak(puppy)
speak(t)