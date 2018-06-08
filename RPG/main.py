import random
import sys
import time
from character import *
from itens import *

inventario = {}
def batalha(hero, monster, randomlife,randomatk,randommagic,dfs):
    while True:
        if hero.life <= 0:
          print("Você morreu")
          break
        time.sleep(1)
        print("------------------------------------------------")
        print("")
        print("Vida do", monster.nome, monster.life)
        print("")
        print("Level:", hero.level)
        print(hero.nome)
        print("Vida", hero.life, "/", hero.maxlife)
        print("Mana", hero.mana, "/", hero.maxmana)
        print("Ouro",hero.gold)
        print("Xp",hero.xp)
        print("")
        print("")
        print("Ataque(1)")
        print("Ataque magico(2)")
        print("Defender(3)")
        print("Inventario(4)")
        while True:
          try:
            choice = int(input())
            break
          except:
            print("Digite uma opção valida")
        if choice == 1:
          print(hero.attack(monster))
        elif choice == 2:
          hero.magic = hero.magic - monster.dfs 
          if hero.magic <= 10:
              hero.magic = 10
              hero.spell(0)
              for i in hero.magias.keys():
                print(hero.magias[i][0]);
              print("(0) Voltar")
              escolha = input('Qual magia você quer usar? ')
              if escolha == '0':
                batalha(hero, monster, randomlife,randomatk,randommagic,dfs)
              else:
                escolha = escolha.upper()
                usar = hero.magias[escolha]
                if usar[1] > hero.mana:
                  print("Você não tem mana para esse ataque")
                else:
                  hero.spell(usar[1])#Usar 1 é o custo
                  time.sleep(1)
                  print(usar[3]) #Usar 3 é a mensagem
                  monster.life = monster.life - usar[2]#Usar 2 é o dano
                  hero.magic = hero.magic +monster.dfs
          else:
              hero.spell(0)
              for i in hero.magias.keys():
                print(hero.magias[i][0]);
                print("(0) Voltar")
              escolha = input('Qual magia você quer usar? ')
              escolha = escolha.upper()
              if escolha == '0':
                batalha(hero, monster, randomlife,randomatk,randommagic,dfs)
              elif escolha not in hero.magias.keys():
                print("Essa magia não existe")
                batalha(hero, monster, randomlife,randomatk,randommagic,dfs)
              else:
                usar = hero.magias[escolha]
                if usar[1] > hero.mana:
                  print("Você não tem mana para esse ataque")
                else:
                  hero.spell(usar[1])
                  time.sleep(1)
                  print(usar[3])
                  monster.life = monster.life - usar[2]
                  hero.magic = hero.magic +monster.dfs
        elif choice == 3:
            time.sleep(1)
            print("Você está em modo defensivo")
        elif choice == 4:
          if (len(inventario)) == 0:
            print("Inventario Vazio")
            batalha(hero, monster, randomlife,randomatk,randommagic,dfs)
          else:
            for i in inventario.keys():
              print(inventario[i][0]);
            print("(0) Voltar")
            escolha = input('Qual item você quer usar? ')
            if escolha == '0':
              batalha(hero, monster, randomlife,randomatk,randommagic,dfs)
            else:
              escolha = escolha.upper()
              usar = inventario[escolha]
              del inventario[escolha]
              if escolha[0] =='L' or escolha[1] =='L':
                if usar[1]+hero.life >= hero.maxlife:
                  hero.life = hero.maxlife
                  print('Você restaurou toda sua vida')
                  batalha(hero, monster, randomlife,randomatk,randommagic,dfs)
                else:
                  hero.life = hero.life+usar[1]
                  print('Você restaurou '+str(usar[1])+' de vida')
                  batalha(hero, monster, randomlife,randomatk,randommagic,dfs)
              elif escolha[0] =='M' or escolha[1] =='M':
                if usar[1]+hero.mana >= hero.maxmana:
                  hero.mana = hero.maxmana
                  print('Você restaurou toda sua mana')
                  batalha(hero, monster, randomlife,randomatk,randommagic,dfs)
                else:
                  hero.mana = hero.mana+usar[1]
                  print('Você restaurou '+str(usar[1])+' de mana')
                  batalha(hero, monster, randomlife,randomatk,randommagic,dfs)
        sorteio(hero)
        if monster.life <= 0:
          time.sleep(1)
          print("Você derrotou o", monster.nome)
          chance = random.randint(1,100)
          if chance%2==0:
            aleatorio = random.randint(1,4)
            if aleatorio == 1:
              inventario[lp.name] = lp.info,lp.stats
              time.sleep(1)
              print('Você ganhou uma',lp.name)
            elif aleatorio ==2:
              time.sleep(1)
              inventario[gmp.name] = gmp.info,lp.stats
              print('Você ganhou uma',gmp.name)
            elif aleatorio ==3:
              time.sleep(1)
              inventario[mp.name] = mp.info,mp.stats
              print('Você ganhou uma',mp.name)
            elif aleatorio ==4:
              time.sleep(1)
              inventario[glp.name] = glp.info,glp.stats
              print('Você ganhou uma',glp.name)
          print("Você ganhou ",monster.gold,'peças de ouro')
          hero.gold = hero.gold + monster.gold
          hero.xp = hero.xp + monster.xp
          monster.life = randomlife
          monster.atk = randomatk
          monster.magic  = randommagic
          monster.dfs = dfs
          if hero.xp >=100:
            while hero.xp >= 100:
              monster.life = round(monster.life+monster.life*0.2)
              monster.atk = round(monster.atk+monster.atk*0.1)
              monster.magic = round(monster.magic+monster.magic*0.12)
              print("Subiu de nivel")
              hero.levelup()
            if hero.level%2==0:
              print("Você deseja ir para a loja?(S/N)")
              escolha = input("")
              escolha = escolha.upper()
              if escolha =='S':
                store(hero)
            break
          break
        else:
          mchoice = random.randint(1, 3)
          if mchoice == 1:
              if choice == 3:
                  monster.atk = monster.atk - hero.dfs
                  if monster.atk <= 0:
                      print("Você não sofreu dano")
                      monster.atk = monster.atk + hero.dfs
                  else:
                      hero.life = hero.life - monster.atk
                      time.sleep(1)
                      print(monster.attack())
                      monster.atk = monster.atk + hero.dfs
              else:
                  hero.life = hero.life - monster.atk
                  time.sleep(1)
                  print(monster.attack())
          elif mchoice == 2:
              time.sleep(1)
              print(monster.spell(hero))
          elif mchoice == 3:
              if choice == 3:
                  monster.magic = monster.magic - hero.dfs
                  if monster.magic <= 0:
                    print("Você não sofreu dano")
                    monster.magic = monster.magic + hero.dfs
                  else:
                      hero.life = hero.life - monster.magic
                      time.sleep(1)
                      print(monster.specialattack())
                      monster.magic = monster.magic + hero.dfs
              else:
                  hero.life = hero.life - monster.magic
                  print(monster.specialattack())


