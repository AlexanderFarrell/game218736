places = dict()
class Place:
    def __init__(self, name, desc, things=[]):
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