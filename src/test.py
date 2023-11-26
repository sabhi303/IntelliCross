import unittest

# controller
from tests.controllerTests import ControllerTests

# vehiclle
from tests.vehicleTest import TestVehicle


if __name__ == "__main__":

    # controller
    controller = ControllerTests()
    unittest.main()


    #vehicle
    vehicle = TestVehicle()
    unittest.main()