def sorteio(hero):
	sorteio = random.randint(1,100)
	if sorteio <=35:
	  sorteio2 = random.randint(1,10)
	  if sorteio2 <=6:
	    if hero.life < hero.maxlife:
	      minheal = hero.maxlife*0.02
	      maxheal = hero.maxlife*0.10
	      maxheal = round(maxheal)
	      minheal = round(minheal)
	      lifedice = random.randint(minheal,maxheal)
	      if lifedice > hero.maxlife-hero.life:
	        diference = hero.maxlife-hero.life
	        lifedice = diference
	        hero.life = hero.life+lifedice
	        time.sleep(1)
	        print("A luz sagrada lhe curou",lifedice,"de vida")
	      else:
	        hero.life = hero.life+lifedice
	        time.sleep(1)
	        print("A luz sagrada lhe curou",lifedice,"de vida")
	  elif sorteio2 >=7:
	    if hero.mana < hero.maxmana:
	      minirmana = hero.maxmana*0.05
	      maxrmana = hero.maxmana*0.15
	      minirmana = round(minirmana)
	      maxrmana = round(maxrmana)
	      manadice = random.randint(minirmana,maxrmana)
	      if manadice > hero.maxmana-hero.mana:
	        diference = hero.maxmana-hero.mana
	        manadice = diference
	        hero.mana = hero.mana+manadice
	        time.sleep(1)
	        print("A luz sagrada lhe restaurou",manadice,"de mana")
	      else:
	        hero.mana = hero.mana+manadice
	        time.sleep(1)
	        print("A luz sagrada lhe restaurou",manadice,"de mana")
