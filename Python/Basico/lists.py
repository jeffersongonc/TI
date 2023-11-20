#Tipos de dados
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#Multiplus tipos de dados
list1 = ["abc", 34, True, 40, "male"]
print(list1)

#tamanho
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist)
print(thislist[1])
print('Ultimo:', thislist[-1])
print('Penultimo:', thislist[-2])
print('Range de 2 ao 4:', thislist[2:5])
print('Range até o 4:', thislist[:4])