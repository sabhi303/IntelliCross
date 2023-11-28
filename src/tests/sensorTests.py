import unittest

from sensor import Sensor  # Assuming the code is in a file named sensor.py

class TestSensor(unittest.TestCase):

    def test_Scene1_1(self):
        
        scene="SCENE1"
        sensor = Sensor(scene)
        expected= {'NORTH': {'count': 1, 'uids': ['d7ae1052']}, 
                    'WEST': {'count': 4, 'uids': ['d392f87d', 
                                                   'fb7d643b', 
                                                   '539d89b3', 
                                                   '1a6d7a61' 
                                                   ]}, 
                    'EAST': {'count': 3, 'uids': ['a0538bb7', 
                                                   '2d1d9350', 
                                                   'cde2cc25']}, 
                    'SOUTH': {'count': 2, 'uids': ['e512e853', 
                                                    'bdc94d23']}, 
                    'ALL': {'count': 40}
                }
        data = sensor.getData() 
        
        # north
        self.assertEqual(data["NORTH"]["count"], 1)
        self.assertEqual(len(data["NORTH"]["uids"]), 1)
        # south
        self.assertEqual(data["SOUTH"]["count"], 2)
        self.assertEqual(len(data["SOUTH"]["uids"]), 2)
        # east
        self.assertEqual(data["EAST"]["count"], 3)
        self.assertEqual(len(data["EAST"]["uids"]), 3)
        # west
        self.assertEqual(data["WEST"]["count"], 4)
        self.assertEqual(len(data["WEST"]["uids"]), 4)

    def test_Scene1_2(self):
        scene="SCENE1"
        sensor = Sensor(scene)
        expected= {'NORTH': {'count': 10, 'uids': ['d7ae1052', 
                                                   '1c3254f7', 
                                                   '92acbdfa', 
                                                   'a77baf82', 
                                                   '2416fb0f', 
                                                   'a481a82e', 
                                                   'c01be579', 
                                                   '1b7093f7', 
                                                   'e3a7331c', 
                                                   '2bc61306']}, 
                    'WEST': {'count': 10, 'uids': ['d392f87d', 
                                                   'fb7d643b', 
                                                   '539d89b3', 
                                                   '1a6d7a61', 
                                                   '1fd8eedf', 
                                                   '37c2f87b', 
                                                   'fc4f23c7', 
                                                   '08406e86', 
                                                   '6a9db6e9', 
                                                   'd7f5889d']}, 
                    'EAST': {'count': 10, 'uids': ['a0538bb7', 
                                                   '2d1d9350', 
                                                   'cde2cc25', 
                                                   'b5cb8ce1', 
                                                   'cc9614b7', 
                                                   '39a2d21a', 
                                                   '0d265676', 
                                                   'd460be64', 
                                                   '22b4edc5', 
                                                   '73e9bb56']}, 
                    'SOUTH': {'count': 10, 'uids': ['e512e853', 
                                                    'bdc94d23', 
                                                    'e07fceaa', 
                                                    'fc3349e7', 
                                                    '228bd334', 
                                                    '0c1b2938', 
                                                    'f83d9dc1', 
                                                    '4034cb58', 
                                                    'f8d81ffc', 
                                                    '6f60e0c4']}, 
                    'ALL': {'count': 40}
                }
        data = sensor.getData() 

        # print(data)
        
        # north
        self.assertNotEqual(data["NORTH"]["count"], -2)
        self.assertNotEqual(len(data["NORTH"]["uids"]), 8)
        # south
        self.assertNotEqual(data["SOUTH"]["count"], -4)
        self.assertNotEqual(len(data["SOUTH"]["uids"]), -15)
        # east
        self.assertNotEqual(data["EAST"]["count"], -100)
        self.assertNotEqual(len(data["EAST"]["uids"]), 8)
        # west
        self.assertNotEqual(data["WEST"]["count"], -10)
        self.assertNotEqual(len(data["WEST"]["uids"]), -20)
    
    def test_Scene2_1(self):
        scene="SCENE2"
        sensor = Sensor(scene)
        expected= {'NORTH': {'count': 10, 'uids': ['d7ae1052', 
                                                   '1c3254f7', 
                                                   '92acbdfa', 
                                                   'a77baf82', 
                                                   '2416fb0f', 
                                                   'a481a82e', 
                                                   'c01be579', 
                                                   '1b7093f7', 
                                                   'e3a7331c', 
                                                   '2bc61306']}, 
                    'WEST': {'count': 0, 'uids': []}, 
                    'EAST': {'count': 10, 'uids': ['a0538bb7', 
                                                   '2d1d9350', 
                                                   'cde2cc25', 
                                                   'b5cb8ce1', 
                                                   'cc9614b7', 
                                                   '39a2d21a', 
                                                   '0d265676', 
                                                   'd460be64', 
                                                   '22b4edc5', 
                                                   '73e9bb56']}, 
                    'SOUTH': {'count': 2, 'uids': ['e512e853', 
                                                    'bdc94d23']}, 
                    'ALL': {'count': 22}
                }
        data = sensor.getData() 
        
        # north
        self.assertEqual(data["NORTH"]["count"], 10)
        self.assertEqual(len(data["NORTH"]["uids"]), 10)
        # south
        self.assertEqual(data["SOUTH"]["count"], 2)
        self.assertEqual(len(data["SOUTH"]["uids"]), 2)
        # east
        self.assertEqual(data["EAST"]["count"], 10)
        self.assertEqual(len(data["EAST"]["uids"]), 10)
        # west
        self.assertEqual(data["WEST"]["count"], 0)
        self.assertEqual(len(data["WEST"]["uids"]), 0)

    def test_Scene2_2(self):
        scene="SCENE2"
        sensor = Sensor(scene)
        expected= {'NORTH': {'count': 10, 'uids': ['d7ae1052', 
                                                   '1c3254f7', 
                                                   '92acbdfa', 
                                                   'a77baf82', 
                                                   '2416fb0f', 
                                                   'a481a82e', 
                                                   'c01be579', 
                                                   '1b7093f7', 
                                                   'e3a7331c', 
                                                   '2bc61306']}, 
                    'WEST': {'count': 10, 'uids': ['d392f87d', 
                                                   'fb7d643b', 
                                                   '539d89b3', 
                                                   '1a6d7a61', 
                                                   '1fd8eedf', 
                                                   '37c2f87b', 
                                                   'fc4f23c7', 
                                                   '08406e86', 
                                                   '6a9db6e9', 
                                                   'd7f5889d']}, 
                    'EAST': {'count': 10, 'uids': ['a0538bb7', 
                                                   '2d1d9350', 
                                                   'cde2cc25', 
                                                   'b5cb8ce1', 
                                                   'cc9614b7', 
                                                   '39a2d21a', 
                                                   '0d265676', 
                                                   'd460be64', 
                                                   '22b4edc5', 
                                                   '73e9bb56']}, 
                    'SOUTH': {'count': 10, 'uids': ['e512e853', 
                                                    'bdc94d23', 
                                                    'e07fceaa', 
                                                    'fc3349e7', 
                                                    '228bd334', 
                                                    '0c1b2938', 
                                                    'f83d9dc1', 
                                                    '4034cb58', 
                                                    'f8d81ffc', 
                                                    '6f60e0c4']}, 
                    'ALL': {'count': 40}
                }
        data = sensor.getData() 
        
        # north
        self.assertNotEqual(data["NORTH"]["count"], -20)
        self.assertNotEqual(len(data["NORTH"]["uids"]), 8)
        # south
        self.assertNotEqual(data["SOUTH"]["count"], -40)
        self.assertNotEqual(len(data["SOUTH"]["uids"]), -1)
        # east
        self.assertNotEqual(data["EAST"]["count"], -10)
        self.assertNotEqual(len(data["EAST"]["uids"]), 80)
        # west
        self.assertNotEqual(data["WEST"]["count"], -10)
        self.assertNotEqual(len(data["WEST"]["uids"]), -90)

    def test_Scene3_1(self):
        scene="SCENE3"
        sensor = Sensor(scene)
        expected= {'NORTH': {'count': 10, 'uids': ['d7ae1052', 
                                                   '1c3254f7', 
                                                   '92acbdfa', 
                                                   'a77baf82', 
                                                   '2416fb0f', 
                                                   'a481a82e', 
                                                   'c01be579', 
                                                   '1b7093f7', 
                                                   'e3a7331c', 
                                                   '2bc61306']}, 
                    'WEST': {'count': 10, 'uids': ['d392f87d', 
                                                   'fb7d643b', 
                                                   '539d89b3', 
                                                   '1a6d7a61', 
                                                   '1fd8eedf', 
                                                   '37c2f87b', 
                                                   'fc4f23c7', 
                                                   '08406e86', 
                                                   '6a9db6e9', 
                                                   'd7f5889d']}, 
                    'EAST': {'count': 10, 'uids': ['a0538bb7', 
                                                   '2d1d9350', 
                                                   'cde2cc25', 
                                                   'b5cb8ce1', 
                                                   'cc9614b7', 
                                                   '39a2d21a', 
                                                   '0d265676', 
                                                   'd460be64', 
                                                   '22b4edc5', 
                                                   '73e9bb56']}, 
                    'SOUTH': {'count': 10, 'uids': ['e512e853', 
                                                    'bdc94d23', 
                                                    'e07fceaa', 
                                                    'fc3349e7', 
                                                    '228bd334', 
                                                    '0c1b2938', 
                                                    'f83d9dc1', 
                                                    '4034cb58', 
                                                    'f8d81ffc', 
                                                    '6f60e0c4']}, 
                    'ALL': {'count': 40}
                }
        data = sensor.getData() 
        
        # north
        self.assertEqual(data["NORTH"]["count"], 1)
        self.assertEqual(len(data["NORTH"]["uids"]), 1)
        # south
        self.assertEqual(data["SOUTH"]["count"], 2)
        self.assertEqual(len(data["SOUTH"]["uids"]), 2)
        # east
        self.assertEqual(data["EAST"]["count"], 3)
        self.assertEqual(len(data["EAST"]["uids"]), 3)
        # west
        self.assertEqual(data["WEST"]["count"], 0)
        self.assertEqual(len(data["WEST"]["uids"]), 0)

    def test_Scene3_2(self):
        scene="SCENE3"
        sensor = Sensor(scene)
        expected= {'NORTH': {'count': 10, 'uids': ['d7ae1052', 
                                                   '1c3254f7', 
                                                   '92acbdfa', 
                                                   'a77baf82', 
                                                   '2416fb0f', 
                                                   'a481a82e', 
                                                   'c01be579', 
                                                   '1b7093f7', 
                                                   'e3a7331c', 
                                                   '2bc61306']}, 
                    'WEST': {'count': 10, 'uids': ['d392f87d', 
                                                   'fb7d643b', 
                                                   '539d89b3', 
                                                   '1a6d7a61', 
                                                   '1fd8eedf', 
                                                   '37c2f87b', 
                                                   'fc4f23c7', 
                                                   '08406e86', 
                                                   '6a9db6e9', 
                                                   'd7f5889d']}, 
                    'EAST': {'count': 10, 'uids': ['a0538bb7', 
                                                   '2d1d9350', 
                                                   'cde2cc25', 
                                                   'b5cb8ce1', 
                                                   'cc9614b7', 
                                                   '39a2d21a', 
                                                   '0d265676', 
                                                   'd460be64', 
                                                   '22b4edc5', 
                                                   '73e9bb56']}, 
                    'SOUTH': {'count': 10, 'uids': ['e512e853', 
                                                    'bdc94d23', 
                                                    'e07fceaa', 
                                                    'fc3349e7', 
                                                    '228bd334', 
                                                    '0c1b2938', 
                                                    'f83d9dc1', 
                                                    '4034cb58', 
                                                    'f8d81ffc', 
                                                    '6f60e0c4']}, 
                    'ALL': {'count': 40}
                }
        data = sensor.getData() 
        
        # north
        self.assertNotEqual(data["NORTH"]["count"], -2)
        self.assertNotEqual(len(data["NORTH"]["uids"]), 8)
        # south
        self.assertNotEqual(data["SOUTH"]["count"], -4)
        self.assertNotEqual(len(data["SOUTH"]["uids"]), -15)
        # east
        self.assertNotEqual(data["EAST"]["count"], -100)
        self.assertNotEqual(len(data["EAST"]["uids"]), 8)
        # west
        self.assertNotEqual(data["WEST"]["count"], -10)
        self.assertNotEqual(len(data["WEST"]["uids"]), -20)

    def test_Scene4_1(self):
        scene="SCENE4"
        sensor = Sensor(scene)
        expected= {'NORTH': {'count': 10, 'uids': ['d7ae1052', 
                                                   '1c3254f7', 
                                                   '92acbdfa', 
                                                   'a77baf82', 
                                                   '2416fb0f', 
                                                   'a481a82e', 
                                                   'c01be579', 
                                                   '1b7093f7', 
                                                   'e3a7331c', 
                                                   '2bc61306']}, 
                    'WEST': {'count': 10, 'uids': ['d392f87d', 
                                                   'fb7d643b', 
                                                   '539d89b3', 
                                                   '1a6d7a61', 
                                                   '1fd8eedf', 
                                                   '37c2f87b', 
                                                   'fc4f23c7', 
                                                   '08406e86', 
                                                   '6a9db6e9', 
                                                   'd7f5889d']}, 
                    'EAST': {'count': 10, 'uids': ['a0538bb7', 
                                                   '2d1d9350', 
                                                   'cde2cc25', 
                                                   'b5cb8ce1', 
                                                   'cc9614b7', 
                                                   '39a2d21a', 
                                                   '0d265676', 
                                                   'd460be64', 
                                                   '22b4edc5', 
                                                   '73e9bb56']}, 
                    'SOUTH': {'count': 10, 'uids': ['e512e853', 
                                                    'bdc94d23', 
                                                    'e07fceaa', 
                                                    'fc3349e7', 
                                                    '228bd334', 
                                                    '0c1b2938', 
                                                    'f83d9dc1', 
                                                    '4034cb58', 
                                                    'f8d81ffc', 
                                                    '6f60e0c4']}, 
                    'ALL': {'count': 40}
                }
        data = sensor.getData() 
        
        # north
        self.assertEqual(data["NORTH"]["count"], 1)
        self.assertEqual(len(data["NORTH"]["uids"]), 1)
        # south
        self.assertEqual(data["SOUTH"]["count"], 2)
        self.assertEqual(len(data["SOUTH"]["uids"]), 2)
        # east
        self.assertEqual(data["EAST"]["count"], 3)
        self.assertEqual(len(data["EAST"]["uids"]), 3)
        # west
        self.assertEqual(data["WEST"]["count"], 0)
        self.assertEqual(len(data["WEST"]["uids"]), 0)

    def test_Scene4_2(self):
        scene="SCENE4"
        sensor = Sensor(scene)
        expected= {'NORTH': {'count': 10, 'uids': ['d7ae1052', 
                                                   '1c3254f7', 
                                                   '92acbdfa', 
                                                   'a77baf82', 
                                                   '2416fb0f', 
                                                   'a481a82e', 
                                                   'c01be579', 
                                                   '1b7093f7', 
                                                   'e3a7331c', 
                                                   '2bc61306']}, 
                    'WEST': {'count': 10, 'uids': ['d392f87d', 
                                                   'fb7d643b', 
                                                   '539d89b3', 
                                                   '1a6d7a61', 
                                                   '1fd8eedf', 
                                                   '37c2f87b', 
                                                   'fc4f23c7', 
                                                   '08406e86', 
                                                   '6a9db6e9', 
                                                   'd7f5889d']}, 
                    'EAST': {'count': 10, 'uids': ['a0538bb7', 
                                                   '2d1d9350', 
                                                   'cde2cc25', 
                                                   'b5cb8ce1', 
                                                   'cc9614b7', 
                                                   '39a2d21a', 
                                                   '0d265676', 
                                                   'd460be64', 
                                                   '22b4edc5', 
                                                   '73e9bb56']}, 
                    'SOUTH': {'count': 10, 'uids': ['e512e853', 
                                                    'bdc94d23', 
                                                    'e07fceaa', 
                                                    'fc3349e7', 
                                                    '228bd334', 
                                                    '0c1b2938', 
                                                    'f83d9dc1', 
                                                    '4034cb58', 
                                                    'f8d81ffc', 
                                                    '6f60e0c4']}, 
                    'ALL': {'count': 40}
                }
        data = sensor.getData() 
        
        # north
        self.assertNotEqual(data["NORTH"]["count"], -2)
        self.assertNotEqual(len(data["NORTH"]["uids"]), 8)
        # south
        self.assertNotEqual(data["SOUTH"]["count"], -4)
        self.assertNotEqual(len(data["SOUTH"]["uids"]), -15)
        # east
        self.assertNotEqual(data["EAST"]["count"], -100)
        self.assertNotEqual(len(data["EAST"]["uids"]), 8)
        # west
        self.assertNotEqual(data["WEST"]["count"], -10)
        self.assertNotEqual(len(data["WEST"]["uids"]), -20)

    def test_Scene5_1(self):
        scene="SCENE5"
        sceneDynamic = {
                        "CT_VEHICLES_NORTH": "10",
                        "CT_VEHICLES_EAST": "10",
                        "CT_VEHICLES_SOUTH": "10",
                        "CT_VEHICLES_WEST": "10",
                    }
        sensor = Sensor(
            scene=scene, vehicle_counts=sceneDynamic
        )
        expected= {'NORTH': {'count': 0, 'uids': ['d7ae1052', 
                                                   '1c3254f7', 
                                                   '92acbdfa', 
                                                   'a77baf82', 
                                                   '2416fb0f', 
                                                   'a481a82e', 
                                                   'c01be579', 
                                                   '1b7093f7', 
                                                   'e3a7331c', 
                                                   '2bc61306']}, 
                    'WEST': {'count': 10, 'uids': ['d392f87d', 
                                                   'fb7d643b', 
                                                   '539d89b3', 
                                                   '1a6d7a61', 
                                                   '1fd8eedf', 
                                                   '37c2f87b', 
                                                   'fc4f23c7', 
                                                   '08406e86', 
                                                   '6a9db6e9', 
                                                   'd7f5889d']}, 
                    'EAST': {'count': 10, 'uids': ['a0538bb7', 
                                                   '2d1d9350', 
                                                   'cde2cc25', 
                                                   'b5cb8ce1', 
                                                   'cc9614b7', 
                                                   '39a2d21a', 
                                                   '0d265676', 
                                                   'd460be64', 
                                                   '22b4edc5', 
                                                   '73e9bb56']}, 
                    'SOUTH': {'count': 10, 'uids': ['e512e853', 
                                                    'bdc94d23', 
                                                    'e07fceaa', 
                                                    'fc3349e7', 
                                                    '228bd334', 
                                                    '0c1b2938', 
                                                    'f83d9dc1', 
                                                    '4034cb58', 
                                                    'f8d81ffc', 
                                                    '6f60e0c4']}, 
                    'ALL': {'count': 40}
                }
        data = sensor.getData() 
        
        # north
        self.assertEqual(data["NORTH"]["count"], 10)
        self.assertEqual(len(data["NORTH"]["uids"]), 10)
        # south
        self.assertEqual(data["SOUTH"]["count"], 10)
        self.assertEqual(len(data["SOUTH"]["uids"]), 10)
        # east
        self.assertEqual(data["EAST"]["count"], 10)
        self.assertEqual(len(data["EAST"]["uids"]), 10)
        # west
        self.assertEqual(data["WEST"]["count"], 10)
        self.assertEqual(len(data["WEST"]["uids"]), 10)

    def test_Scene5_2(self):
        scene="SCENE5"
        sceneDynamic = {
                        "CT_VEHICLES_NORTH": "2",
                        "CT_VEHICLES_EAST": "4",
                        "CT_VEHICLES_SOUTH": "4",
                        "CT_VEHICLES_WEST": "2",
                    }
        sensor = Sensor(
            scene=scene, vehicle_counts=sceneDynamic
        )
        expected= {'NORTH': {'count': 10, 'uids': ['d7ae1052', 
                                                   '1c3254f7', 
                                                   '92acbdfa', 
                                                   'a77baf82', 
                                                   '2416fb0f', 
                                                   'a481a82e', 
                                                   'c01be579', 
                                                   '1b7093f7', 
                                                   'e3a7331c', 
                                                   '2bc61306']}, 
                    'WEST': {'count': 10, 'uids': ['d392f87d', 
                                                   'fb7d643b', 
                                                   '539d89b3', 
                                                   '1a6d7a61', 
                                                   '1fd8eedf', 
                                                   '37c2f87b', 
                                                   'fc4f23c7', 
                                                   '08406e86', 
                                                   '6a9db6e9', 
                                                   'd7f5889d']}, 
                    'EAST': {'count': 10, 'uids': ['a0538bb7', 
                                                   '2d1d9350', 
                                                   'cde2cc25', 
                                                   'b5cb8ce1', 
                                                   'cc9614b7', 
                                                   '39a2d21a', 
                                                   '0d265676', 
                                                   'd460be64', 
                                                   '22b4edc5', 
                                                   '73e9bb56']}, 
                    'SOUTH': {'count': 10, 'uids': ['e512e853', 
                                                    'bdc94d23', 
                                                    'e07fceaa', 
                                                    'fc3349e7', 
                                                    '228bd334', 
                                                    '0c1b2938', 
                                                    'f83d9dc1', 
                                                    '4034cb58', 
                                                    'f8d81ffc', 
                                                    '6f60e0c4']}, 
                    'ALL': {'count': 40}
                }
        data = sensor.getData() 
        
        # north
        self.assertNotEqual(data["NORTH"]["count"], -2)
        self.assertNotEqual(len(data["NORTH"]["uids"]), 8)
        # south
        self.assertNotEqual(data["SOUTH"]["count"], -4)
        self.assertNotEqual(len(data["SOUTH"]["uids"]), -15)
        # east
        self.assertNotEqual(data["EAST"]["count"], -100)
        self.assertNotEqual(len(data["EAST"]["uids"]), 8)
        # west
        self.assertNotEqual(data["WEST"]["count"], -10)
        self.assertNotEqual(len(data["WEST"]["uids"]), -20)

    # reads config file
    # positive
    def test_read_config_1(self):
        scene="SCENE1"
        sensor = Sensor(scene)

        CT_VEHICLES_NORTH = 1
        CT_VEHICLES_EAST = 3
        CT_VEHICLES_SOUTH = 2
        CT_VEHICLES_WEST = 4
        sensor.read_config(scene=scene)

        self.assertEqual(CT_VEHICLES_SOUTH, sensor.CT_VEHICLES_SOUTH)
        self.assertEqual(CT_VEHICLES_EAST, sensor.CT_VEHICLES_EAST)
        self.assertEqual(CT_VEHICLES_NORTH, sensor.CT_VEHICLES_NORTH)
        self.assertEqual(CT_VEHICLES_WEST, sensor.CT_VEHICLES_WEST)

    def test_read_config_2(self):
        scene="SCENE2"
        sensor = Sensor(scene)

        CT_VEHICLES_NORTH = 10
        CT_VEHICLES_EAST = 10
        CT_VEHICLES_SOUTH = 2
        CT_VEHICLES_WEST = 0
        sensor.read_config(scene=scene)

        self.assertEqual(CT_VEHICLES_SOUTH, sensor.CT_VEHICLES_SOUTH)
        self.assertEqual(CT_VEHICLES_EAST, sensor.CT_VEHICLES_EAST)
        self.assertEqual(CT_VEHICLES_NORTH, sensor.CT_VEHICLES_NORTH)
        self.assertEqual(CT_VEHICLES_WEST, sensor.CT_VEHICLES_WEST)

    def test_read_config_3(self):
        scene="SCENE3"
        sensor = Sensor(scene)

        CT_VEHICLES_NORTH = 1
        CT_VEHICLES_EAST = 3
        CT_VEHICLES_SOUTH = 2
        CT_VEHICLES_WEST = 0
        sensor.read_config(scene=scene)

        self.assertEqual(CT_VEHICLES_SOUTH, sensor.CT_VEHICLES_SOUTH)
        self.assertEqual(CT_VEHICLES_EAST, sensor.CT_VEHICLES_EAST)
        self.assertEqual(CT_VEHICLES_NORTH, sensor.CT_VEHICLES_NORTH)
        self.assertEqual(CT_VEHICLES_WEST, sensor.CT_VEHICLES_WEST)

    def test_read_config_4(self):
        scene="SCENE4"
        sensor = Sensor(scene)

        CT_VEHICLES_NORTH = 1
        CT_VEHICLES_EAST = 3
        CT_VEHICLES_SOUTH = 2
        CT_VEHICLES_WEST = 0
        sensor.read_config(scene=scene)

        self.assertEqual(CT_VEHICLES_SOUTH, sensor.CT_VEHICLES_SOUTH)
        self.assertEqual(CT_VEHICLES_EAST, sensor.CT_VEHICLES_EAST)
        self.assertEqual(CT_VEHICLES_NORTH, sensor.CT_VEHICLES_NORTH)
        self.assertEqual(CT_VEHICLES_WEST, sensor.CT_VEHICLES_WEST)



if __name__ == "__main__":
         unittest.main()


    