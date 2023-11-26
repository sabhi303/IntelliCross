import unittest
from vehicle import Vehicle  # Importing vehicle class

class TestVehicle(unittest.TestCase):

    # testing object construction
    # positive
    def test_init_1(self):
        side = "NORTH"
        lane = 0
        vehicles = {
            "EAST": {0: [], 1: [], 2: [], "crossed": 0},
            "NORTH": {0: [], 1: [], 2: [], "crossed": 0},
            "WEST": {0: [], 1: [], 2: [], "crossed": 0},
            "SOUTH": {0: [], 1: [], 2: [], "crossed": 0},
        }

        import pygame
        simulation = pygame.sprite.Group()

        vehicle = Vehicle(side=side, lane=lane,
                          vehicles=vehicles, simulation=simulation)

        self.assertEqual(side, vehicle.side)
        self.assertEqual(lane, vehicle.lane)
        self.assertEqual(False, vehicle.passed)

    # negative
    def test_init_2(self):
        side = "NORTH"
        lane = 0
        vehicles = {
            "EAST": {0: [], 1: [], 2: [], "crossed": 0},
            "NORTH": {0: [], 1: [], 2: [], "crossed": 0},
            "WEST": {0: [], 1: [], 2: [], "crossed": 0},
            "SOUTH": {0: [], 1: [], 2: [], "crossed": 0},
        }

        import pygame
        simulation = pygame.sprite.Group()

        vehicle = Vehicle(side=side, lane=lane,
                          vehicles=vehicles, simulation=simulation)

        self.assertNotEqual("SOUTH", vehicle.side)
        self.assertNotEqual(1, vehicle.lane)

    # testing vehicles
    # positive
    def test_init_3(self):
        side = "NORTH"
        lane = 0
        vehicles = {
            "EAST": {0: [], 1: [], 2: [], "crossed": 0},
            "NORTH": {0: [], 1: [], 2: [], "crossed": 0},
            "WEST": {0: [], 1: [], 2: [], "crossed": 0},
            "SOUTH": {0: [], 1: [], 2: [], "crossed": 0},
        }

        import pygame
        simulation = pygame.sprite.Group()

        vehicle = Vehicle(side=side, lane=lane,
                          vehicles=vehicles, simulation=simulation)

        self.assertEqual(1, len(vehicles["NORTH"][0]))

    # negative
    def test_init_4(self):
        side = "NORTH"
        lane = 0
        vehicles = {
            "EAST": {0: [], 1: [], 2: [], "crossed": 0},
            "NORTH": {0: [], 1: [], 2: [], "crossed": 0},
            "WEST": {0: [], 1: [], 2: [], "crossed": 0},
            "SOUTH": {0: [], 1: [], 2: [], "crossed": 0},
        }

        import pygame
        simulation = pygame.sprite.Group()

        vehicle = Vehicle(side=side, lane=lane,
                          vehicles=vehicles, simulation=simulation)

        self.assertNotEqual(1, len(vehicles["SOUTH"][0]))
        self.assertNotEqual(1, len(vehicles["EAST"][0]))
        self.assertNotEqual(1, len(vehicles["WEST"][0]))
        self.assertNotEqual(1, len(vehicles["SOUTH"][1]))
        self.assertNotEqual(1, len(vehicles["EAST"][1]))
        self.assertNotEqual(1, len(vehicles["WEST"][1]))
        self.assertNotEqual(1, len(vehicles["NORTH"][1]))

    # testing vehicle type
    # positive
    def test_init_5(self):
        side = "NORTH"
        lane = 0
        vehicles = {
            "EAST": {0: [], 1: [], 2: [], "crossed": 0},
            "NORTH": {0: [], 1: [], 2: [], "crossed": 0},
            "WEST": {0: [], 1: [], 2: [], "crossed": 0},
            "SOUTH": {0: [], 1: [], 2: [], "crossed": 0},
        }

        import pygame
        simulation = pygame.sprite.Group()

        vehicle = Vehicle(side=side, lane=lane,
                          vehicles=vehicles, simulation=simulation)

        self.assertTrue(vehicle.type in ["car", "truck", "bus"])

    # positive
    def test_init_6(self):
        side = "NORTH"
        lane = 0
        vehicles = {
            "EAST": {0: [], 1: [], 2: [], "crossed": 0},
            "NORTH": {0: [], 1: [], 2: [], "crossed": 0},
            "WEST": {0: [], 1: [], 2: [], "crossed": 0},
            "SOUTH": {0: [], 1: [], 2: [], "crossed": 0},
        }

        import pygame
        simulation = pygame.sprite.Group()

        vehicle = Vehicle(side=side, lane=lane,
                          vehicles=vehicles, simulation=simulation)

        self.assertFalse(vehicle.type in ["bike", "train", "tempo"])

    #positive
    def test_move_1(self):
            
        side = "EAST"
        lane = 0
        currentGreen=1
        currentYellow=0
        vehicles ={
            "EAST": {0: [], 1: [], 2: [], "crossed": 0},
            "NORTH": {0: [], 1: [], 2: [], "crossed": 0},
            "WEST": {0: [], 1: [], 2: [], "crossed": 0},
            "SOUTH": {0: [], 1: [], 2: [], "crossed": 0},
        }

        import pygame
        simulation = pygame.sprite.Group()
        
        vehicle = Vehicle(side=side, lane=lane,
                          vehicles=vehicles, simulation=simulation)
        x = vehicle.x 
        vehicle.move(currentYellow=currentYellow, currentGreen=currentGreen,
                    vehicles=vehicles)
        x = x + 0.6
        self.assertEqual(x, vehicle.x)

