import random
import os
import shutil


#retorno

#def multiplica(x,y):
#    return x * y

#print(multiplica(10,5))

#keywwords argument

#def esse(primeiro,meio, ultimo):
#    print("hello"+ primeiro + meio + ultimo)

#esse(ultimo=" Melo",meio=" Fontes",primeiro=" Caio")

#nested function call

#print(round(abs(float(input("digite um numero:")))))

#Scope

#name = "Caio"
#def fale_nome():
#   name = "code"
#   print(name)
#fale_nome()
#print(name)

#*args

#def add (*args):
#    sum = 0
#    for i in args:
#        sum += i
#    return sum
#print(add(1,2,5,7))

#**kwargs

#def ola(**kwargs):
#    print()
#    print("ola", end = " ")
#    for key,values in kwargs.items():
#        print(values, end=" ")
#ola(first = "caio",meio = "fontes", esse = "de", final = "melo")

#Str.format

#animal = "vaca"
#item = "lua"
#print("a {} pulou a {} " .format(animal,item))
#text = "a {} pulou a {}"
#print(text.format(animal,item))

#nome = "caio"
#print("ola meu nome é {}" .format(nome))
#print("ola meu nome é {:10}" .format(nome))

#num = 3.124
#numero = 1000
#print(" o numero pi é {:.2f}".format(num))
#print(" o numero pi é {:b}".format(numero))

#numeros random

#num = random.randint(1,6)
#print(num)
#y = random.random()
#print(y)
#minha_lista = ["pedra" , "papel", "tesoura"]
#z = random.choice(minha_lista)
#print(z)
#cards = [1,2,3,4,5,6,7,8,9,"j","q","k","a"]
#random.shuffle(cards)
#print(cards)

#exception
#try:
#    numerador = int(input("coloque um numero:"))
#    denominador= int(input("coloque um numero:"))
#    resultado = numerador / denominador
#except ZeroDivisionError as e:
#    print(e)
#    print("não da pra dividir por 0")
#except ValueError as e:
#    print(e)
    #    print("so funciona com numero")
    #except Exception as e:
#    print(e)
    #    print("alguma coisa deu erro")
    #else:
#    print(resultado)
    #finally:
#    print("sempre executa")

#file

#path = "C:\\Users\\Caio\\Documents\\esse"
#if os.path.exists(path):
#    print("existe")
#    if os.path.isfile(path):
#        print("é um arquivo")
#    elif os.path.isdir(path):
#        print("diretorio")
#else:
#    print(("não existe"))

#try:
#    with open('test.tx') as file:
#        print(file.read())
#except FileNotFoundError as e:
#    print(e)
#    print('file não existe')

#escrvendo uma file
#text = "asaassas"
#with open('test.txt','a') as file:
#    file.write(text)

#copiando uma file
#shutil.copyfile('test.txt','copy.txt')


#replacing files
#source = "test"
#destination = "C:\\Users\\Caio\\Documents\\novinho"

#try:
#    if os.path.exists(destination):
#        print("já existe esse arquivo")
#    else:
#        os.replace(source,destination)
#except FileNotFoundError as e:
#    print(e)
#    print("não foi possivel achar a file")

#deletando files
#path = "folder"
#try:
#        #os.remove(path)
#        #os.rmdir(path)
#        shutil.rmtree(path)
#except FileNotFoundError as e:
#    print(e)
#    print("file não foi achada")
#except PermissionError as e:
#    print("voce não ter permissão para deletar isso")
#except OSError as e:
#    print(e)
#    print("não esta vazio")
#else:
#    print(path + " foi deletad0 ")