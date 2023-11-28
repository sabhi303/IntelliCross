# pygame stuff will go here

import pygame
import configparser
import time
import random
import threading
import sys
import json
import easygui
from itertools import chain

from vehicle import Vehicle
from trafficSignal import TrafficSignal
from sensor import Sensor
from controller import calculate_times, prioritize_lanes


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
timers = {}  # timers indicates the signal timing
priority = []  # priority indicates the lane


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


#
# Initialization of signals with default values
def initialize():
    global currentGreen, timers, priority, signals

    signals = []

    # for normal bootup
    while len(timers.keys()) != 4 or len(priority) != 4:
        continue

    signals = []

    # for normal bootup
    while len(timers.keys()) != 4 or len(priority) != 4:
        continue
    greenTimes = [timers[directionNumbers[i] + "_TIME"] for i in priority]
    allRed = (
        timers["EAST_TIME"]
        + timers["WEST_TIME"]
        + timers["NORTH_TIME"]
        + timers["SOUTH_TIME"]
    )

    redTimes = []
    for i in range(len(priority)):
        redTimes.append(allRed - sum(greenTimes[i:]))

    for i in range(1, len(redTimes)):
        redTimes[i] += 3 * (i - greenTimes[:i].count(0))

    s1 = TrafficSignal(
        redTimes[0] - timers["EAST_TIME"], defaultYellow, timers["EAST_TIME"]
    )
    signals.append(s1)

    s2 = TrafficSignal(
        redTimes[1] - timers["NORTH_TIME"], defaultYellow, timers["NORTH_TIME"]
    )
    signals.append(s2)

    s3 = TrafficSignal(
        redTimes[2] - timers["WEST_TIME"], defaultYellow, timers["WEST_TIME"]
    )
    signals.append(s3)

    s4 = TrafficSignal(
        redTimes[3] - timers["SOUTH_TIME"], defaultYellow, timers["SOUTH_TIME"]
    )
    signals.append(s4)

    for i in range(len(priority)):
        signals[priority[i]].red = redTimes[i] if signals[priority[i]].green else 0

    # all will be red initially for let's say 5 seconds
    time.sleep(5)

    currentGreen = priority.pop(0)

    repeat(priority=priority)


# eat..sleep..
def repeat(priority) -> bool:
    global currentGreen, currentYellow, nextGreen, signals

    currentYellow = 0  # set yellow signal off
    if signals[currentGreen].green > 0:
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
        signals[currentGreen].green = "---"
        signals[currentGreen].red = "---"
        signals[currentGreen].yellow = "---"
        currentGreen = -1

        # ensure it is not dead till vehicles are there
        # while len(simulation) is not None:
        #     continue
        return

    # reset all signal times of current signal to default times
    signals[currentGreen].green = "---"
    signals[currentGreen].yellow = "---"
    signals[currentGreen].red = "---"

    currentGreen = nextGreen  # set next signal as green signal

    repeat(priority=priority)


# Update values of the signal timers after every second
def updateValues():
    global signals, noOfSignals
    for i in range(0, noOfSignals):
        if i == currentGreen:
            if currentYellow == 0:
                signals[i].green = (
                    "---" if signals[i].green == "---" else signals[i].green - 1
                )
            else:
                signals[i].yellow = (
                    "---" if signals[i].yellow == "---" else signals[i].yellow - 1
                )
        else:
            signals[i].red = "---" if signals[i].red == "---" else signals[i].red - 1


# Generating vehicles in the simulation, this will be from other class, that is sensor shit
def generateVehicles(data=None):
    # all vehicles in the scene, now
    global vehicles
    vehicles = {
        "EAST": {0: [], 1: [], 2: [], "crossed": 0},
        "NORTH": {0: [], 1: [], 2: [], "crossed": 0},
        "WEST": {0: [], 1: [], 2: [], "crossed": 0},
        "SOUTH": {0: [], 1: [], 2: [], "crossed": 0},
    }
    for direction in data:
        if direction == "ALL":
            pass
        else:
            for i in range(data[direction]["count"]):
                Vehicle(
                    lane=i % 2,
                    side=direction,
                    vehicles=vehicles,
                    simulation=simulation,
                )

    return


