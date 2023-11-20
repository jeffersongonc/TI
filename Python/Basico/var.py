"""
Melhor declarar as funções globais fora das funções. Evite usar o global
Use o global para levar dados da função, mas o melhor é levar através do return 
Sempre que declarar como global fora das funções
"""
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)
  return x

x = myfunc()

print("Python is " + x)