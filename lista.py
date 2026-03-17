lista_compras = []

frutas = ['maçã', 'banana', 'uva', 'pera']
numeros = [1,2,3,4] 

print(lista_compras)

item = input("Insira o item: ")
lista_compras.append (item)
print (lista_compras)

item2 = input("Insira o item: ")
lista_compras.append (item2)
print (lista_compras)

item3 = input("Insira o item: ")
lista_compras.append (item3)
print (lista_compras)

item4 = input("Insira o item: ")
lista_compras.append (item4)
print (lista_compras)

item5 = input("Insira o item: ")
lista_compras.append (item5)

print ("Sua lista de compras: ", lista_compras)
exclui = input("Qual item deseja remover? ")

,if exclui in lista_compras:
    lista_compras.remove(exclui)
    print(f"{item} foi removido.")
else:
    print(f"Erro: {item} não encontrado na lista.")

print("Lista atualizada:", lista_compras)
