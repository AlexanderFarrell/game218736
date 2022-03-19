places = dict()
class Place:
    def __init__(self, name, desc=" in a place you can't make out.", things=[]):
        self.Name = name
        places[name] = self
        self.Neighbors = []
        self.Things = []
        self.Description = desc

    def set_neighbors(self, neighbors):
        self.Neighbors = [places.get(a) for a in neighbors]

    def place_things(self, things):
        pass

Place("Meadow", "a peaceful meadow")
Place("Forest", "a dark, murky forest.")

Place("Chipotle")
Place("Meadow")
Place("Forest")
Place("Desert")
Place("Home")
Place("Romania")
Place("Arctic")
Place("Space")
Place("Jungle")

places.get("Meadow").set_neighbors(['Forest'])
places.get("Forest").set_neighbors(['Meadow', 'Desert', 'Home', 'Romania', 'Arctic', 'Space', 'Jungle'])
places.get("Jungle").set_neighbors(['Meadow', 'Desert', 'Home', 'Romania', 'Arctic', 'Space'])
places.get("Space").set_neighbors(['Meadow', 'Desert', 'Home', 'Romania', 'Arctic', 'Jungle'])
places.get("Arctic").set_neighbors(['Meadow', 'Desert', 'Home', 'Romania', 'Jungle', 'Space'])
places.get("Romania").set_neighbors(['Meadow', 'Desert', 'Home', 'Jungle', 'Arctic', 'Space'])
places.get("Home").set_neighbors(['Meadow', 'Desert', 'Jungle', 'Romania', 'Arctic', 'Space', 'Chipotle'])
places.get("Desert").set_neighbors(['Meadow', 'Jungle', 'Home', 'Romania', 'Arctic', 'Space'])
places.get("Chipotle").set_neighbors(['Home'])

places.get("Meadow").set_neighbors(['Forest'])
places.get("Forest").set_neighbors(['Meadow'])

name = input("Enter your name: ")
playing = True
location = places.get("Meadow")

while playing:
    i = input("\nWhat next?: ")
    if i == "move":
        print(f"\t(Neighbors: {', '.join([a.Name for a in location.Neighbors])})")
        a = input("Where would you like to go?: ")
        if a in places.keys():
            location = places.get(a)
            print(f"You move to the {location.Name}")
        else:
            print(f"No such place {a}")
    elif i == 'say':
        print(f"{name}: {input('What would you like to say?: ')}")
    elif i == 'where':
        print(f"I am currently in the {location.Name}. From here, I can go "
              f"to the {', '.join([a.Name for a in location.Neighbors])}")
    elif i == "quit":
        playing = False
    elif i == 'look':
        print(f"You see {location.Description}.\n ")
    else:
        print("Invalid command")