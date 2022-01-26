class PartyAnimal:
    x = 0

    def __init__(self) :
        print('I am constructed')

    def party(self) :
        self.x = self.x + 1
        print("So far", self.x)

    def __del__(self) :
        print('I am destructed', self.x)

an = PartyAnimal()

an.party()
an.party()
an.party()
an = 42
print( 'an contains', an)

x = list()
print(x)
print('TYPE', type(x))
print('DIR', dir(x))
x.append('x0')
print('x', x)
y = x.copy()
print('y', y)
print('x.count(y[0])', x.count(y[0]))
x.clear()
print('x, y', x, y)
x = y.copy()
y.extend(y)
print(y)
print(y.index(x[0]))
y.insert(1, 'o')
print(y)
z = y.pop(1)
print(z)
y.insert(1, 'e')
y.insert(2, 'g')
print(y)
y.reverse()
print(y)
y.sort()
print(y)
y.remove('g')
print(y)
print(type(an))
print(dir(an))

