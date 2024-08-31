my_dict = {'Denis': 1975,'Andrey':1980}
print(my_dict)
print(my_dict.get('Denis'))
print(my_dict.get('Igor','Такого значения нет'))
my_dict.update({'Vera':1977,'Semen':1987})
print(my_dict)
a = my_dict. pop ('Denis')
print(a)
my_set = {'Moscow':1980,'SPB':1990}
print(my_set)
my_set.update({'Minsk':2000,'Saratov':1950})
print(my_set)
del my_set['Minsk']
print(my_set)

