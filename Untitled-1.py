fruit =['apple','banana','cherry']

fruit.append('orange')
print(fruit)

# itr = iter(fruit)
# print(next(itr))
# print(next(itr))
# print(next(itr))

def generator():
    yield 'apple'
    yield 'banana' 
    yield 'cherry'

g = generator()

next(g)
next(g)
next(g)

