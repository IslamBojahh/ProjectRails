# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 10:07:05 2019

@author: ORCAS_ISLAM
"""
import random
class Warrier(object):
    def __init__(self):
        self.health=50
        self.attack=5
    
    def is_alive(self):
        if self.health>0:
            return True 
        else:
            return False
    def equip_weapon(self, weapon):
        pass
        
        
class Knight(Warrier):
    def __init__(self):
        super().__init__()
        self.attack=7
    def equip_weapon(self, weapon):
        self.health+=weapon.health
        self.attack+=weapon.attack
        
class Defender(Warrier):
    def __init__(self):
        super().__init__()
        self.health=60
        self.attack=3
        self.defense=2
        
    def equip_weapon(self, weapon):
        self.health+=weapon.health
        self.attack+=weapon.attack
        self.defense+=weapon.defense

class Rookie(Warrier):
   def __init__(self):
       super().__init__()
       self.health = 50
       self.attack = 1
       
   def equip_weapon(self, weapon):
       self.health+=weapon.health
       self.attack+=weapon.attack

class Vampire(Warrier):
    def __init__(self):
       super().__init__()
       self.health = 40
       self.attack = 4
       self.vampirism=0.5
    def equip_weapon(self, weapon):
       self.health+=weapon.health
       self.attack+=weapon.attack
       self.vampirism=weapon.vampirism

class Lancer(Warrier):
    def __init__(self):
       super().__init__()
       self.health = 50
       self.attack = 6
    def equip_weapon(self, weapon):
       self.health+=weapon.health
       self.attack+=weapon.attack
       
class Healers(Warrier):
    def __init__(self):
       super().__init__()
       self.health = 60
       self.attack = 0
    def equip_weapon(self, weapon):
       self.health+=weapon.health
       self.attack+=weapon.attack
    
    def heal(self , fighter):
        fighter.health+=2
        if fighter.health>fighter.__class__().health:
            fighter.health=fighter.__class__().health

class Warlord(Warrier):
    def __init__(self):
       super().__init__()
       self.health = 100
       self.attack = 4
       self.defense =2
    

       
def fight(fighter1 , fighter2):
    First=True
    while fighter1.health >0 and fighter2.health >0:
        if  First==True:
            fighter2.health-=fighter2.attack
        else:
            fighter1.health-=fighter1.attack
        
        First=not First
            
    if fighter1.health >0:
        return True 
    else:
        return False


    

class Army(object):
    def __init__(self):
        self.army=[]
    
    def add_units(self , army):
        self.army.append(army)

class Battles(object):
    def __init__(self):
        pass        
    def fight(self ,army1 , army2):
        while len(army1.army)>0 and len(army2.army)>0:
            fighter1=random.choice(army1.army)
            fighter2=random.choice(army2.army)
            First=True
            while fighter1.health >0 and fighter2.health >0:
                if  First==True:
                    if fighter1.__class__.__name__=='Lancer' and fighter2.__class__.__name__=='Knight' :
                        fighter2.health-=int(fighter1.attack*0.5)
                    else:
                        fighter2.health-=fighter2.attack
                    if fighter1.__class__.__name__=='Vampire':
                        fighter1.health+=int(fighter2.attack*fighter1.vampirism)
                        

                else:
                    if fighter2.__class__.__name__=='Lancer' and fighter1.__class__.__name__=='Knight' :
                        fighter1.health-=int(fighter2.attack*0.5)
                    else:
                        fighter1.health-=fighter1.attack
                    if fighter2.__class__.__name__=='Vampire':
                        fighter2.health+=int(fighter1.attack*fighter2.vampirism)
                First=not First

                    
            if fighter1.health <=0:
                army1.army.remove(fighter1)
            else:
                army2.army.remove(fighter2)
                
        if len(army1.army)==0:
            return False
        else:
            return True
        
    def straight_fight(self,army1 , army2):
        smallest=0
        while len(army1.army)>0 and len(army2.army)>0:
            if len(army1.army)>len(army2.army):
                smallest=len(army2.army)
            elif len(army2.army)>len(army1.army):
                smallest=len(army1.army)
            else:
                smallest=len(army1.army)
            First=True
            deleted_List1=[]
            deleted_List2=[]

            for i in range(smallest):
                fighter1=army1.army[i]
                fighter2=army2.army[i]
                if  First==True:
                    if fighter1.__class__.__name__=='Lancer' and fighter2.__class__.__name__=='Knight' :
                        fighter2.health-=int(fighter1.attack*0.5)
                    else:
                        fighter2.health-=fighter2.attack
                    if fighter1.__class__.__name__=='Vampire':
                        fighter1.health+=int(fighter2.attack*fighter1.vampirism)
                        

                else:
                    if fighter2.__class__.__name__=='Lancer' and fighter1.__class__.__name__=='Knight' :
                        fighter1.health-=int(fighter2.attack*0.5)
                    else:
                        fighter1.health-=fighter1.attack
                    if fighter2.__class__.__name__=='Vampire':
                        fighter2.health+=int(fighter1.attack*fighter2.vampirism)
                First=not First
                
                if fighter1.health <=0:
                    
                    deleted_List1.append(fighter1)
                else:
                    deleted_List2.append(fighter2)
            
            for item in deleted_List1:
                army1.army.remove(item)
            for item in deleted_List2:
                army2.army.remove(item)
    
    
    def move_units(self , army):
        lancer=[]
        healer=[]
        soldier=[]
        for item in army:
            if item.__class__.__name__=='Lancer':
                lancer.append(item)
            elif item.__class__.__name__=='Healers':
                healer.append(item)
            else:
                soldier.append(item)
        
        return lancer+soldier+healer
                
                
    
class Weapon(object):
    def __init__(self , health, attack, defense, vampirism, heal_power):
        self.health=health
        self.attack=attack
        self.defense=defense
        self.vampirism=vampirism
        self.heal_power=heal_power
        

class Sword (Weapon):
    def __init__(self):
        self.health =5
        self.attack =2

class Shield (Weapon):
    def __init__(self):
        self.health =20
        self.attack =-1
        self.defense=1
        
class GreatAxe (Weapon):
    def __init__(self):
        self.health =-15
        self.attack =5
        self.defense=-2
        self.vampirism =0.1
        
class Katana (Weapon):
    def __init__(self):
        self.health =-20
        self.attack =6
        self.defense=-5
        self.vampirism =0.5

class MagicWand (Weapon):
    def __init__(self):
        self.health =30
        self.attack =3
        self.heal_power =3

            
            

            
            
                
        
    
            
        
    
        

chuck = Warrier()
bruce = Warrier()
carl = Knight()
dave = Warrier()
xx=Vampire()
yy=Defender()

Army1=Army()
Army1.add_units(carl)
Army1.add_units(dave)

Army2=Army()
Army2.add_units(xx)
Army2.add_units(yy)



b=Battles()



print(b.straight_fight(Army2 , Army1)) 

h=Healers()
h.heal(carl)
