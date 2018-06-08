from fractions import Fraction
import math
parada = False
print("Insira a sua equação de bhaskara. Esse algoritimo só serve como confirmação da conta, sempre faça a conta em papel e caneta antes.")
a = int(input("Insira o A: "))
b = int(input("Insira o B: "))
c = int(input("Insira o C: "))
delta = (b**2) - 4*a*c
print(b**2)
print(-4*a*c)
print(delta)
div = 2*a
try:
  rdelta = int(math.sqrt(delta))
except ValueError:
  parada = True
  print("Numero sem raiz real")
if (parada == False): 
    x1 = (-b + rdelta)
    x2 = (-b - rdelta)
    print (str(-b) + "" + " √" + str(delta) + "/" + str(div))
    print(str(-b) + " + " + str(rdelta) + "/" + str(div))
    print("B+: "+str(-b + rdelta) + "/" + str(div))
    print("B-: "+str(-b - rdelta) + "/" + str(div))
    print("Resultado b+: " + str(Fraction(-b+rdelta,a*2)))
    print("Resultado b-: " + str(Fraction(-b-rdelta,a*2)))