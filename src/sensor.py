# sensor and related stuff

import uuid
import configparser


class Sensor:
    # vehicles
    VEHICLES_NORTH: list
    VEHICLES_EAST: list
    VEHICLES_SOUTH: list
    VEHICLES_WEST: list

    # counts
    CT_VEHICLES_NORTH: int
    CT_VEHICLES_EAST: int
    CT_VEHICLES_SOUTH: int
    CT_VEHICLES_WEST: int

    # config for scenarios
    scene_config = None
    scene = None

    # constructors
    def __init__(self, scene=None, vehicle_counts=None):
        # print(scene)
        if not scene:
            # scene = input("Tell me the scene: ")
            self.scene = "SCENE1"
            self.read_config(self.scene)
        elif scene == "SCENE5" and vehicle_counts is not None:
            # print("Entered Scene 5")
            # print(vehicle_counts)
            # print(type(vehicle_counts["CT_VEHICLES_NORTH"]))
            self.scene_config = scene
            self.CT_VEHICLES_NORTH = int(vehicle_counts["CT_VEHICLES_NORTH"])
            self.CT_VEHICLES_SOUTH = int(vehicle_counts["CT_VEHICLES_SOUTH"])
            self.CT_VEHICLES_EAST = int(vehicle_counts["CT_VEHICLES_EAST"])
            self.CT_VEHICLES_WEST = int(vehicle_counts["CT_VEHICLES_WEST"])
            self.setUids()

            # print(self.VEHICLES_NORTH)
        else:
            # print("Entered other scene")
            self.scene = scene
            self.read_config(self.scene)

    def read_config(self, scene):
        # read config file
        # scenarios
        scene_config = configparser.ConfigParser()
        scene_config.read("./config/scenes.config")

        if scene in scene_config:
            self.scene_config = scene_config[scene]

        else:
            print("Unable to proceed")
            return False

        if self.scene_config:
            self.CT_VEHICLES_NORTH = int(self.scene_config["CT_VEHICLES_NORTH"])
            self.CT_VEHICLES_SOUTH = int(self.scene_config["CT_VEHICLES_SOUTH"])
            self.CT_VEHICLES_EAST = int(self.scene_config["CT_VEHICLES_EAST"])
            self.CT_VEHICLES_WEST = int(self.scene_config["CT_VEHICLES_WEST"])

            # set uids
            self.setUids()

        else:
            print("Unable to proceed")
            exit - 1

    # get counts and all data
    def getData(self) -> bool:
        return {
            "NORTH": {"count": self.CT_VEHICLES_NORTH, "uids": self.VEHICLES_NORTH},
            "WEST": {"count": self.CT_VEHICLES_WEST, "uids": self.VEHICLES_WEST},
            "EAST": {"count": self.CT_VEHICLES_EAST, "uids": self.VEHICLES_EAST},
            "SOUTH": {"count": self.CT_VEHICLES_SOUTH, "uids": self.VEHICLES_SOUTH},
            "ALL": {
                "count": self.CT_VEHICLES_NORTH
                + self.CT_VEHICLES_WEST
                + self.CT_VEHICLES_EAST
                + self.CT_VEHICLES_SOUTH
            },
        }

    # set unique ids to vehicles
    def setUids(self) -> bool:
        # will add some collision detection mechanism later
        self.VEHICLES_SOUTH = [
            str(uuid.uuid4())[:8] for _ in range(int(self.CT_VEHICLES_SOUTH))
        ]
        self.VEHICLES_NORTH = [
            str(uuid.uuid4())[:8] for _ in range(int(self.CT_VEHICLES_NORTH))
        ]
        self.VEHICLES_EAST = [
            str(uuid.uuid4())[:8] for _ in range(int(self.CT_VEHICLES_EAST))
        ]
        self.VEHICLES_WEST = [
            str(uuid.uuid4())[:8] for _ in range(int(self.CT_VEHICLES_WEST))
        ]

    # except Exception as e:
    #     print(e)
