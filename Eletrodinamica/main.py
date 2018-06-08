from fractions import Fraction
from decimal import Decimal
import math
a = 1
def menu():
  print("")
  print("Eletrodinamica")
  print("(1) Resistencia eletrica 'R'")
  print("(2) Tensão 'U'")
  print("(3) Intensidade da corrente 'i'")
  print("")
  print("Onda")
  print("(4) Velocidade da onda 'v'")
  print("(5) Comprimento da onda")
  print("(6) Frequencia da onda 'f'")
  print("(7) Sair")
  

while 0<a<8:
  menu()
  print("----------------------------------------------------------------")
  a = int(input("Digite sua opção: "))
  if a == 1:
    pergunta = input("A conta terá notação cientifica?(S/N)")
    if(pergunta=="S"):
      u = float(input("Digite a tensão: ")) #R = U/I
      notacao = int(input("Digite a notação: "))
      i = float(input("Digite a intensidade: "))
      conta = i*(10**notacao)
      resultado = (u/conta)
      print("A resistencia eletrica é "+ str(resultado) + " ohm")
    else:
      U = int(input("Digite a tensão: "))
      I = int(input("Digite a intensidade: "))
      resultado = Fraction(U,I)
      print("A resistencia eletrica é "+ str(resultado) + " ohm")
  elif a == 2:
    R = int(input("Digite a resistencia eletrica: "))
    I = int(input("Digite a intensidade da corrente: "))
    resultado = R*I
    print("A tensão é de " + str(resultado))
  elif a == 3:
    #pergunta = input("A conta terá notação cientifica?(S/N)")
    #if(pergunta=="S"):
      #u = float(input("Digite a tensão: "))
      #r = float(input("Digite a resistencia eletrica: "))
      #resultado = u/r
      #print("A intensidade da corrente é de " + str(resultado))
    #else:
    U = int(input("Digite a tensão: "))
    R = int(input("Digite a resistencia eletrica: "))
    resultado = Fraction(U,R)
    print("A intensidade da corrente é de " + str(resultado))
  elif a==4:
    pergunta= input("A conta terá notação ciencifica?(S/N)")
    if (pergunta =="S"):
      conv = input("É necessária a conversão?(S/N) ")
      if (conv =="S"):
        notacao = int(input("Digite a notação da frequencia: "))
        f = int(input("Digite a frequencia da onda: "))
        hz = f/60
        c = int(input("Digite o comprimento da onda: "))
        conta = (hz*(10**notacao) *(c*(10**(notacao*(-1)))))
        resultado = conta
        print(conta)
      else:
        notacao = int(input("Digite a notação da frequencia: "))
        f = int(input("Digite a frequencia da onda: "))
        c = int(input("Digite o comprimento da onda: "))
        conta = (f*(10**notacao) *(c*(10**(notacao*(-1)))))
        resultado = conta
        print(conta)
        
    else:
      conv = input("É necessária a conversão?(S/N) ")
      if conv == "S":
        f = int(input("Digite a frequencia da onda para a conversão: "))
        hz = f/60
        c = int(input("Digite o comprimento da onda: "))
        conta = c*hz
        print(conta)
      else:
        f = int(input("Digite a frequencia da onda: "))
        c = int(input("Digite o comprimento da onda: "))
        conta = c*f
        print(conta)
  if a == 7:
    break
      
    
  