#negative
    def test_move_2(self):
            
        side = "EAST"
        lane = 0
        currentGreen=1
        currentYellow=0
        vehicles ={
            "EAST": {0: [], 1: [], 2: [], "crossed": 0},
            "NORTH": {0: [], 1: [], 2: [], "crossed": 0},
            "WEST": {0: [], 1: [], 2: [], "crossed": 0},
            "SOUTH": {0: [], 1: [], 2: [], "crossed": 0},
        }

        import pygame
        simulation = pygame.sprite.Group()
        
        vehicle = Vehicle(side=side, lane=lane,
                          vehicles=vehicles, simulation=simulation)
        x = vehicle.x 
        vehicle.move(currentYellow=currentYellow, currentGreen=currentGreen,
                    vehicles=vehicles)
        x = x + 1.8
        self.assertNotEqual(x, vehicle.x)

#positive
    def test_move_3(self):
            
        side = "WEST"
        lane = 0
        currentGreen=1
        currentYellow=0
        vehicles ={
            "EAST": {0: [], 1: [], 2: [], "crossed": 0},
            "NORTH": {0: [], 1: [], 2: [], "crossed": 0},
            "WEST": {0: [], 1: [], 2: [], "crossed": 0},
            "SOUTH": {0: [], 1: [], 2: [], "crossed": 0},
        }

        import pygame
        simulation = pygame.sprite.Group()
        
        vehicle = Vehicle(side=side, lane=lane,
                          vehicles=vehicles, simulation=simulation)
        x = vehicle.x 
        vehicle.move(currentYellow=currentYellow, currentGreen=currentGreen,
                    vehicles=vehicles)
        x = x - 0.6
        self.assertEqual(x, vehicle.x)

