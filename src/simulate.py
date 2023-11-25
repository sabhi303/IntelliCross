# pygame stuff will go here

import pygame
import configparser
import ConfigParserList
import time
import random
import threading
import sys
import json

from vehicle import Vehicle
from trafficsignal import TrafficSignal
from sensor import Sensor

# read config
defaults_config = configparser.ConfigParser()
defaults_config.read("./config/defaults.config")
vehicle_config = defaults_config["VEHICLE"]
screen_config = defaults_config["SCREEN"]
coods_config = defaults_config["COORDINATES"]

defaultStop = json.loads(coods_config["defaultStop"])


# Screensize; this also can be fetched from defaults file
screenWidth = int(screen_config["WIDTH"])
screenHeight = int(screen_config["HEIGHT"])

# Default values of signal timers, this will be set laterrrrr
defaultGreen = 0
defaultRed = 150
defaultYellow = 3
signalPositions = {"WEST_TIME": 2, "NORTH_TIME": 1, "EAST_TIME": 0, "SOUTH_TIME": 3}

# signal times, 4 signals are there
signals = []
noOfSignals = 4
global currentGreen, currentYellow, nextGreen
currentGreen = None  # Indicates which signal is green currently
currentYellow = None  # Indicates whether yellow signal is on or off
nextGreen = None  # Indicates which signal will be green next

# Coordinates of signal image, timer, and vehicle count
signalCoods = [(433, 200), (620, 200), (620, 442), (433, 442)]
signalTimerCoods = [(433, 180), (620, 180), (620, 532), (433, 532)]


# direction numbers
directionNumbers = {0: "EAST", 1: "NORTH", 2: "WEST", 3: "SOUTH"}

# all vehicles in the scene, now
vehicles = {
    "EAST": {0: [], 1: [], 2: [], "crossed": 0},
    "NORTH": {0: [], 1: [], 2: [], "crossed": 0},
    "WEST": {0: [], 1: [], 2: [], "crossed": 0},
    "SOUTH": {0: [], 1: [], 2: [], "crossed": 0},
}

# Gap between vehicles
stoppingGap = 15  # stopping gap
movingGap = 15  # moving gap

# init and group
pygame.init()
simulation = pygame.sprite.Group()


# Initialization of signals with default values
def initialize(timers, priority):
    global currentGreen

    print(priority)

    # for i in priority:
    #     signals.append(TrafficSignal(defaultRed, defaultYellow, timers[directionNumbers[i]+"_TIME"]))
    s1 = TrafficSignal(defaultRed, defaultYellow, timers["EAST_TIME"])
    signals.append(s1)

    s2 = TrafficSignal(defaultRed, defaultYellow, timers["NORTH_TIME"])
    signals.append(s2)

    s3 = TrafficSignal(defaultRed, defaultYellow, timers["WEST_TIME"])
    signals.append(s3)

    s4 = TrafficSignal(defaultRed, defaultYellow, timers["SOUTH_TIME"])
    signals.append(s4)

    # all will be red initially for let's say 5 seconds
    time.sleep(5)

    currentGreen = priority.pop(0)

    repeat(priority=priority)


# eat..sleep..
def repeat(priority) -> bool:
    global currentGreen, currentYellow, nextGreen

    currentYellow = 0  # set yellow signal off
    while (
        signals[currentGreen].green > 0
    ):  # while the timer of current green signal is not zero
        updateValues()
        time.sleep(1)

    currentYellow = 1  # set yellow signal on for current yellow

    # stop all the vehicles for yello
    for i in range(0, 3):
        for vehicle in vehicles[directionNumbers[currentGreen]][i]:
            vehicle.stop = defaultStop[directionNumbers[currentGreen]]

    while (
        signals[currentGreen].yellow > 0
    ):  # while the timer of current yellow signal is not zero
        updateValues()
        time.sleep(1)

    currentYellow = 0  # set yellow signal off

    if len(priority):
        nextGreen = priority.pop(0)
    else:
        return False

    # reset all signal times of current signal to default times
    signals[currentGreen].green = defaultRed
    signals[currentGreen].yellow = defaultYellow
    signals[currentGreen].red = defaultRed

    currentGreen = nextGreen  # set next signal as green signal

    print(signals[currentGreen].yellow, signals[currentGreen].green)
    signals[nextGreen].red = (
        signals[currentGreen].yellow + signals[currentGreen].green
    )  # set the red time of next to next signal as (yellow time + green time) of current signal

    repeat(priority=priority)


