import unittest

from controller import *


class ControllerTests(unittest.TestCase):
    # calculate times for each direction
    # same traffic in all lanes
    # positive
    def test_calculate_times_1(self):
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

        expected = {
            "NORTH_TIME": 20,
            "SOUTH_TIME": 20,
            "EAST_TIME": 20,
            "WEST_TIME": 20,
        }
        actual = calculate_times(data)
        # -------
        self.assertEqual(expected, actual)

    # negative
    def test_calculate_times_2(self):
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

        expected = {"NORTH_TIME": 8, "SOUTH_TIME": 7, "EAST_TIME": 6, "WEST_TIME": 5}
        actual = calculate_times(data)
        # -------
        self.assertNotEqual(expected, actual)

    # different traffic in all lanes
    # positive
    def test_calculate_times_3(self):
        data = {
            "NORTH": {
                "count": 3,
                "uids": ["f2fdb1b3", "e89ff94c", "f9643102"],
            },
            "WEST": {
                "count": 5,
                "uids": ["b7ed1d34", "bdef26d7", "38f27b19", "a0ad5c67", "7debbf50"],
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
                "count": 8,
                "uids": [
                    "cbd4ae0c",
                    "81d72d37",
                    "383efbaa",
                    "3c28859d",
                    "56cef0f9",
                    "e1d5ecd9",
                    "af384afe",
                    "2f1adb66",
                ],
            },
            "ALL": {"count": 26},
        }

        expected = {
            "NORTH_TIME": 6,
            "SOUTH_TIME": 16,
            "EAST_TIME": 20,
            "WEST_TIME": 10,
        }
        actual = calculate_times(data)
        # -------
        self.assertEqual(expected, actual)

    # negative
    def test_calculate_times_4(self):
        data = {
            "NORTH": {
                "count": 3,
                "uids": ["f2fdb1b3", "e89ff94c", "f9643102"],
            },
            "WEST": {
                "count": 5,
                "uids": ["b7ed1d34", "bdef26d7", "38f27b19", "a0ad5c67", "7debbf50"],
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
                "count": 8,
                "uids": [
                    "cbd4ae0c",
                    "81d72d37",
                    "383efbaa",
                    "3c28859d",
                    "56cef0f9",
                    "e1d5ecd9",
                    "af384afe",
                    "2f1adb66",
                ],
            },
            "ALL": {"count": 26},
        }

        expected = {"NORTH_TIME": 8, "SOUTH_TIME": 7, "EAST_TIME": 6, "WEST_TIME": 5}
        actual = calculate_times(data)
        # -------
        self.assertNotEqual(expected, actual)

    # prioritize lanes according to times
    # different times for lanes
    # positive
    def test_prioritize_lanes_1(self):
        times = {"NORTH_TIME": 10, "SOUTH_TIME": 10, "EAST_TIME": 15, "WEST_TIME": 15}

        actual = prioritize_lanes(times=times)
        expected = ["NORTH_TIME", "SOUTH_TIME", "EAST_TIME", "WEST_TIME"]
        self.assertEqual(expected, actual)

    # negative
    def test_prioritize_lanes_2(self):
        times = {"NORTH_TIME": 10, "SOUTH_TIME": 10, "EAST_TIME": 15, "WEST_TIME": 15}

        actual = prioritize_lanes(times=times)
        expected = ["EAST_TIME", "WEST_TIME", "SOUTH_TIME", "NORTH_TIME"]
        self.assertNotEqual(expected, actual)

    # same times for lanes
    # positive
    def test_prioritize_lanes_3(self):
        times = {"NORTH_TIME": 10, "SOUTH_TIME": 10, "EAST_TIME": 10, "WEST_TIME": 10}

        actual = prioritize_lanes(times=times)
        expected = ["NORTH_TIME", "SOUTH_TIME", "EAST_TIME", "WEST_TIME"]
        self.assertEqual(expected, actual)

    # negative
    def test_prioritize_lanes_4(self):
        times = {"NORTH_TIME": 10, "SOUTH_TIME": 10, "EAST_TIME": 10, "WEST_TIME": 10}

        actual = prioritize_lanes(times=times)
        expected = ["EAST_TIME", "WEST_TIME", "SOUTH_TIME", "NORTH_TIME"]
        self.assertNotEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