#negative
    def test_move_4(self):
            
        side = "WEST"
        lane = 0
        currentGreen=1
        currentYellow=0
        vehicles ={
            "EAST": {0: [], 1: [], 2: [], "crossed": 0},
            "NORTH": {0: [], 1: [], 2: [], "crossed": 0},
            "WEST": {0: [], 1: [], 2: [], "crossed": 0},
            "SOUTH": {0: [], 1: [], 2: [], "crossed": 0},
        }

        import pygame
        simulation = pygame.sprite.Group()
        
        vehicle = Vehicle(side=side, lane=lane,
                          vehicles=vehicles, simulation=simulation)
        x = vehicle.x 
        vehicle.move(currentYellow=currentYellow, currentGreen=currentGreen,
                    vehicles=vehicles)
        x = x - 2.1
        self.assertNotEqual(x, vehicle.x)


#positive
    def test_move_5(self):
            
        side = "NORTH"
        lane = 0
        currentGreen=1
        currentYellow=0
        vehicles ={
            "EAST": {0: [], 1: [], 2: [], "crossed": 0},
            "NORTH": {0: [], 1: [], 2: [], "crossed": 0},
            "WEST": {0: [], 1: [], 2: [], "crossed": 0},
            "SOUTH": {0: [], 1: [], 2: [], "crossed": 0},
        }

        import pygame
        simulation = pygame.sprite.Group()
        
        vehicle = Vehicle(side=side, lane=lane,
                          vehicles=vehicles, simulation=simulation)
        y = vehicle.y 
        vehicle.move(currentYellow=currentYellow, currentGreen=currentGreen,
                    vehicles=vehicles)
        y = y + 0.6
        self.assertEqual(y, vehicle.y)

#negative
    def test_move_6(self):
            
        side = "NORTH"
        lane = 0
        currentGreen=1
        currentYellow=0
        vehicles ={
            "EAST": {0: [], 1: [], 2: [], "crossed": 0},
            "NORTH": {0: [], 1: [], 2: [], "crossed": 0},
            "WEST": {0: [], 1: [], 2: [], "crossed": 0},
            "SOUTH": {0: [], 1: [], 2: [], "crossed": 0},
        }

        import pygame
        simulation = pygame.sprite.Group()
        
        vehicle = Vehicle(side=side, lane=lane,
                          vehicles=vehicles, simulation=simulation)
        y = vehicle.y 
        vehicle.move(currentYellow=currentYellow, currentGreen=currentGreen,
                    vehicles=vehicles)
        y = y + 2.06
        self.assertNotEqual(y, vehicle.y)
        

#positive
    def test_move_7(self):
            
        side = "SOUTH"
        lane = 0
        currentGreen=1
        currentYellow=0
        vehicles ={
            "EAST": {0: [], 1: [], 2: [], "crossed": 0},
            "NORTH": {0: [], 1: [], 2: [], "crossed": 0},
            "WEST": {0: [], 1: [], 2: [], "crossed": 0},
            "SOUTH": {0: [], 1: [], 2: [], "crossed": 0},
        }

        import pygame
        simulation = pygame.sprite.Group()
        
        vehicle = Vehicle(side=side, lane=lane,
                          vehicles=vehicles, simulation=simulation)
        y = vehicle.y 
        vehicle.move(currentYellow=currentYellow, currentGreen=currentGreen,
                    vehicles=vehicles)
        y = y - 0.6
        self.assertEqual(y, vehicle.y)

#negative
    def test_move_8(self):
            
        side = "SOUTH"
        lane = 0
        currentGreen=1
        currentYellow=0
        vehicles ={
            "EAST": {0: [], 1: [], 2: [], "crossed": 0},
            "NORTH": {0: [], 1: [], 2: [], "crossed": 0},
            "WEST": {0: [], 1: [], 2: [], "crossed": 0},
            "SOUTH": {0: [], 1: [], 2: [], "crossed": 0},
        }

        import pygame
        simulation = pygame.sprite.Group()
        
        vehicle = Vehicle(side=side, lane=lane,
                          vehicles=vehicles, simulation=simulation)
        y = vehicle.y 
        vehicle.move(currentYellow=currentYellow, currentGreen=currentGreen,
                    vehicles=vehicles)
        y = y - 0.3
        self.assertNotEqual(y, vehicle.y)            

