from abc import ABC,abstractmethod

class Champion(ABC) :
    def __init__(self,champion_id :str,name :str,base_hp :int,base_atk :int):
        self.champion_id=champion_id
        self.name=name
        self.base_hp=base_hp
        self.base_atk=base_atk

    @abstractmethod
    def calculate_skill_damage(self):
        pass

    @abstractmethod
    def get_he(self):
        pass

    def get_combat_power(self):
        return self.base_hp+ (self.calculate_skill_damage()*1.5)

    def __add__(self, other):
        if isinstance(other, Champion) :
            return self.get_combat_power() + other.get_combat_power()
        elif isinstance (other,(int,float)):
            return self.get_combat_power() + other
        return NotImplementedError

    def __gt__(self, other):
        return self.get_combat_power() > other.get_combat_power()

    def display_info(self):

        if self.get_he()=='Warrior':
            status=f'Armor {self.shield_bonus}'

        else:
            status=f'Mana {self.ability_power}'

        print(f"{self.champion_id} {self.name}  {self.get_he()} {self.base_hp} {self.base_atk} {status} {self.get_combat_power()}")



class Warrior(Champion):

    def __init__(self, champion_id: str, name: str, base_hp: int, base_atk: int,shield_bonus :int):
        super().__init__(champion_id, name, base_hp, base_atk)
        self.shield_bonus=shield_bonus

    def calculate_skill_damage(self):
        return self.base_atk+self.shield_bonus

    def get_he(self):
        return 'Warrior'


class Mage(Champion):
    def __init__(self, champion_id: str, name: str, base_hp: int, base_atk: int,ability_power:float):
        super().__init__(champion_id, name, base_hp, base_atk)
        self.ability_power=ability_power
    def calculate_skill_damage(self):
        return self.base_atk*self.ability_power
    def get_he(self):
        return "Mage"


def display(lst):
    print("--- DANH SÁCH QUÂN CỜ TRONG BỂ TƯỚNG ---")
    print("Mã     | Tên tướng            | Hệ       | HP    | ATK   | Chỉ số riêng      | Chiến lực")
    for i in lst:
        i.display_info()


database=[
    Warrior("WAR01  ","Rikkei Knight ",1200 ,150 ,150),
    Warrior("WAR02   ","Steel Guardian",1500   ,200  ,200),
    Mage("MAG01  ","Rikkei Wizard ",800,500  ,250 )
]

display(database)