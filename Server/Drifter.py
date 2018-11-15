
import time
#import Classes

class Galaxy(object,):

    def __init__(self, name):
        self.name = name
        self.systems = {}

    def add_system(self, system,):
        self.systems[system.name] = system

    def remove_system(self, system,):
        del self.systems[system.name]



class System(object,):

    def __init__ (self, name,):
        self.name = name
        self.system_id = 1
        self.system_captains = {}
        self.system_ships = {}
        self.system_stars = {}
        self.system_planets = {}
        self.system_celestials = {}
        self.system_items = {}


    def add_item(self, tool):
        self.system_items[tool.name] = tool

    def remove_item(self, tool):
        del self.system_items[tool.name]


    def add_captain(self, captain,):
        self.system_captains[captain.name] = captain


    def remove_captain(self, captain,):
        del self.system_captains[captain.name]


    def add_star(self, star):
        self.system_stars[star.name] = star
        self.system_celestials[star.name] = star


    def remove_star(self, star):
        del self.system_stars[star.name]


    def add_planet(self, planet):
        self.system_planets[planet.name] = planet
        self.system_celestials[planet.name] = planet


    def remove_planet(self, planet):
        del self.system_planets[planet.name]


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
        self.ships_captain = [ShipYardCommander]
        self.where_is = SolSystem
        self.ship_equipment = {}


    def install_tool(self, tool):
        self.ship_equipment[tool.name] = tool



class Tool(object,):

    def __init__(self, name):
        self.installed_in = 'none'
        self.name = name

    def install(self, install_target,):
        self.installed_in = install_target
        install_target.install_tool(self,)


class Scanner(Tool,):

    def __init__(self, name):
        self.installed_in = EnterpriseA
        self.name = name


# Use the 'Scan' command to show information about your current system.
    def scan(self,):
        print ('Scanning...')
        i=1

        while i < 4:
            time.sleep(1)
            print('...')
            i += 1

        print ('You are currently in the '
               + self.installed_in.where_is.name
              )

        print ('This system contains '
               + str(len(self.installed_in.where_is.system_stars) )
               + ' stars.'
              )

        print('...')

        for name in self.installed_in.where_is.system_stars:
            print (name)

        print('...')

        print ('The '
                + self.installed_in.where_is.name
                + ' contains '
                + str(len(self.installed_in.where_is.system_planets) )
                + ' planets.'
              )

        print('...')

        for name in self.installed_in.where_is.system_planets:
            print (name)

        print('...')

        print ('There are '
                + str(len(self.installed_in.where_is.system_ships))
                + ' ships currently in the system.'
              )

        print('...')

        for name in self.installed_in.where_is.system_ships:
            print (name + ', ')

        print('...')

        print ('There are '
        + str(len(self.installed_in.where_is.system_captains))
        + ' life signs in the system.')

        print('...')

        for name in self.installed_in.where_is.system_captains:
            print (name)

        print('...')


class Warpdrive(Tool,):

    def __init__(self, name):
        self.installed_in = EnterpriseA
        self.name = name

        # Use the 'Jump -target_system' command to move your ship to a target_system.
    def jump(self,):
        print ('Please enter target system.')
        self.target_system = MilkyWay.systems[input()]
        print('Jumping...')
        self.installed_in.where_is.remove_ship(self.installed_in)
        self.installed_in.where_is = self.target_system
        self.installed_in.where_is.add_ship(self.installed_in)
        #time.sleep(3)
        print('You hear the whire of the Warpdrive die down as reality fades back into exsistance.')



#class DrifterApp():

    #def __init__(self,):
MilkyWay = Galaxy('Milky Way')
SolSystem = System('Sol System')
CentauriSystem = System('Centauri System')
Sol = Star('Sol')
AlphaCentauri = Star('Alpha Centauri')
BetaCentauri = Star('Beta Centauri')
ProximaCentauri = Star('Proxima Centauri')
ShipYardCommander = Captain('Ship Yard Commander')
Kirk = Captain('Kirk')
Picard = Captain('Picard')
EnterpriseA = Ship('Enterprise A','Constitution Class',)
EnterpriseD = Ship('Enterprise D','Galaxy Class',)
Scanner1 = Scanner('Scanner 1',)
Warpdrive1 = Warpdrive('Warpdrive 1',)

SolSystem.add_star(Sol)
CentauriSystem.add_star(AlphaCentauri)
CentauriSystem.add_star(BetaCentauri)
CentauriSystem.add_star(ProximaCentauri)
MilkyWay.add_system(SolSystem)
MilkyWay.add_system(CentauriSystem)

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
    SolSystem.add_planet(i)

SolSystem.add_captain(ShipYardCommander)
SolSystem.add_captain(Kirk)
SolSystem.add_captain(Picard)
SolSystem.add_ship(EnterpriseA)
SolSystem.add_ship(EnterpriseD)
SolSystem.add_item(Scanner1)
SolSystem.add_item(Warpdrive1)



print ('You awake adrift in space.')

command = ''

while command !='Quit':
    command = input('Please enter a command.')

    if command == 'Scan':
        Scanner1.scan()

    elif command == 'Install':
        print ('What would you like to install?')
        target_tool = SolSystem.system_items[input()]

        print ('Where would you like to install it?')
        install_target = SolSystem.system_ships[input()]
        target_tool.install(install_target)



    elif command == 'Jump':
        Warpdrive1.jump()

    elif command =='Quit':
        print('Entering Cryostasis...')

    else:
        print ('Unknown Command.')



#App = DrifterApp()
