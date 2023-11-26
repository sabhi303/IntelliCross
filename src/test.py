import unittest

# controller
from tests.controllerTests import ControllerTests


# vehicle
from tests.vehicleTest import TestVehicle

#sensor
from tests.sensorTests import TestSensor

if __name__ == "__main__":

    # controller
    controller = ControllerTests()
    unittest.main()


    #vehicle
    vehicle = TestVehicle()
    unittest.main()

    # sensor
    sensor = TestSensor()
    unittest.main()