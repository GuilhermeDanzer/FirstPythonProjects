import math
from fractions import Fraction
class Contas():
  def __init__(self):
    pass
  def quadrado(self,lado):
    area = lado**2
    return 'Área : '+str(area)
    
  def retangulo(self,ladoa,ladob):
    area = ladoa*ladob
    return 'Área : '+str(area)
  
  def triangulo(self,lado,h):
    area = lado*h
    area = Fraction(area,2)
    return 'Área : '+str(area)
  
  def trianguloEquilatero(self,lado):
    area = lado**2
    area = Fraction(area,4)
    #area = area*1.73
    return 'Área : '+str(area)+'√3'
    
  def paralelogramo(self,lado,h):
    area = lado*h
    return 'Área : '+str(area)
  
  def losango(self,dMaior,dMenor):
    area = dMaior*dMenor
    area = Fraction(area,2)
    return 'Área : '+str(area)
  
  def trapezio(self,bMaior,bMenor,h):
    area = bMaior+bMenor
    area = area*h
    area = Fraction(area,2)
    return 'Área : '+str(area)
  
  def circulo(self,r):
    area = (r**2)
    return 'Área : '+str(area)+'π'
    
  def esferaA(self,r):
    area = 4*(r**2)
    return 'Área : '+str(area)+'π'
    
  def esferaV(self,r):
    fracao = Fraction(4,3)
    volume = fracao*(r**3)
    return 'Volume: '+str(volume)+'π'
  
  def coneAL(self,r,g):
    area = r*g
    return 'Área Lateral: '+ str(area)+'π'
  
  def coneB(self,r):
    area = r**2
    return 'Área da Base: '+str(area)+'π'
    
  def coneV(self,r,h):
    volume = (r**2)*h
    volume = Fraction(volume,3)
    return 'Volume: '+str(volume)+'π'
    
  def cilindroB(self,r):
    area = r**2
    return 'Área da Base: '+str(area)+'π'
  
  def cilindroAL(self,r,h):
    area = r*h*2
    return 'Área Lateral: '+str(area)+'π'
  
  def cilindroV(self,r,h):
    volume = (r**2)*h
    return 'Volume: '+str(volume)+'π'
    
  def troncoCone(self,R,r,h):
    volume = h*((r**2)+(r*R)+(R**2))
    volume = Fraction(volume/3)
    return 'Volume: '+str(volume)+'π'
  
  def troncoPiramide(self,bMaior,bMenor,h):
    fracao = Fraction(h,3)
    raiz = bMaior*bMenor
    volume = bMaior+bMenor
    volume = volume +int(math.sqrt(raiz))
    volume = volume *fracao
    return 'Volume: '+str(volume)
    
    
    
    
    
    
    
    
    
  