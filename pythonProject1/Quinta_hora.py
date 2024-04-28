#overriding

#class Animal:
#    def eat(self):
#       print("esta comendo")

#class Coelho(Animal):
#    def eat(self):
#        print("esta comendo agora")

#coelho = Coelho()
#coelho.eat()

#method chaining

#class Car:

#    def ligar(self):
#        print("voce ligou o carro")
#        return self

#    def desligar(self):
#        print("voce desligou o carro")
#        return self

#    def ok(self):
#        print("ok")
#        return self

#car = Car()
#car.ligar().ok().desligar()

#super()

#class Retangulo:
#    def __init__(self,lenght,width):
#        self.lenght = lenght
#        self.width = width


#class Quadrado(Retangulo):
#    def __init__(self,lenght,width):
#        super().__init__(lenght,width)

#    def area(self):
#        return self.lenght*self.width
#class Cubo(Retangulo):
#    def __init__(self,lenght,width,height):
#        super().__init__(lenght,width)
#        self.height = height

#    def volume(self):
#        return self.lenght*self.width*self.height


#cubo = Cubo(3,3,3)
#print(cubo.volume())


#classes abstract

#from abc import ABC,abstractmethod

#class veiculo(ABC):
#    @abstractmethod
#    def go(self):
#        pass

#    @abstractmethod
#    def stop(self):
#        pass

#class carro(veiculo):
#    def go(self):
#        print("estou dirigindo um carro")

#    def stop(self):
#        print("estou parando um carro")

#class moto(veiculo):
#    def go(self):
#        print("estou dirigindo uma moto")

#    def stop(self):
#        print("estou parando uma moto")

#carro = carro()
#moto = moto()

#carro.stop()
#moto.go()

#objects as arguments

