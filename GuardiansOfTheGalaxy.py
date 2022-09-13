class Spaceship:
    def __init__(self, name, clocation):
        self.name = name
        self.clocation = clocation
        self.guardian = []
        self.known_locations = []
    
    def location(self): # returns the location of the spaceship
        return self.clocation
    
    def go_to(self, planet): # changes the location of the spaceship
        if self.guardian == None or self.guardian == []:
            print(self.name, "does not have any guardians on board")
        else:
            if planet not in self.known_locations:
                print(planet, "is not a known location")
            else:
                self.clocation = planet
                print(self.name, "travels to", planet)
    
    def contains(self): # returns the name of the spaceship
        return self.guardian

class Guardian:
    def __init__(self, name, clocation, *known_planets):
        self.name = name
        self.clocation = clocation
        self.knownplanets = []
        for i in known_planets:
            self.knownplanets.append(i)
        self.onboard = False
        if self.clocation not in self.knownplanets:
            self.knownplanets.append(self.clocation)
    
    def known_planets(self):
        return self.knownplanets

    def board(self, ship): # boards the spaceship
        if ship.clocation != self.clocation:
            print(self.name, "cannot board the", ship.name)
        else:
            ship.guardian.append(self.name)
            ship.guardian = list(set(ship.guardian))
            print(self.name, "boards the", ship.name)
            for i in self.knownplanets:
                if i not in ship.known_locations:
                    ship.known_locations.append(i)
                else:
                    pass
            self.knownplanets = ship.known_locations
            self.knownplanets = list(set(self.knownplanets))
            self.clocation = ship.clocation
            self.onboard = True
            self.ship = ship
    
    def location(self):
        if self.onboard == True:
            print(self.name, "is on the ship", self.ship.name, "at the planet", self.ship.clocation)
        else:
            print(self.name, "is on the planet", self.clocation) 