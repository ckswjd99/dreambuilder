from basic import *
import component

from random import *

class market:   # List components
    def __init__(self):
        self.line_max_1 = 4
        self.line_max_2 = 3
        self.line_max_3 = 2
        self.line_1 = []
        self.line_2 = []
        self.line_3 = []
    
    def fill(self):
        pass

class dispenser:    # Dispense resources
    def __init__(self):
        self.show_num = 5
        self.queue = []

    def fill(self):
        while( len(self.queue) < self.show_num ):
            self.queue.append( randint(1,4) )

    def pop(self, index = 0):
        if(len(self.queue) > 0):
            result = self.queue.pop(index)
        else:
            result = -1
        self.fill()
        return result

class player:
    def __init__(self, system):
        self.system = system
        self.pocket_size = 5
        self.pocket = {'JOY':0, 'SADNESS':0, 'ANGER':0, 'FEAR':0}
        self.additional_pocket = {'JOY':0, 'SADNESS':0, 'ANGER':0, 'FEAR':0}
        self.storage_size = 1
        self.storage = []
        self.components= []
        self.research_ability = 3





class system:
    def __init__(self, runner):
        self.turn = 1
        self.phase = GAME_START

        self.market = market()
        self.dispenser = dispenser()
        self.player = player(self)

        self.market.fill()
        self.dispenser.fill()


def standard(runner):
    return system(runner)
