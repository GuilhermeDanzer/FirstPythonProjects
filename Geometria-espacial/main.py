from contas import *
import time
a = Contas()
print("Digite sua escolha para descobrir a area das seguintes figuras")
def menu():
  time.sleep(1)
  print("-----------------------------------------------")
  #print("Para o Triangulo Equilatero considere raiz de três como 1,73")
  print("")
  print("(1)Quadrado")
  print("(2)Retangulo")
  print("(3)Triangulo")
  print("(4)Triangulo Equilatero")
  print("(5)Paralelogramo")
  print("(6)Losango")
  print("(7)Trapezio")
  print("(8)Circulo")
  print("(9)Esfera")
  print("(10)Cilindro")
  print("(11)Cone")
  print("(12)Tronco Cone")
  print("(13)Tronco Piramide")
  print("(0)Sair")

  escolha = int(input())
  
  if escolha == 1:
    lado = int(input("Digite o lado: "))
    print(a.quadrado(lado))
    menu()
  
  elif escolha ==2:
    ladoa = int(input("Digite o lado maior: "))
    ladob = int(input("Digite o lado menor: "))
    print(a.retangulo(ladoa,ladob))
    menu()  
    
  elif escolha ==3:
    lado = int(input("Digite o lado: "))
    altura = int(input("Digite a altura: "))
    print(a.triangulo(lado,altura))
    menu()
    
  elif escolha ==4:
    lado = int(input("Digite o lado: "))
    print(a.trianguloEquilatero(lado))
    menu()
    
  elif escolha == 5:
    lado = int(input("Digite o lado: "))
    altura = int(input("Digite a altura"))
    print(a.paralelogramo(lado,altura))
    menu()
    
  elif escolha ==6:
    dMaior = int(input("Digite a diagonal maior: "))
    dMenor = int(input("Digite a diagonal menor: "))
    print(a.losango(dMaior,dMenor))
    menu()
 
  elif escolha == 7:
    bMaior = int(input("Digite a base maior: "))
    bMenor = int(input("Digite a base menor: "))
    print(a.trapezio(bMaior,bMenor))

  elif escolha == 8:
    raio = int(input("Digite o raio: "))
    print(a.circulo(raio))
    menu()
  
  elif escolha == 9:
    raio = int(input("Digite o raio: "))
    print(a.esferaA(raio))
    print(a.esferaV(raio))
    menu()

  elif escolha == 10:
    raio = int(input("Digite o raio: "))
    altura = int(input("Digite a altura: "))
    print(a.cilindroAL(raio,altura))
    print(a.cilindroB(raio))
    print(a.cilindroV(raio,altura))
    menu()
    
  elif escolha == 11:
    raio = int(input("Digite o raio: "))
    altura = int(input("Digite a altura: "))
    geratriz = int(input("Digite a geratriz: "))
    print(a.coneAL(raio,geratriz))
    print(a.coneB(raio))
    print(a.coneV(raio,altura))
    menu()
    
  elif escolha ==12:
    Raio = int(input("Digite o raio maior: "))
    raio = int(input("Digite o raio menor: "))
    altura = int(input("Digite a altura: "))
    print(a.coneV(Raio,raio,altura))
    menu()
  
  elif escolha ==13:
    bMaior = int(input("Digite a base maior: "))
    bMenor = int(input("Digite a base menor: "))
    altura = int(input("Digite a altura: "))
    print(a.troncoPiramide(bMaior,bMenor,altura))
    menu()
  elif escolha == 0:
    pass
    
menu()


 
    

    
  
  
  
  