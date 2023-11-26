class TrafficSignal:
    red: int
    yellow: int
    green: int
    text: str

    def __init__(self, red, yellow, green):
        self.red = red if type(red) == type(0) else int(red)
        self.yellow = yellow if type(yellow) == type(0) else int(yellow)
        self.green = green if type(green) == type(0) else int(green)
        self.signalText = ""
