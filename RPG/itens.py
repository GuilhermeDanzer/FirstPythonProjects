class ManaPotion():
  def __init__(self):
    self.name = 'MP'
    self.type = 'consumable'
    self.stats = 70
    self.info = 'MP:Ela restaura '+str(self.stats)+' pontos de mana'
    self.price = 20
    self.trade = 'MP:Essa poção restaura '+str(self.stats)+' pontos de mana. Ele custa '+str(self.price)+' peças de ouro'



class LifePotion():
  def __init__(self):
    self.name = 'LP'
    self.type = 'consumable'
    self.stats = 80
    self.info = 'LP:Ela restaura '+str(self.stats)+ ' pontos de vida'
    self.price = 25
    self.trade = 'LP:Essa poção restaura '+str(self.stats)+' pontos de vida. Ele custa '+str(self.price)+' peças de ouro'


    
class GreatManaPotion():
  def __init__(self):
    self.name = 'GMP'
    self.type = 'consumable'
    self.stats = 140
    self.info = 'GMP:Ela restaura '+str(self.stats)+' pontos de mana'
    self.price = 40
    self.trade = 'GMP:Essa poção grande restaura '+str(self.stats)+' pontos de mana. Ele custa '+str(self.price)+' peças de ouro'


class GreatLifePotion():
  def __init__(self):
    self.name = 'GLP'
    self.type = 'consumable'
    self.stats = 160
    self.info = 'GLP:Ela restaura '+str(self.stats)+' pontos de vida'
    self.price = 50
    self.trade = 'GLP:Essa poção grande restaura '+str(self.stats)+' pontos de vida. Ele custa '+str(self.price)+' peças de ouro'


class WoodShield():
    def __init__(self):
        self.name = 'WS'
        self.type = 'equipment'
        self.stats = 10
        self.price = 50
        self.info ='a'
        self.trade = 'WS:Esse escudo de madeira lhe da mais '+str(self.stats)+' de defesa. Ele custa '+str(self.price)+' peças de ouro'
    
    def useItem(self,hero):
        hero.dfs = hero.dfs +self.stats

  
class RingOfStrength():
    def __init__(self):
        self.name = 'ROS'
        self.type = 'equipment'
        self.stats = 5
        self.price = 50
        self.info ='a'
        self.trade = 'ROS:Esse anel aumenta a força de seus ataques em '+str(self.stats)+' pontos. Ele custa ' +str(self.price)+' peças de ouro'
    
    def useItem(self,hero):
        hero.atk = hero.atk+self.stats


class PearlOfPower():
    def __init__(self):
        self.name = 'POP'
        self.type = 'equipment'
        self.stats = 10
        self.price = 50
        self.info ='a'
        self.trade = 'POP:Essa poderosa perola azul intensifica sua força magica em '+str(self.stats)+' pontos. Ela custa '+str(self.price)+' peças de ouro'

    def useItem(self,hero):
        hero.magic = hero.magic+self.stats