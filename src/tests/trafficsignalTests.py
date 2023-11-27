import unittest
from trafficSignal import TrafficSignal

class Testtrafficsignal(unittest.TestCase):

    # checking signal timer valuess
    #positive
    def test_init_test_1(self):
       
        red=10
        yellow=0
        green=0

        trafficsignal = TrafficSignal(red=red,yellow=yellow,green=green)

        self.assertTrue(type(trafficsignal.red)==int)
        self.assertTrue(type(trafficsignal.yellow)==int)
        self.assertTrue(type(trafficsignal.green)==int)

    #Negative
    def test_init_test_2(self):
       
        red=10
        yellow=10
        green=6

        trafficsignal = TrafficSignal(red=red,yellow=yellow,green=green)

        self.assertFalse(type(trafficsignal.red)==type(""))
        self.assertFalse(type(trafficsignal.yellow)==type(""))
        self.assertFalse(type(trafficsignal.green)==type(""))

    # checking signal timer text
    #positive
    def test_text_1(self):
       
        red=10
        yellow=0
        green=0

        trafficsignal = TrafficSignal(red=red,yellow=yellow,green=green)
        self.assertEqual("", trafficsignal.signalText)

        text = "---"
        trafficsignal.signalText = text
        self.assertEqual(text, trafficsignal.signalText)

    #Negative
    def test_text_2(self):
       
        red=10
        yellow=10
        green=6

        trafficsignal = TrafficSignal(red=red,yellow=yellow,green=green)
        self.assertNotEqual("---", trafficsignal.signalText)

        text = "---"
        trafficsignal.signalText = text
        self.assertNotEqual("text", trafficsignal.signalText)