# vehicle and related stuff

import random
import configparser


class Vehicle:
    # co-ordinates
    x: int
    y: int
    position: str  # can be at north, south, etc.

    # uid
    id: str

    # movements
    direction: str
    isStopped: bool

    def __init__(self, x = None, y = None, id = None, position = None):
        
        # if not passed
        if x == None or y == None or id == None or position == None:
            print("Cannot Initiate!")
            exit -1
        
        self.x = x
        self.y = y
        self.direction = random.choice(
            ["straight", "left", "right"]
        )  # in our case, we're choosing random
        self.stopped = True

        # set speed so that we can move the co-ordinates
        defaults_config = configparser.ConfigParser()
        defaults_config.read("./config/defaults.config")
        defaults_config = defaults_config["VEHICLE"]

        self.speed = int(defaults_config["SPEED"])
    
    # move vehicles
    def move(self):
        # adjust the position below depending on the side
        if not self.stopped:
            if self.direction == "straight":
                pass
            elif self.direction == "left":
                pass
            elif self.direction == "right":
                pass

    # draw vehicle here            
    def draw(self):
        pass
