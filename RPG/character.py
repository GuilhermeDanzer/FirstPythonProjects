import random
import sys
import time

class Warrior():
    def __init__(self, nome):
        super().__init__()
        self.magias = {}
        self.nome = nome
        self.life = 400
        self.maxlife = 400
        self.mana = 100
        self.maxmana = 100
        self.atk = 10
        self.dfs = 10
        self.xp = 0
        self.magic = 20
        self.level = 1
        self.cost = 10
        self.gold = 20

    def attack(self,monster):
      self.atk =  self.atk - monster.dfs
      if self.atk < 1:
          self.atk = 10
          monster.life = monster.life - self.atk
          time.sleep(1)
          self.atk = self.atk + monster.dfs
      else:
          monster.life = monster.life - self.atk
          time.sleep(1)
          self.atk = self.atk + monster.dfs
      return 'Seu dano foi de ' + str(self.atk) + ' pontos de vida'

    def spell(self,cost):
        fsDamage = self.magic
        fsCost = self.cost
        self.magias['FS'] = ['FS:Você coloca sua espada em chamas e ataca o inimigo Dano: '+str(fsDamage)+' Custo '+str(fsCost),fsCost,fsDamage,'Sua espada flamejante deu ' + str(fsDamage) + ' de dano']
        self.mana = self.mana - cost
    
    def levelup(self):
      self.life = self.life + 50
      self.maxlife = self.maxlife + 50
      self.mana = self.mana + 25
      self.maxmana = self.maxmana + 25
      self.atk = self.atk + 5
      self.magic = self.magic + 5
      self.dfs = self.dfs + 10
      self.level = self.level + 1
      self.xp = self.xp - 100
      self.cost = self.cost + 5
      
class Ranger():
    def __init__(self, nome):
        super().__init__()
        self.magias = {}
        self.nome = nome
        self.life = 175
        self.maxlife = 175
        self.mana = 150
        self.maxmana = 150
        self.atk = 15
        self.dfs = 5
        self.xp = 0
        self.magic = 25
        self.level = 1
        self.cost = 15 
        self.gold = 20
        
    def attack(self,monster):
      self.atk =  self.atk - monster.dfs
      if self.atk < 1:
          self.atk = 10
          monster.life = monster.life - self.atk
          time.sleep(1)
          self.atk = self.atk + monster.dfs
      else:
          monster.life = monster.life - self.atk
          time.sleep(1)
          self.atk = self.atk + monster.dfs
      return 'Seu dano foi de ' + str(self.atk) + ' pontos de vida'

    def spell(self,cost):
        waCost = self.cost
        waDamage = self.magic
        self.magias['WA'] = ['WA:Você encanta sua flecha com vento e atira em seus oponentes Dano: '+str(waDamage)+' Custo '+str(waCost),waCost,waDamage,'Sua flecha de vento deu ' + str(waDamage) + ' de dano']
        self.mana = self.mana - cost
        
    def levelup(self):
      self.life = self.life + 25
      self.maxlife = self.maxlife + 25
      self.mana = self.mana + 25
      self.maxmana = self.maxmana + 25
      self.atk = self.atk + 10
      self.magic = self.magic + 10
      self.dfs = self.dfs + 3
      self.level = self.level + 1
      self.xp = self.xp - 100
      self.cost = self.cost + 5

class Mage():
    def __init__(self, nome):
        super().__init__()
        self.magias = {}
        self.nome = nome
        self.life = 100
        self.maxlife = 100
        self.mana = 300
        self.maxmana = 300
        self.atk = 5
        self.dfs = 0
        self.xp = 0
        self.magic = 5
        self.level = 1
        self.cost = 10 
        self.gold = 20
        
    def attack(self,monster):
      self.atk =  self.atk - monster.dfs
      if self.atk < 1:
          self.atk = 10
          monster.life = monster.life - self.atk
          time.sleep(1)
          self.atk = self.atk + monster.dfs
      else:
          monster.life = monster.life - self.atk
          time.sleep(1)
          self.atk = self.atk + monster.dfs
      return 'Seu dano foi de ' + str(self.atk) + ' pontos de vida'

    def spell(self,cost):
        fbDamage = self.magic+30
        fbCost = self.cost+15
        lbDamage = self.magic +15
        lbCost = self.cost
        msDamage = self.magic+400
        msCost = self.cost+200
        self.magias['LB'] = ['LB:Você faz um raio mágico cair em cima do seu oponente Dano: '+str(lbDamage)+ ' Custo '+ str(lbCost),lbCost,lbDamage,'Seu raio causou ' +str(lbDamage) + ' de dano']
        self.magias['FB'] = ['FB:Você cria e atira uma bola de fogo mágica em seu oponente Dano: '+str(fbDamage)+' Custo '+ str(fbCost),fbCost,fbDamage,'Sua bola de fogo causou '+str(fbDamage)+' de dano']        
        self.magias['MS'] = ['MS:Você invoca uma chuva de meteoros em cima de seu oponente Dano: '+str(msDamage)+' Custo '+ str(msCost),msCost,msDamage,'Sua chuva de meteoros causou '+str(msDamage)+' de dano']
        self.mana = self.mana - cost

    def levelup(self):
      self.life = self.life + 25
      self.maxlife = self.maxlife + 25
      self.mana = self.mana + 75
      self.maxmana = self.maxmana + 75
      self.atk = self.atk + 3
      self.magic = self.magic + 15
      self.dfs = self.dfs + 5
      self.level = self.level + 1
      self.cost = self.cost + 10
      self.xp = self.xp - 100


