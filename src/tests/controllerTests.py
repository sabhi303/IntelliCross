import unittest

from controller import *


class ControllerTests(unittest.TestCase):

    # equal vehicles in all directions
    def test_calcculate_times_1(self):
        data = {
            "NORTH": {
                "count": 10,
                "uids": [
                    "f2fdb1b3",
                    "e89ff94c",
                    "f9643102",
                    "22047611",
                    "6a732dbd",
                    "808c194a",
                    "a2aa831c",
                    "a3b6c716",
                    "91624d07",
                    "425885d2",
                ],
            },
            "WEST": {
                "count": 10,
                "uids": [
                    "b7ed1d34",
                    "bdef26d7",
                    "38f27b19",
                    "a0ad5c67",
                    "7debbf50",
                    "8d1a4e73",
                    "a9f899ca",
                    "7cd5ade7",
                    "7023c9f9",
                    "63700586",
                ],
            },
            "EAST": {
                "count": 10,
                "uids": [
                    "86f36bd7",
                    "cf02077a",
                    "62e0a531",
                    "46ccb4f3",
                    "0bfa2d0f",
                    "0a8f129b",
                    "093c1245",
                    "0a3130a6",
                    "8550b5e0",
                    "8bf4af4e",
                ],
            },
            "SOUTH": {
                "count": 10,
                "uids": [
                    "cbd4ae0c",
                    "81d72d37",
                    "383efbaa",
                    "3c28859d",
                    "56cef0f9",
                    "e1d5ecd9",
                    "af384afe",
                    "2f1adb66",
                    "7aa7f942",
                    "2116e893",
                ],
            },
            "ALL": {"count": 40},
        }

        expected = {'NORTH_TIME': 10, 'SOUTH_TIME': 10, 'EAST_TIME': 15, 'WEST_TIME': 15}
        actual = calculate_times(data)
        # -------
        self.assertEqual(expected, actual)
        

    def test_isupper(self):
        self.assertTrue("FOO".isupper())
        self.assertFalse("Foo".isupper())

    def test_split(self):
        s = "hello world"
        self.assertEqual(s.split(), ["hello", "world"])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == "__main__":
    unittest.main()
