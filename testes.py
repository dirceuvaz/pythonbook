#CRUD EM LISTA

#Declacorando
lista_nomes = ["Dirceu", "Apolo"]

#printando normal (SELECT)
print(lista_nomes)

#Inserindo mais valores em uma lista
lista_nomes.insert(2,"Rogeria") # 2 = indice da lista, "valor"
#printando normal
print(lista_nomes)

#Update na lista
lista_nomes[2] = "Rogeria Lara"
#printando normal
print(lista_nomes)

#Removendo valor da lista
lista_nomes.remove("Rogeria Lara")
print(lista_nomes)

#Pecorrer uma lista e imprimir, no caso.
for x in lista_nomes:
    print(x)

# if e ifelse
a = "2"
b = "1"
if a > b:
    print(f"O valor de a é maior {a}") #concatenando
    print("Valor de a é = " + a)
else:
    print(f"O valor de a é menor: {a}")

str1 = "Ola"
str2 = "Mundo"
print(str1 + " " + str2)  # Saída: Olá Mundo


xx = 1
while xx < 10:
    xx+=1
    print(f"Valor de x {xx}")
    
i = 10
for i in range (1,10):
    print(i)