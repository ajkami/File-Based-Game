from player import Player

# Add a special attack for each monster that it has a 25% chance of using and a status effect to go with it

class Null:
    def __init__(self, life, damage):
        self.life = life
        self.damage = damage
        
        
class Slime:
    def __init__(self, life, damage):
        self.life = life
        self.damage = damage
        
    def attack(self,Player):
        Player.life_loss(self.damage)
        
    def life_loss(self, loss):
        self.life = self.life - loss
        
    def get_name(self):
        return "Slime"
    
    def update(self):
        return "Slime\nLife: " + str(self.life) + '\n'
        
    
        
        
class Troll:
    def __init__(self,life,damage):
        self.life = life
        self.damage = damage
        
    def attack(self,Player):
        Player.life_loss(self.damage)
        
    def life_loss(self, loss):
        self.life = self.life - loss
        
    def get_name(self):
        return "Troll"
    
    def update(self):
        return "Troll\nLife: " + str(self.life) + '\n'
        
        
        
class Skeleton:
    def __init__(self, life, damage):
        self.life = life
        self.damage = damage
        
    def attack(self,Player):
        Player.life_loss(self.damage)
        
    def life_loss(self, loss):
        self.life = self.life - loss
        
    def get_name(self):
        return "Skeleton"

    def update(self):
        return "Skeleton\nLife: " + str(self.life) + '\n'
        
        
class Vampire:
    def __init__(self, life, damage):
        self.life = life
        self.damage = damage
        
    def attack(self,Player):
        Player.life_loss(self.damage)
        
    def life_loss(self, loss):
        self.life = self.life - loss
        
    def get_name(self):
        return "Vampire"

    def update(self):
        return "Vampire\nLife: " + str(self.life) + '\n'


class Dragon:
    def __init__(self,life,damage):
        self.life = life
        self.damage = damage
        
    def attack(self,Player):
        Player.life_loss(self.damage)
        
    def life_loss(self, loss):
        self.life = self.life - loss
        
    def get_name(self):
        return "Dragon"
    
    def update(self):
        return "Dragon\nLife: " + str(self.life) + '\n'