def store(hero):
  print("*------------------------------*------------------------------*")
  print("Bem vindo a loja heroi")
  print("")
  toSell = {}
  stock = [mp,lp,gmp,glp,ws,ros,pop]
  random.shuffle(stock,random.random)
  for i in range(1,4):
    v = random.randint(0,(len(stock))-1)
    toSell[stock[v].name] = stock[v].info,stock[v].stats,stock[v].price,stock[v].type,stock[v].trade,stock[v]
    #0 é a info
    #1 é o status do item
    #2 é o preço
    #3 é o tipo
    #4 é descrição
    #5 é o objeto
  for i in range(0,(len(toSell))):
    print("Gold",hero.gold)
    if (len(toSell)) == 0:
      print("Estou sem itens, volte outra hora")
    for i in toSell.keys():
      print(toSell[i][4]);#0 é a info
    print('(0) Sair')
    print("Qual item você vai querer?")
    escolha = input("")
    if escolha == '0':
      print("Até mais heroi")
      
    else:
      escolha = escolha.upper()
      usar = toSell[escolha]
      hero.gold = hero.gold-usar[2]
      if usar[3] == 'consumable':
        inventario[escolha] = usar[0],usar[1]
        print("Obrigado pela compra")
        print("")
        del toSell[escolha]
      else:
        usar[5].useItem(hero)
        print("Obrigado pela compra")
        print("")
        del toSell[escolha]
    
  
  
  
  
name = input("Qual é o seu nome, heroi? ")
clas = int(input("Escolha sua classe:\n(1) Guerreiro\n(2) Arqueiro\n(3) Mago\n"))
print("Você só consegue armazenar uma poção de cada tipo")
print("MP: Mana potion")
print("LP: Life potion")
print("GLM: Great mana potion")
print("GLP: Great life potion")
print("Pressione enter quando estiver pronto")
asd = input("")
if clas == 1:
  player = Warrior(name)
elif clas ==2:
  player = Ranger(name)
elif clas ==3:
  player = Mage(name)
#Declarações ------------------------------------------------
Dracula = Dracula()
Ghoul = Ghoul()
Orc = Orc()
Golem = Golem()
Slime = Slime()
SlimeKing = SlimeKing()
lp = LifePotion()
mp= ManaPotion()
gmp = GreatManaPotion()
glp = GreatLifePotion()
ws = WoodShield()
ros = RingOfStrength()
pop = PearlOfPower()
IMP = IMP()
#Declarações ------------------------------------------------
while player.life > 0:
  monstercount = random.randint(1,4)
  print("monstercount",monstercount)
  if player.level == 7:
    batalha(player, SlimeKing, SlimeKing.life,SlimeKing.atk,SlimeKing.magic,SlimeKing.dfs)
    if player.life <=0:
      break
  if player.level >= 14:
    batalha(player, Dracula, Dracula.life,Dracula.atk,Dracula.magic,Dracula.dfs)
    if player.life <=0:
      break
  elif monstercount == 1:
    batalha(player, Slime, Slime.life,Slime.atk,Slime.magic,Slime.dfs)
  elif monstercount == 2 and player.level>=3:
    batalha(player, IMP, IMP.life,IMP.atk,IMP.magic,IMP.dfs)
  elif monstercount == 3 and player.level>=4:
    batalha(player, Ghoul, Ghoul.life,Ghoul.atk,Ghoul.magic,Ghoul.dfs)
  elif monstercount == 3 and player.level > 7:
    batalha(player, Golem, Golem.life,Golem.atk,Golem.magic,Golem.dfs)
  elif monstercount == 4 and player.level > 7:
    batalha(player, Orc, Orc.life,Orc.atk,Orc.magic,Orc.dfs)
