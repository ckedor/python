dictionary = {'a':1, 'b':2, 'c':3, 'd':4}

new_dict_values = {k:v*2 for (k, v) in dictionary.items()}
print(new_dict_values)

new_dict_keys = {k*2:v for (k, v) in dictionary.items()}
print(new_dict_keys)

############################
## achar os quadrados dos números pares 

dictionary = {i:i**2 for i in range(10) if i%2==0}
print(dictionary)

############################
## Dictonary comprehension as lambda function (converter fahrenheit temperaturas)
## Same example without lambda

feh = {'temp1':10, 'temp2':20, 'temp3':30, 'temp4':40}
cel = list(map(lambda x: (float(5)/9)*(x-32), feh.values()))
cel_dict = dict(zip(feh.keys(), cel))
print(cel_dict)

cel_dict = {k:(float(5)/9)*(v-32) for (k, v) in feh.items() }
print(cel_dict)

############################
## 
##
dictionary = {'a':1, 'b':2, 'c':3, 'd':5, 'e':5, 'f':6}
new_dict = {k:('even N' if v%2==0 else 'Odd N') for (k,v) in dictionary.items()}
print(new_dict)