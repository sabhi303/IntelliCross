# pygame stuff will go here

import pygame
import configparser
import time
import random
import threading
import sys

from vehicle import Vehicle

# read config
defaults_config = configparser.ConfigParser()
defaults_config.read("./config/defaults.config")
defaults_config = defaults_config["VEHICLE"]


# Screensize; this also can be fetched from defaults file
screenWidth = 1358
screenHeight = 730

'''
# co-ordinates where vehicle starts
x = {
    "EAST": [0, 0],
    "NORTH": [550, 580],
    "WEST": [1040, 1040],
    "SOUTH": [480, 510],
}

y = {
    "EAST": [305, 335],
    "NORTH": [0, 0],
    "WEST": [375, 405],
    "SOUTH": [800, 800],
}
'''

# Default values of signal timers, this will be set laterrrrr
defaultGreen = {0: 2, 1: 2, 2: 2, 3: 2}
defaultRed = 150
defaultYellow = 1

# signal times, 4 signals are there
signals = []
noOfSignals = 4
currentGreen = 0  # Indicates which signal is green currently
currentYellow = 0  # Indicates whether yellow signal is on or off
nextGreen = (
    currentGreen + 1
) % noOfSignals  # Indicates which signal will turn green next

# Coordinates of signal image, timer, and vehicle count

# these are temp vars
margin1X = 10
margin1Y = 65
roadLength = 200
sig1X = ((screenWidth - (screenWidth * 0.2)) / 2 - roadLength / 2) - margin1X
sig1Y = (screenHeight / 2 - roadLength / 2) - margin1Y
margin2X = -23
margin2y = -23
sig2X = ((screenWidth - (screenWidth * 0.2)) / 2 + roadLength / 2) + margin2X
sig2Y = (screenHeight / 2 + roadLength / 2) + margin2y

signalCoods = [(sig1X, sig1Y), (sig2X, sig1Y), (sig2X, sig2Y), (sig1X, sig2Y)]
signalTimerCoods = [
    (sig1X, sig1Y - 20),
    (sig2X, sig1Y - 20),
    (sig2X, sig2Y + 90),
    (sig1X, sig2Y + 90),
]

'''
# Coordinates of stop lines
stopLines = {"EAST": 435, "NORTH": 265, "WEST": 645, "SOUTH": 465}
defaultStop = {
    "EAST": 435 - 10,
    "NORTH": 265 - 10,
    "WEST": 645 + 10,
    "SOUTH": 465 + 10,
}
print(stopLines)
print(defaultStop)
'''
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


class TrafficSignal:
    def __init__(self, red, yellow, green):
        self.red = red
        self.yellow = yellow
        self.green = green
        self.signalText = ""

# Initialization of signals with default values
def initialize():
    s1 = TrafficSignal(0, defaultYellow, defaultGreen[0])
    signals.append(s1)

    s2 = TrafficSignal(s1.red + s1.yellow + s1.green, defaultYellow, defaultGreen[1])
    signals.append(s2)

    s3 = TrafficSignal(defaultRed, defaultYellow, defaultGreen[2])
    signals.append(s3)

    s4 = TrafficSignal(defaultRed, defaultYellow, defaultGreen[3])
    signals.append(s4)

    repeat()


# eat..sleep..
def repeat():
    global currentGreen, currentYellow, nextGreen
    while (
        signals[currentGreen].green > 0
    ):  # while the timer of current green signal is not zero
        updateValues()
        time.sleep(1)

    currentYellow = 1  # set yellow signal on

    # reset stop coordinates of lanes and vehicles
    for i in range(0, 3):
        for vehicle in vehicles[directionNumbers[currentGreen]][i]:
            vehicle.stop = defaultStop[directionNumbers[currentGreen]]

    while (
        signals[currentGreen].yellow > 0
    ):  # while the timer of current yellow signal is not zero
        updateValues()
        time.sleep(1)

    currentYellow = 0  # set yellow signal off

    # reset all signal times of current signal to default times
    signals[currentGreen].green = defaultGreen[currentGreen]
    signals[currentGreen].yellow = defaultYellow
    signals[currentGreen].red = defaultRed

    currentGreen = nextGreen  # set next signal as green signal
    nextGreen = (currentGreen + 1) % noOfSignals  # set next green signal
    signals[nextGreen].red = (
        signals[currentGreen].yellow + signals[currentGreen].green
    )  # set the red time of next to next signal as (yellow time + green time) of next signal
    repeat()


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


# Generating vehicles in the simulation, this will be from other class, that is sensor shit
def generateVehicles():
    while True:
        # only one lane so, not needed tbh
        lane_number = random.randint(0, 1)
        temp = random.randint(0, 99)

        direction_number = 0

        # distance
        dist = [25, 50, 75, 100]
        if temp < dist[0]:
            direction_number = 0

        elif temp < dist[1]:
            direction_number = 1

        elif temp < dist[2]:
            direction_number = 2

        elif temp < dist[3]:
            direction_number = 3
        Vehicle(
            lane=lane_number,
            direction_number=direction_number,
            side=directionNumbers[direction_number],
            vehicles=vehicles,
            simulation=simulation
        )
        # zopava tyachya aaila
        time.sleep(1)


# ata bajar uthel
class Main:
    # ofcourse
    # threading: signal change does not depend on how many vechicles the sensor detects, both should work on their own
    thread1 = threading.Thread(
        name="initialization", target=initialize, args=()
    )  # initialization
    thread1.daemon = True
    thread1.start()

    # Colours
    black = (0, 0, 0)
    white = (255, 255, 255)

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

    # ithe jra interesting kai tri kru
    font = pygame.font.Font(None, 30)

    # this is generation
    thread2 = threading.Thread(
        name="generateVehicles", target=generateVehicles, args=()
    )  # Generating vehicles
    thread2.daemon = True
    thread2.start()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # display background in simulation
        screen.blit(background, (0, 0))

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
                    signals[i].signalText = "---"
                screen.blit(redSignal, signalCoods[i])
        signalTexts = ["", "", "", ""]

        # display signal timer
        for i in range(0, noOfSignals):
            signalTexts[i] = font.render(str(signals[i].signalText), True, white, black)
            screen.blit(signalTexts[i], signalTimerCoods[i])

        # display the vehicles
        for vehicle in simulation:
            if vehicle.x > 1040:
                vehicle.x = 1500
            
            screen.blit(vehicle.image, [vehicle.x, vehicle.y])
            vehicle.move(currentGreen=currentGreen, currentYellow=currentYellow, vehicles=vehicles)

        # keep it running
        pygame.display.update()


Main()