# Update values of the signal timers after every second
def updateValues():
    for i in range(0, noOfSignals):
        if i == currentGreen:
            if currentYellow == 0:
                signals[i].green -= 1
            else:
                signals[i].yellow -= 1
        else:
            signals[i].red -= 1

        updateTimers()


# Generating vehicles in the simulation, this will be from other class, that is sensor shit
def generateVehicles(data=None):
    for direction in data:
        if direction == "ALL":
            pass
        else:
            for _ in range(data[direction]["count"]):
                Vehicle(
                    lane=random.randint(0, 1),
                    side=direction,
                    vehicles=vehicles,
                    simulation=simulation,
                )

    return


def updateTimers():
    if currentGreen:
        x = str(int(signals[currentGreen].signalText) - 1)
        print(x)
        signals[currentGreen].signalText = str(
            int(signals[currentGreen].signalText) - 1
        )
    for i in range(0, noOfSignals):
        if currentGreen != i:
            x = str(int(signals[i].signalText) - 1)
            print(x)
            signals[i].signalText = str(int(signals[i].signalText) - 1)


def setTimers(timers, screen):
    # Colours
    black = (0, 0, 0)
    white = (255, 255, 255)
    signalTexts = ["", "", "", ""]
    font = pygame.font.Font(None, 30)

    totalTime = 0
    for _, time in timers.items():
        totalTime += time + 20  # 5*4 initial waiting time

    # display signal timer
    for i in range(0, noOfSignals):
        signals[i].signalText = str(
            totalTime - signals[i].green + 3
        )  # 3 seconds yellow time
        signalTexts[i] = font.render(str(signals[i].signalText), True, white, black)
        screen.blit(signalTexts[i], signalTimerCoods[i])


class Simulate:
    #
    timers: None
    data: None
    priority = []

    def __init__(self, data, timers, priorities):
        self.data = data
        self.timers = timers

        for prior in priorities:
            self.priority.append(signalPositions[prior])

    def start(self):
        # ofcourse
        # threading: signal change does not depend on how many vechicles the sensor detects, both should work on their own

        screenSize = (screenWidth, screenHeight)

        # Setting background image i.e. image of intersection
        screen = pygame.display.set_mode(screenSize)
        pygame.display.set_caption("IntelliCross - Smart Traffic Control Signal")

        background = pygame.image.load("assets/intersection.jpg").convert()
        background = pygame.transform.smoothscale(background, screenSize)
        screen.blit(background, (0, 0))

        # Loading signal images and font
        redSignal = pygame.image.load("assets/signals/red.png")
        yellowSignal = pygame.image.load("assets/signals/yellow.png")
        greenSignal = pygame.image.load("assets/signals/green.png")

        # this is vehicle generation

        # this thread is required for continuos traffic only one scenario
        thread1 = threading.Thread(
            name="generateVehicles", target=generateVehicles, args=()
        )  # Generating vehicles
        thread1.daemon = True
        # thread1.start()
        generateVehicles(self.data)

        thread2 = threading.Thread(
            name="initialization",
            target=initialize,
            args=(),
            kwargs={"timers": self.timers, "priority": self.priority},
        )  # initialization
        thread2.daemon = True

        # will wait for all vehicles to arrive at the scene
        thread2.start()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # display background in simulation
            screen.blit(background, (0, 0))

            # set timers
            setTimers(timers=self.timers, screen=screen)

            # display signal and set timer according to current status: green, yello, or red
            for i in range(0, noOfSignals):
                if i == currentGreen:
                    if currentYellow == 1:
                        signals[i].signalText = signals[i].yellow
                        screen.blit(yellowSignal, signalCoods[i])
                    else:
                        signals[i].signalText = signals[i].green
                        screen.blit(greenSignal, signalCoods[i])
                else:
                    if signals[i].red <= 10:
                        signals[i].signalText = signals[i].red
                    else:
                        updateTimers()
                    screen.blit(redSignal, signalCoods[i])

            # display the vehicles
            for vehicle in simulation:
                # should not cross the right edge
                if vehicle.x > 1040:
                    vehicle.x = 1500

                screen.blit(vehicle.image, [vehicle.x, vehicle.y])
                vehicle.move(
                    currentGreen=currentGreen,
                    currentYellow=currentYellow,
                    vehicles=vehicles,
                )

            # keep it running
            pygame.display.update()