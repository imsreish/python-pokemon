# python concepts covered:
# - OOP in python
# - instance methods, static methods
# - dunder methods
# - If __name__ == "__main__"
# - implementing game logic
# create a Pokemon...
class Pokemon:
    def __init__(self, name, primary_type, max_hp):
        self.name = name
        self.primary_type = primary_type
        self.hp = max_hp
        self.max_hp = max_hp

    def __str__(self):
        return f"{self.name} ({self.primary_type}: {self.hp}/{self.max_hp})".format()

    # feed them to increase health...
    def feed(self):
        if self.hp < self.max_hp:
            self.hp += 1
            print(f"{self.name} now has {self.hp} HP")
        else:
            print(f"{self.name} is full")

    # make them battle and choose a winner...
    def battle(self, other):
        result = self.typewheel(self.primary_type, other.primary_type)
        print(f"Battle: {self.name} vs {other.name}")
        if result == "lose":
            self.hp -= 10
            print(f"{self.name} lost and now has an HP of {self.hp}")
        print(f"{self.name} fought {other.name} and the result is a {result}")

    @staticmethod
    def typewheel(type1, type2):
        result = {0: "lose", 1: "win", -1: "tie"}
        # mapping between types and result conditions
        game_map = {"water": 0, "fire": 1, "grass": 2}
        # implement win-lose matrix
        wl_matrix = [
            [-1, 1, 0], # wasser
            [0, -1, 1], # feuer
            [1, 0 -1], # grass
        ]
        # declare a winner
        wl_result = wl_matrix[game_map[type1]][game_map[type2]]
        return result[wl_result]


# example
if __name__ == "__main__":
    bulbi = (Pokemon(name="bulbasaur", primary_type="grass", max_hp=100))
    charchar = (Pokemon(name="charmander", primary_type="fire", max_hp=75))
    bulbi.battle(charchar)