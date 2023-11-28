import configparser
from sensor import Sensor

# globals
defaults_config = None


# calculate green time for each side
def calculate_times(data):
    #
    all_vehicles = data.get("ALL", 0).get("count", 0)
    calculate_lane_time = lambda vehicles_count, dir_vehicles_count, multiplier: round(
        ((dir_vehicles_count / vehicles_count))
        * data.get("ALL").get("count")
        * multiplier
    )
    timers = {
        "NORTH_TIME": calculate_lane_time(
            all_vehicles, data.get("NORTH").get("count"), 2
        ),
        "SOUTH_TIME": calculate_lane_time(
            all_vehicles, data.get("SOUTH").get("count"), 2
        ),
        "EAST_TIME": calculate_lane_time(
            all_vehicles, data.get("EAST").get("count"), 2
        ),
        "WEST_TIME": calculate_lane_time(
            all_vehicles, data.get("WEST").get("count"), 2
        ),
    }

    return timers


def prioritize_lanes(times):
    # print([key for key, val in (sorted(times.items(), key=lambda vals: vals[1]))])
    return [key for key, val in (sorted(times.items(), key=lambda vals: vals[1]))]


if __name__ == "__main__":
    # defaults
    defaults_config = configparser.ConfigParser()
    defaults_config.read("./config/defaults.config")
    defaults_config = defaults_config["DEFAULTS"]

    # Initialize sensor object
    # sensor = Sensor("SCENE1")
    # sensor = Sensor()
    # # get data
    # data = sensor.getData()
    # print(data)

    # timers = calculate_times(data)
    # print(timers)

    from simulate import Simulate

    sim = Simulate()
    sim.start()
