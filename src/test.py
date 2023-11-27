import unittest

# controller
from tests.controllerTests import ControllerTests

# vehicle
from tests.vehicleTest import TestVehicle

#sensor
from tests.sensorTests import TestSensor

#traffic signal
from tests.trafficsignalTests import Testtrafficsignal

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

    #traffic Signal
    trafficsignal= Testtrafficsignal()
    unittest.main()
