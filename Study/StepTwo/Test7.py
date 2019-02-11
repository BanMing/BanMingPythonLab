class Person:
    name = 'aaaa'

p1 = Person()
p2 = Person()
p1.name='bbbb'
print(p1.name)
print(p2.name)
print(Person.name)


class PersonM:
    name=[]
p1=PersonM()
p2=PersonM()
p1.name.append(1)
print(p1.name)
print(p2.name)
print(PersonM.name)