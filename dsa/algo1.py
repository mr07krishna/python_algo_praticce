class Person:
    name = "Hello "

    # def ChangeName(self, name):
    #     self.__class__.name = name
    #     #self.name= name

    @classmethod
    def ChangeName(cls, name):
        cls.name = name


p1 = Person()
p1.ChangeName("Rahul Kumar")
print(p1.name)
print(Person.name)
