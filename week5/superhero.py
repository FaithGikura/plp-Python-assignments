class Superhero:
    def __init__(self, name, power, universe):
        self.name = name
        self.power = power
        self.universe = universe

    def introduce(self):
        print(f"I am {self.name} from the {self.universe} universe, and I can {self.power}!")

    def fight(self):
        print(f"{self.name} is fighting evil with {self.power}!")


class TechHero(Superhero):
    def __init__(self, name, power, universe, gadget):
        super().__init__(name, power, universe)
        self.gadget = gadget

    def use_gadget(self):
        print(f"{self.name} uses their advanced {self.gadget}!")

class MagicHero(Superhero):
    def __init__(self, name, power, universe, spell):
        super().__init__(name, power, universe)
        self.spell = spell

    def cast_spell(self):
        print(f"{self.name} casts a mighty {self.spell} spell!")


ironman = TechHero("Iron Man", "high-tech armor", "Marvel", "repulsor beams")
dr_strange = MagicHero("Doctor Strange", "mystic arts", "Marvel", "Time Manipulation")

ironman.introduce()
ironman.use_gadget()

dr_strange.introduce()
dr_strange.cast_spell()
