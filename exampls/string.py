country = 'Colombia'
country[1] #o 
country[-1] #a
country[-2] #i
len(country) # 8

second_letter = country[1]
print(second_letter)
id(second_letter) # Donde esta en nuestra memoria   4461106712
other_var = '0'
id(other_var) # Su espacio es en 4461106712
id('i') # 4461106714


country = 'Mexico' #4461106777
country += 's'
id(country) # 4461106788

# Operations with string  in python 

platzi = 'platzi'
platzi.upper() # PLATZI
platzi.startswith('p') #true
platzi.startswith('l') # false
dir(platzi)


