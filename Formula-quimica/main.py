r = 0.0821
t = int(input("Digite a temperatura em K: "))
deltan = float(input("Digite o delta n: "))
kc = float(input("Digite o coeficiente de equilibrio(atm): "))
a = float(r*t)
b = float(a**deltan)
c = float(kc*b)
print("Resposta final:",c)
pergunta = input("Você deseja colocar em notação cientifica?(S/N) ")
if pergunta == "S":
  notacao=int(input("Digite em qual notação você deseja colocar: "))
  calculo = c*((10)**notacao)
  print("Resposta em notação: "+str(calculo)+"*10^"+str(notacao))
  
