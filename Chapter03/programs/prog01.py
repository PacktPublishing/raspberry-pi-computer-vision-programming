class Person:

    def __init__(self, name='', age=0):
        self.name = name
        self.age = age

    def show(self):
        print(self.name)
        print(self.age)

p1 = Person('Ashwin', 25)
p1.show()

p2 = Person()
p2.name = 'Jane'
p2.age = 20
print(p2.name)
print(p2.age)
