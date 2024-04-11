import math

#String

#primeiro_nome = "caio"
#last_name = "fontes"
#full_name = primeiro_nome+ " " +last_name
#print("ola " + full_name)

#Int

#idade = 21
#idade += 1
#print("sua idade é " + str(idade))
#print(type(idade))

#Float

#altura = 250.5
#print("sua altura é " + str(altura))
#print(type(altura))

#Boolean

#human = True
#print("você é humano ? " + str(human))
#print(type(human))

#Múltiplas atribuições

#nome,idade,bonito = "Caio",21,True
#print(nome)
#print(idade)
#print(bonito)

#karin = Caio = Joao = 30
#print(Caio)

#Métodos de strings

#nome = "caio"
#print(len(nome))
#print(nome.find("C"))
#print(nome.capitalize()) #deixa a primeira letra maiuscula
#print(nome.upper())
#print(nome.lower())
#print(nome.isdigit()) #retorna true se for digito
#print(nome.isalpha()) #True se so tiver letras alfabeticas
#print(nome.count("a"))
#print(nome.replace("o","a"))
#print(nome*5)

#Type casting

#x = 2
#y = 3.0
#z = "4"
#print(x)
#print(int(y))
#print(int(z) * 4)
#x = float(x)
#print(x)
#print("X tem o valor de : " + str(y))

#input usuário

#nome = input("qual o seu nome?")
#idade = int(input("qual a sua idade ?:"))
#altura = float(input("qual a sua altura:? "))
#idade += 1
#print(idade)
#print("olá " + nome)
#print("voce tem " + str(idade) + "anos" + ", alé. disso você tem : " +str(altura))

#matemática

#pi = 3.14
#pin = -3.14
#print(round(pi))
#print(math.ceil(pi))
#print(abs(pin)) #quanto falta pra chegar em 0
#print(pow(pi,2))
#print(math.sqrt(pi))
#x = 1
#y = 2
#z = 3
#print(max(x,y,z))
#print(max(x,y,z,pi))
#print(min(x,y,z,pi))

#cortando String

#nome = "Caio Fontes"
#primeiro_nome = nome[0:4]
#ultimo_nome = nome[5:11]
#nome_estranho = nome[0:11:2]
#nome_reverso = nome[::-1]

#print(primeiro_nome)
#print(ultimo_nome)
#print(nome_estranho)
#print(nome_reverso)

#website1 = "http://google.com"
#website2 = "http://wikipedia.com"
#slice = slice(7,-4)
#print(website1[slice])
#print(website1[7:13])
#print(website2[slice])

#if statement

#idade = int(input("qual a sua idade:? "))

#if idade == 100:
#    print("você tem " + str(idade) + " anos")
#elif idade >= 18 :
#    print("você é um adulto.")
#elif idade < 0:
#    print("você ainda não nasceu.")
#else:
#    print("você é menor de idade.")

#operadores lógicos(and,or,not)

#temp = int(input("Qual a temperatura:? "))

#if not(temp >= 0 and temp <=30):
#    print("a temperatura está ruim hoje")
#elif not(temp < 0 or temp > 30):
#    print("a temperatura está boa hoje")
#    print("vá para o lado de fora")

