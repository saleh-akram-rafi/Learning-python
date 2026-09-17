#Concatinating string

my_str_1 = 'Hello'
my_str_2 = "World"

str_plus_str = my_str_1 + ' ' + my_str_2
print(str_plus_str) # Hello World

#Repeating String

sound = 'ha'
repeated_sound = sound * 3
print(repeated_sound) # hahaha


name = 'John Doe'
age = 26

# name_and_age = name + age
# print(name_and_age) # TypeError: can only concatenate str (not "int") to str
#}
name_and_age = name + ' '+str(age)
print(name_and_age) # John Doe26

