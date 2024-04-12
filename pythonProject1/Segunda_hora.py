import time

#while loop

#while 1 ==1:
#    print("socoorrrooo")

#nome = ""
#while len(nome) ==0:
#    nome = input("escreva seu nome :")
#print("ola " + nome)

#for loop

#for i in range(10):
#    print(i+1)

#for i in range(50,100+1,2):
#    print(i)

#for i in "caio":
#    print(i)
#aaaaaa
#for i in range(10,0,-1):
#    print(i)
#    time.sleep(1)
#print("feliz ano novo")

#vários loops

#linhas = int(input("quantas linhas você quer:? "))
#coluna = int(input("quantas colunas você quer:? "))
#simbolo = input("qual o simbolo você quer usar:? ")

#for i in range(linhas):
#    for j in range(coluna):
#        print(simbolo, end="")
#    print()

#controle de loop

#while True:
#    nome = input("digite o seu nome: ")
#    if nome != "":
#        break

#numero = "1213-123123"
#for i in numero:
#    if i == "-":
#        continue
#    print(i)

#Lista

#food = ["pizza","sushi","tomate","ovo","carne"]
#food.append("sorvete")
#food[0] = "pepino"
#food.remove("tomate")
#food.pop()
#food.insert(0,"bolo")
#food.sort()
#food.clear()
#print(food[0])
#for i in food:
#    print(i)

#2D Lists

#bebida = ["agua","suco","coca"]
#jantar = ["macarrão","arroz","vitamina"]
#sobremesa = ["sorvete","bolo"]

#comida = [bebida,jantar,sobremesa]
#print(comida[0][1])

#tupla

#student = ("caio",21,"gender")
#print(student.count("caio"))
#print(student.index("gender"))

#set

#utensils = {"colher","garfo","faca","faca","faca"}
#utensils.add("tampa")
#utensils.remove("tampa")

#pratos = {"prato","copo",'bowl',"colher"}
#utensils.update(pratos)
#dinner_table = utensils.union(pratos)
#for i in utensils:
#    print(i)
#print(utensils.difference(pratos))
#print(utensils.intersection(pratos))

#dicionário

#capitais = {'USA':'Washington',
 #           'India':'New dehli',
 #           'China':'Beijing',
 #            'Russia': 'Moscow'}

#capitais.update({'Alemanha':'Berlin'})
#capitais.update({'USA':'Las vegas'})
#print(capitais['Brasil'])
#print(capitais.get('UBR'))
#capitais.pop('Russia')
#print(capitais.keys())
#print(capitais.values())
#print(capitais.items())
#for key,value in capitais.items():
#    print(key,value)

#Operador index

#name = "caio Fontes!"
#if(name[0].islower()):
#    name = name.capitalize()
#primeiro_nome = name[:4].upper()
#ultimo_nome = name[5:].lower()
#ultimo_caractere = name[-1]
#print(primeiro_nome)
#print(ultimo_nome)
#print(ultimo_caractere)
#print(name)

#função

#def hello(primeiro_nome,ultimo_nome,idade):
#    print("ola " + primeiro_nome + " " + ultimo_nome + " a sua idade é " + str(idade))
#    print("opa")
#hello("Caio","Fontes", 21)

