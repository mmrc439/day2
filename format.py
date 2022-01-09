name=input('enter your name : ')
city=input('enter your city : ')
age=int(input('enter your age : '))

print('I am '+name+ ', live in '+city+ ' I am '+str(age)+' years old')
print('I am %s, live in %s I am %s years old'%(name,city,age))
print('I am {0}, live in {1} I am {2} years old'.format(name,city,age))
print(f'I am {name}, live in {city} I am {age} years old')