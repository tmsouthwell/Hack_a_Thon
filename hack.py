# Use the starter code to make a RPG battle game between ninjas and pirates.
# Customize the attack methods on both the Ninja and Pirate class.
# Have an instance of a ninja and pirate battle it out until one's health is depleted.
# Ninja Bonus: Use Inheritance, Class Methods, and Static Methods within your code.

import random
        # Parent Class
# class CoffeeM:
#     def __init__(self,name):
#         self.name = name
#         self.water_temp = 200
#     def brew_now(self,beans):
#         print(f"Using {beans}!")
#         print("Brew now brown cow!")
#     def clean(self):
#         print("Cleaning!")


        # Child Class
# class CappuccinoM( CoffeeM ):
#     def __init__(self,name):
#         super().__init__(name)
#         self.milk = "whole"
#     def make_cappuccino(self,beans):
#         super.brew_now(beans)
#         print("Frothy!!!")

class Weapon:
    def __init__(self, WeaponName = "Hands", WeaponStrength = 20):
        self.WeaponName = WeaponName
        self.WeaponStrength = WeaponStrength


class NinjaWeapon(Weapon):
    def __init__(self, WeaponName, WeaponStrength):
        super().__init__(WeaponName, WeaponStrength)
        

    def ninjaWeaponAttack(self):
        print(self.WeaponName)

class PirateWeapon(Weapon):
    def __init__(self, WeaponName, WeaponStrength):
        super().__init__(WeaponName, WeaponStrength)
        
    
    # def pirateWeaponAttack(self):
    #     pass

class Ninja():
    def __init__( self , name):
        self.name = name
        self.strength = 10
        self.speed = 10
        self.health = 100