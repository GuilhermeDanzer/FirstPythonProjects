n = int(input("Digite um numero para saber sua tabuada: "))
if n > 10:
  for i in range(1,n+1):
    nx = n*i
    print(str(n) +"x"+str(i)+" = " +str(nx))

else:
  for i in range(1,11):
    nx = n*i
    print(str(n) +"x"+str(i)+" = " +str(nx))
  