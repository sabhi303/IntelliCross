import pygame
import configparser
import json

defaults_config = configparser.ConfigParser()
defaults_config.read("./config/defaults.config")
vehicle_config = defaults_config["VEHICLE"]
coods_config = defaults_config["COORDINATES"]


# co-ordinates where vehicle starts
x = json.loads(coods_config["x"])
y = json.loads(coods_config["y"])

# Coordinates of stop lines
stopLines = json.loads(coods_config["stopLines"])
defaultStop = json.loads(coods_config["defaultStop"])

# Gap between vehicles
stoppingGap = 15  # stopping gap
movingGap = 15  # moving gap

class Vehicle(pygame.sprite.Sprite):
    speed: float  # speed of the vehicle
    side: str  # side of the intersection
    lane_number: int  # which lane you are in
    x: int  # x-position
    y: int  # y-position
    croseed: bool  # has crossed the signal
    index: int  # position in the queue
    image: str  # path of the image
    stop: tuple  # stopping co-ordinates

    def __init__(self, side, lane, vehicles, simulation) -> None:
        # initiliaze sprite

        pygame.sprite.Sprite.__init__(self)
        self.side = side
        self.lane = lane
        self.speed = float(vehicle_config["SPEED"])

        # set co-ordinates on side of vehicle, what is 3rd lane, let it be for some time
        if self.side == "WEST":
            self.x = 1040
        else:
            self.x = x[side][lane]
        self.y = y[side][lane]

        # has the vehicle crossed the stop line?
        self.crossed = False

        # add this in the line or queue
        vehicles[side][lane].append(self)

        # personal index for how many in front
        self.index = len(vehicles[side][lane]) - 1

        #
        path = "assets/vehicles/" + side + ".png"
        self.image = pygame.image.load(path)

        if (
            len(vehicles[side][lane]) > 1  # if any vehicles are there
            and vehicles[side][lane][self.index - 1].crossed
            == 0  # and has it already crossed
        ):  # if more than 1 vehicle in the lane of vehicle before it has crossed stop line
            if side == "EAST":
                self.stop = (
                    vehicles[side][lane][self.index - 1].stop
                    - vehicles[side][lane][self.index - 1].image.get_rect().width
                    - stoppingGap
                )  # setting stop coordinate as: stop coordinate of next vehicle - width of next vehicle - gap

            elif side == "WEST":
                self.stop = (
                    vehicles[side][lane][self.index - 1].stop
                    + vehicles[side][lane][self.index - 1].image.get_rect().width
                    + stoppingGap
                )

            elif side == "NORTH":
                self.stop = (
                    vehicles[side][lane][self.index - 1].stop
                    - vehicles[side][lane][self.index - 1].image.get_rect().height
                    - stoppingGap
                )

            elif side == "SOUTH":
                self.stop = (
                    vehicles[side][lane][self.index - 1].stop
                    + vehicles[side][lane][self.index - 1].image.get_rect().height
                    + stoppingGap
                )
        else:
            self.stop = defaultStop[side]  # set the stop co-ordinates

        # Set new starting and stopping coordinate
        if side == "EAST":
            temp = self.image.get_rect().width + stoppingGap
            x[side][lane] -= temp

        elif side == "WEST":
            temp = self.image.get_rect().width + stoppingGap
            x[side][lane] += temp

        elif side == "NORTH":
            temp = self.image.get_rect().height + stoppingGap
            y[side][lane] -= temp
        elif side == "SOUTH":
            temp = self.image.get_rect().height + stoppingGap
            y[side][lane] += temp
        simulation.add(self)

    # render image on the screen
    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))

    # move the vehicle
    def move(self, currentYellow, currentGreen, vehicles):
        if self.side == "EAST":
            if (
                self.crossed == 0
                and self.x + self.image.get_rect().width > stopLines[self.side]
            ):  # if the image has crossed stop line now
                self.crossed = 1

            if (
                self.x + self.image.get_rect().width <= self.stop
                or self.crossed == 1
                or (currentGreen == 0 and currentYellow == 0)
            ) and (
                self.index == 0
                or self.x + self.image.get_rect().width
                < (vehicles[self.side][self.lane][self.index - 1].x - movingGap)
            ):
                # (if the image has not reached its stop coordinate or has crossed stop line or has green signal) and (it is either the first vehicle in that lane or it is has enough gap to the next vehicle in that lane)
                self.x += self.speed  # move the vehicle

        elif self.side == "NORTH":
            if (
                self.crossed == 0
                and self.y + self.image.get_rect().height > stopLines[self.side]
            ):
                self.crossed = 1

            if (
                self.y + self.image.get_rect().height <= self.stop
                or self.crossed == 1
                or (currentGreen == 1 and currentYellow == 0)
            ) and (
                self.index == 0
                or self.y + self.image.get_rect().height
                < (vehicles[self.side][self.lane][self.index - 1].y - movingGap)
            ):
                self.y += self.speed

        elif self.side == "WEST":
            if self.crossed == 0 and self.x < stopLines[self.side]:
                self.crossed = 1
            if (
                self.x >= self.stop
                or self.crossed == 1
                or (currentGreen == 2 and currentYellow == 0)
            ) and (
                self.index == 0
                or self.x
                > (
                    vehicles[self.side][self.lane][self.index - 1].x
                    + vehicles[self.side][self.lane][self.index - 1]
                    .image.get_rect()
                    .width
                    + movingGap
                )
            ):
                self.x -= self.speed

        elif self.side == "SOUTH":
            if self.crossed == 0 and self.y < stopLines[self.side]:
                self.crossed = 1
            if (
                self.y >= self.stop
                or self.crossed == 1
                or (currentGreen == 3 and currentYellow == 0)
            ) and (
                self.index == 0
                or self.y
                > (
                    vehicles[self.side][self.lane][self.index - 1].y
                    + vehicles[self.side][self.lane][self.index - 1]
                    .image.get_rect()
                    .height
                    + movingGap
                )
            ):
                self.y -= self.speed