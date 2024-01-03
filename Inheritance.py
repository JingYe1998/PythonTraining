class Mammal:
    def walk(self):
        print('walk')


class Dog(Mammal):
    def bark(self):
        print('bark')


class Cat(Mammal):
    pass  # pass代表繼承的class是empty，沒有寫其他method


dog = Dog()
dog.bark()
dog.walk()

cat = Cat()
cat.walk()
