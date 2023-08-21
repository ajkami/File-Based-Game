class Player:
    def __init__(self, life, mana,exp):
        self.life = life
        self.mana = mana
        self.exp = exp
    
    def life_gain(self, gain):
        self.life = self.life + gain
        
    def life_loss(self, loss):
        self.life = self.life - loss
        
    def mana_gain(self, gain):
        self.mana = self.mana + gain
        
    def mana_loss(self, loss):
        self.mana = self.mana - loss
        
    def update(self):
        return "Life: " + str(self.life) + "\nMana: " + str(self.mana) + "\nExp: " + str(self.exp) + "\n"
        
    def get_name(self):
        return "AJ"
        