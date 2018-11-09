
import time


class System(object,):

    def __init__ (self, system_name,):
        self.system_name = system_name
        self.system_id = 1
        self.system_captains = {}
        self.system_celestials = {}
        self.system_ships = {}


    def add_captain(self, captain,):
        self.system_captains[captain.name] = captain


    def remove_captain(self, captain,):
        del self.system_captains[captain.name]


    def add_celestial(self, celestial):
        self.system_celestials[celestial.name] = celestial


    def remove_celestial(self, celestial):
        del self.system_celestials[celestial.name]


    def add_ship(self, ship):
        self.system_ships[ship.name] = ship


    def remove_ship(self, ship):
        del self.system_ships[ship.name]

class celestial(object,):
    def __init__(self,):
        return

class Star(celestial,):

    def __init__(self, name,):
        self.name = name


class Planet(celestial,):

    def __init__(self, name,):
        self.name = name


class Captain(object,):

    def __init__(self, name,):
        self.name = name


class Ship(object,):

    def __init__(self, name, ship_class,):
        self.name = name
        self.ship_class = ship_class
        self.ships_captain = ShipYardCommander
        self.where_is = SolSystem

    def jump(self,target_system):
        self.target_system = target_system
        self.whereis.remove_ship(self.name)
        self.where_is = target_system
        self.whereis.add_ship(self.name)




class Tool(object,):
    def __init__(self,):
        return



class Scanner(Tool,):

    def __init__(self,):
        return

    def scan(self,):
        print ('Scanning...')
        i=1
        for i < 4
            print('...')
            i = i + 1
        print ('You are currently in the ' + SolSystem.system_name)
        print ('This system contains 1 G-type star, ' + Sol.name + '.')

        print ('The ' + SolSystem.system_name
                      + ' contains '
                      + str(len(SolSystem.system_celestials) - 1)
                      + ' planets.'
                      )

        for name in SolSystem.system_celestials:
            print (name + '', '')

        print ('There are '
               + str(len(SolSystem.system_ships))
               + ' ships in the system.')

        for name in SolSystem.system_ships:
            print (name + ', ')

        print ('There are '
        + str(len(SolSystem.system_captains))
        + ' life signs in the system.')

        for name in SolSystem.system_captains:
            print (name + ', ')



SolSystem = System('Sol System')
CentauriSystem = System(' Centauri System')
Sol = Star('Sol')
AlphaCentauri = Star('Alpha Centauri')
ShipYardCommander = Captain('Ship Yard Commander')
Kirk = Captain('Kirk')
Picard = Captain('Picard')
EnterpriseA = Ship('Enterprise A','Constitution Class',)
EnterpriseD = Ship('Enterprise D','Galaxy Class',)
Scanner = Scanner()

SolSystem.add_celestial(Sol)
CentauriSystem.add_celestial(AlphaCentauri)

sol_planets = [
        'Mercury',
        'Venus',
        'Terra',
        'Mars',
        'Saturn',
        'Jupiter',
        'Neptune',
        'Uranus',
        ]

for i in sol_planets:
    i = Planet(i)
    SolSystem.add_celestial(i)

    SolSystem.add_captain(Kirk)
    SolSystem.add_captain(Picard)
    SolSystem.add_ship(EnterpriseA)
    SolSystem.add_ship(EnterpriseD)


print ('You awake adrift in space.')
command = ''
while command !='Quit':

    command = input('Please enter a command.')
    if command == 'Scan':
        Scanner.scan()

    elif command =='Quit':
        print('Entering Cryostasis...')

    else:
        print ('Unknown Command.')