# display multiline text
def blit_text(surface, text, pos, font, color=pygame.Color("white")):
    words = [
        word.split(" ") for word in text.splitlines()
    ]  # 2D array where each row is a list of words.
    space = font.size(" ")[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    max_width -= 22
    max_height -= 100
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.


class Simulate:
    #
    data: None
    # Colours
    black = (0, 0, 0)
    white = (255, 255, 255)
    font = pygame.font.Font(None, 30)
    line_color = (255, 0, 0)
    isAnything = False  # are there any vehicles there?
    sensor = None
    screen = None
    isRunning = False  # is simulation is running

    def __init__(self):
        self.screen = None

    def start(self):
        # ofcourse
        # threading: signal change does not depend on how many vechicles the sensor detects, both should work on their own

        screenSize = (screenWidth, screenHeight)

        # Setting background image i.e. image of intersection
        self.screen = pygame.display.set_mode(screenSize)
        pygame.display.set_caption("IntelliCross - Smart Traffic Control")
        background = pygame.image.load(
            "assets/backgroundwithlogoandframe-13.jpg"
        ).convert()
        background = pygame.transform.smoothscale(background, screenSize)

        # Loading signal images and font
        redSignal = pygame.image.load("assets/signals/red.png")
        yellowSignal = pygame.image.load("assets/signals/yellow.png")
        greenSignal = pygame.image.load("assets/signals/green.png")

        # Loading Buttons image and font
        # button1
        button1 = pygame.image.load("assets/buttons/NormalTrafficCondition_button.png")
        button_width, button_height = button1.get_size()
        button1 = pygame.transform.smoothscale(
            button1, (button_width / 55, button_height / 55)
        )
        # position of button 1
        btn1_rect = button1.get_rect(topright=(1300, 50))

        # button2
        button2 = pygame.image.load("assets/buttons/PeakTrafficHours_button1.png")
        button_width2, button_height2 = button2.get_size()
        button2 = pygame.transform.smoothscale(
            button2, (button_width2 / 55, button_height2 / 55)
        )
        # position
        btn2_rect = button2.get_rect(topright=(1300, 150))

        # button3
        button3 = pygame.image.load("assets/buttons/Dynamic_button.png")
        button_width3, button_height3 = button3.get_size()
        button3 = pygame.transform.smoothscale(
            button3, (button_width3 / 55, button_height3 / 55)
        )
        # position
        btn3_rect = button3.get_rect(topright=(1300, 250))

        # display screen
        msgFont = pygame.font.SysFont("Turret Road",13)
        errmsg = ""
        display_screen_position = 1135, 410
        display_message = "\n\n***\nPlease Click On the scenario button above to get started!\n***\n"
        blit_text(
            self.screen,
            display_message,
            display_screen_position,
            msgFont,
            color=pygame.Color("white"),
        )

        thread2 = None
        global timers, priority, signals, simulation, vehicle, vehicles

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if not self.isRunning:
                        self.isRunning = True

                        if thread2 == None or not thread2.is_alive():
                            thread2 = threading.Thread(
                                name="initialization",
                                target=initialize,
                                args=(),
                                kwargs={},
                            )
                            thread2.daemon = True
                            thread2.start()

                        if btn1_rect.collidepoint(event.pos):
                            self.sensor = Sensor(scene="SCENE1")
                            self.data = self.sensor.getData()
                            timers = calculate_times(self.data)
                            for prior in prioritize_lanes(timers):
                                priority.append(signalPositions[prior])
                            generateVehicles(self.data)
                            display_message = """\n***\nVEHICLES COUNT\nA. NORTH : {NORTH}\nB. WEST : {WEST}\nC. SOUTH : {SOUTH}\nD. EAST : {EAST}\n***""".format(
                                NORTH=self.data["NORTH"]["count"],
                                WEST=self.data["EAST"]["count"],
                                SOUTH=self.data["SOUTH"]["count"],
                                EAST=self.data["WEST"]["count"],
                            )

                        if btn2_rect.collidepoint(event.pos):
                            msg1 = "Peak Traffic"
                            msg2 = "Hours"
                            self.sensor = Sensor(scene="SCENE2")
                            self.data = self.sensor.getData()
                            timers = calculate_times(self.data)
                            for prior in prioritize_lanes(timers):
                                priority.append(signalPositions[prior])
                            generateVehicles(self.data)

                            display_message = """\n***\nVEHICLES COUNT\nA. NORTH : {NORTH}\nB. WEST : {WEST}\nC. SOUTH : {SOUTH}\nD. EAST : {EAST}\n***""".format(
                                NORTH=self.data["NORTH"]["count"],
                                WEST=self.data["EAST"]["count"],
                                SOUTH=self.data["SOUTH"]["count"],
                                EAST=self.data["WEST"]["count"],
                            )

                        if btn3_rect.collidepoint(event.pos):
                            msg1 = "Dynamic Traffic"
                            msg2 = "Patterns"
                            message = "Enter Number of Vehicles for Different Lanes"
                            title = "Dynamic Vehicle Count"
                            fieldNames = [" North ", " West ", " South ", " East "]
                            fieldValues = [
                                2,
                                2,
                                2,
                                2,
                            ]  # we start with 2 as the default vehicle count for all the lanes
                            fieldDefValues = [2, 2, 2, 2]
                            fieldValues = easygui.multenterbox(
                                message, title, fieldNames, fieldValues
                            )
                            while 1:
                                if fieldValues == None:
                                    break
                                else:
                                    errmsg = ""
                                    for i in range(len(fieldNames)):
                                        if fieldValues[i].strip() == "":
                                            # Values can't be empty for any direction
                                            errmsg = errmsg + (
                                                '"%s" is a required field.\n\n'
                                                % fieldNames[i]
                                            )

                                        elif (
                                            0 > int(fieldValues[i].strip())
                                            or int(fieldValues[i].strip()) > 10
                                        ):
                                            # vehicle count cannot be less than 0 and more than 10
                                            errmsg = errmsg + (
                                                '"%s" vehicle count cannot  be less than 0 and more than 10.\n\n'
                                                % fieldNames[i]
                                            )
                                    if errmsg == "":
                                        sceneDynamic = {
                                            "CT_VEHICLES_NORTH": fieldValues[0],
                                            "CT_VEHICLES_WEST": fieldValues[3],
                                            "CT_VEHICLES_SOUTH": fieldValues[2],
                                            "CT_VEHICLES_EAST": fieldValues[1],
                                        }
                                        self.sensor = Sensor(
                                            scene="SCENE5", vehicle_counts=sceneDynamic
                                        )
                                        self.data = self.sensor.getData()
                                        timers = calculate_times(self.data)
                                        for prior in prioritize_lanes(timers):
                                            priority.append(signalPositions[prior])
                                        generateVehicles(self.data)
                                        display_message = """\n***\nVEHICLES COUNT\nA. NORTH : {NORTH}\nB. WEST : {WEST}\nC. SOUTH : {SOUTH}\nD. EAST : {EAST}\n***""".format(
                                            NORTH=self.data["NORTH"]["count"],
                                            WEST=self.data["EAST"]["count"],
                                            SOUTH=self.data["SOUTH"]["count"],
                                            EAST=self.data["WEST"]["count"],
                                        )
                                        break
                                    fieldValues = easygui.multenterbox(
                                        errmsg, title, fieldNames, fieldDefValues
                                    )

                                # Display text 1
                            img1 = msgFont.render(msg1, False, (255, 255, 255))
                            # Display text 1
                            img2 = msgFont.render(msg2, False, (255, 255, 255))
                            imgrect1 = img1.get_rect()
                            imgrect1.center = (1200, 320)
                            imgrect2 = img2.get_rect()
                            imgrect2.center = (1200, 360)

                            # display background in simulation
                            self.screen.blit(background, (0, 0))
                            self.screen.blit(button1, btn1_rect)
                            self.screen.blit(button2, btn2_rect)
                            self.screen.blit(button3, btn3_rect)
                            self.screen.blit(img1, imgrect1)
                            self.screen.blit(img2, imgrect2)

            # display background in simulation
            self.screen.blit(background, (0, 0))
            self.screen.blit(button1, btn1_rect)
            self.screen.blit(button2, btn2_rect)
            self.screen.blit(button3, btn3_rect)

            blit_text(
                self.screen,
                display_message,
                display_screen_position,
                msgFont,
                color=pygame.Color("white"),
            )

            # display signal and set timer according to current status: green, yello, or red
            signalTexts = ["", "", "", ""]
            if len(signals) == 4:
                for i in range(0, noOfSignals):
                    if i == currentGreen:
                        if currentYellow == 1:
                            signals[i].signalText = signals[i].yellow
                            self.screen.blit(yellowSignal, signalCoods[i])
                        else:
                            signals[i].signalText = signals[i].green
                            self.screen.blit(greenSignal, signalCoods[i])
                    else:
                        signals[i].signalText = signals[i].red
                        self.screen.blit(redSignal, signalCoods[i])

            # display timer
            if len(signals) == 4:
                for i in range(0, noOfSignals):
                    signalTexts[i] = self.font.render(
                        str(signals[i].signalText), True, self.white, self.black
                    )
                    self.screen.blit(signalTexts[i], signalTimerCoods[i])

            # display the vehicles
            for vehicle in simulation:
                # should not cross the right edge
                if vehicle.x > 1040:
                    vehicle.x = 1500

                self.screen.blit(vehicle.image, [vehicle.x, vehicle.y])
                vehicle.move(
                    currentGreen=currentGreen,
                    currentYellow=currentYellow,
                    vehicles=vehicles,
                )
                if (
                    (vehicle.side == "WEST" and vehicle.x < -20)
                    or (vehicle.side == "EAST" and vehicle.x > 1039)
                    or (vehicle.side == "SOUTH" and vehicle.y < 1)
                    or (vehicle.side == "NORTH" and vehicle.y > 730)
                ):
                    vehicle.passed = True

            if (
                len(list(filter(lambda x: x.passed == True, simulation)))
                == len(simulation)
            ) and (
                len(list(filter(lambda x: x.signalText == "---", signals)))
                == len(signals)
            ):
                simulation.empty()
                simulation = pygame.sprite.Group()  # re-assign just to check
                self.isRunning = False
                timers = {}
                priority = []
                display_message = "\n\n***\nPlease Click On the scenario button above to get started!\n***\n"

            # keep it running
            pygame.display.update()
