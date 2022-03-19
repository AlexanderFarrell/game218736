places = dict()
class Place:
    def __init__(self, name):
        self.Name = name
        places[name] = self
        self.Neighbors = []

    def set_neighbors(self, neighbors):
        self.Neighbors = [places.get(a) for a in neighbors]

Place("Meadow")
Place("Forest")

places.get("Meadow").set_neighbors(['Forest'])
places.get("Forest").set_neighbors(['Meadow'])

name = input("Enter your name: ")
playing = True
location = places.get("Meadow")

while playing:
    i = input("What next?: ")
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
    else:
        print("Invalid command")