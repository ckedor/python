num = [1,3,4,5]

squares = []
for n in num:
    squares.append(n**2)

print(squares)

#########################
## list comprehension

squares_with_list_comprehension = [n**2 for n in num]
print(squares_with_list_comprehension) 

#########################
## Achar a interseção entre duas listas
## Achar elementos não comuns entre duas listas

list = [1, 2, 3, 4, 5]
list1 = [2, 3, 4, 5, 6]

intersection = [x for x in list for y in list1 if x==y]
non_common_elements_pairs = [(x, y) for x in list for y in list1 if x!=y]
print("\nIntersection:", intersection)
print("\nNon Common elements:", non_common_elements_pairs)

#########################
## Aplicar uma função em cada elemento de uma lista

list = ["Hello World", "Whats Up?"]
list2 = [str.lower() for str in list]
print("\nsmall cases lists: ", list2)

#########################
## Lista de listas

list = [1,2,3,4,5]
x = [[a**2, a**3] for a in list]
print("\nlist of list:", x)

#########################
## parsing a file with list compreehension

file = open(".\\python\\test_file.txt", "r")
output = [i for i in file if "list" in i]
print("file output", output)

#########################
## acessing function using list compreehension

def x(a):
    return a*2

print("usando função pra criar lista:", [x(a) for a in range(10)])