class Slime():
    def __init__(self):
      self.nome = "Slime"
      self.life = random.randint(26,30)
      self.atk = random.randint(5, 15)
      self.dfs = 0
      self.xp = 25
      self.magic = random.randint(20, 25)
      self.heal = random.randint(5, 10)
      self.gold = 10
    
    def stats(self):
        self.nome = "Slime"
        self.life = random.randint(30, 60)
        self.atk = random.randint(1, 15)
        self.xp = 25
        self.magic = random.randint(20, 35)
        self.heal = random.randint(5, 25)

      
    def attack(self):
        return 'O Slime deu ' + str(self.atk) + " de dano"

    def specialattack(self):
        return 'Você sofreu  ' + str(self.magic) + " de dano acído"

    def spell(self,hero):
        self.life = self.heal + self.life
        return 'O Slime se curou em ' + str(self.heal) + ' pontos de vida'


class Ghoul():
    def __init__(self):
        self.nome = "Ghoul"
        self.life = random.randint(90, 150)
        self.mana = 0
        self.atk = random.randint(20,60)
        self.dfs = 0
        self.xp = 50
        self.magic = random.randint(40,80)
        self.dfs = 0
        self.gold = 25

    def attack(self):
        return 'O Ghoul deu ' + str(self.atk) + " de dano"

    def spell(self,hero):
        self.atk = round(self.atk * 1.5)
        self.magic = round(self.magic * 2)
        return 'O ataque do monstro é ' + str(self.atk)

    def specialattack(self):
        return 'O Ghoul lhe mordeu dando  ' + str(
            self.magic) + " de dano necrotico"

class Golem():
  def __init__(self):
    self.nome = 'Golem'
    self.life = random.randint(200,400)
    self.atk = random.randint(30,40)
    self.dfs = random.randint(10,20)
    self.xp = 75
    self.magic = random.randint(40,60)
    self.gold = 50
    
  def attack(self):
      return 'O Golem deu ' + str(self.atk) + " de dano"

  def spell(self,hero):
      self.dfs = round(self.dfs * 1.5)
      return 'A redução de dano do Golem é de ' + str(self.dfs)

  def specialattack(self):
      return 'O Golem mandou uma chuva de pedra que provocou ' + str(
          self.magic) + " de dano"
  

class SlimeKing():
    def __init__(self):
        self.nome = "Slime King"
        self.life = random.randint(550, 700)
        self.mana = 0
        self.atk = random.randint(40, 60)
        self.dfs = 0
        self.xp = 150
        self.magic = random.randint(60, 70)
        self.heal = round(self.life * 0.05)
        self.gold = 100

    def attack(self):
        return 'O Slime King deu ' + str(self.atk) + " de dano"

    def specialattack(self):
        return 'Você sofreu ' + str(self.magic) + " de dano acído"

    def spell(self,hero):
        self.life = self.heal + self.life
        return 'O Slime King se curou em ' + str(self.heal) + ' pontos de vida'
        
class Dracula():
    def __init__(self):
        self.nome = "Dracula"
        self.life = random.randint(1000, 1500)
        self.mana = 0
        self.atk = random.randint(60, 90)
        self.dfs = 0
        self.xp = 250
        self.magic = random.randint(60,120)
        self.gold = 200
        

    def attack(self):
        return 'O Dracula deu ' + str(self.atk) + " de dano"

    def specialattack(self):
        self.life = round(self.magic+self.life)
        return 'O Dracula sugou ' + str(self.magic) + ' pontos da sua energia vital'

    def spell(self,hero):
        self.magic = round(self.magic + self.magic*0.1)
        return 'Agora Dracula pode sugar ' + str(self.magic) + ' pontos de energia vital'
        
class Orc():
  def __init__(self):
    self.nome = 'Orc'
    self.life = 350
    self.atk = random.randint(60,120)
    self.dfs = 0
    self.xp = 75
    self.magic = self.atk
    self.gold = 50

    
  def attack(self):
      return 'O Orc lhe acertou com uma clava que deu ' + str(self.atk) + " de dano"

  def spell(self,hero):
    if self.life <=125:
      self.atk = self.atk * 2
      self.dfs = self.dfs - 20
      berserker = True
      return 'O Orc entrou em modo berserker, seu ataque está muito mais forte'
      if berserker == True:
        return 'O Orc está ficando cada vez mais forte '
    else:
      return 'O Orc está rindo da sua cara'
      
  def specialattack(self):
      return 'O Orc acertou um golpe duplo ' + str(
          self.magic*2) + " de dano"
          
class IMP():
    def __init__(self):
        self.nome = "IMP"
        self.life = random.randint(40, 60)
        self.mana = 0
        self.atk = random.randint(30,50)
        self.dfs = 0
        self.xp = 45
        self.magic = random.randint(40,80)
        self.dfs = 0
        self.gold = 15

    def attack(self):
        return 'O IMP deu ' + str(self.atk) + " de dano"

    def spell(self,hero):
        hero.life = hero.life-(self.magic*0.5)
        return 'O fogo infernal conjurado pelo IMP causou' + str(self.magic) +' de dano'

    def specialattack(self):
        return 'O Ghoul lhe mordeu dando  ' + str(
            self.magic) + " de dano necrotico"