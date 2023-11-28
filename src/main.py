import configparser
from sensor import Sensor

# globals
defaults_config = None


# calculate green time for each side
def calculate_times(data):
    #
    all_vehicles = data.get("ALL", 0).get("count", 0)
    calculate_lane_time = lambda vehicles_count, dir_vehicles_count: round(
        (dir_vehicles_count / vehicles_count) * int(defaults_config["MAX_CYCLE"])
    )
    timers = {
        "NORTH_TIME": calculate_lane_time(all_vehicles, data.get("NORTH").get("count")),
        "SOUTH_TIME": calculate_lane_time(all_vehicles, data.get("SOUTH").get("count")),
        "EAST_TIME": calculate_lane_time(all_vehicles, data.get("EAST").get("count")),
        "WEST_TIME": calculate_lane_time(all_vehicles, data.get("WEST").get("count")),
    }

    return timers


def prioritize_lanes(times):
    return [key for key, val in (sorted(times.items(), key=lambda vals: vals[1]))]


if __name__ == "__main__":
    # defaults
    defaults_config = configparser.ConfigParser()
    defaults_config.read("./config/defaults.config")
    defaults_config = defaults_config["DEFAULTS"]

    # Initialize sensor object
    # sensor = Sensor("SCENE1")
    sensor = Sensor()
    # get data
    data = sensor.getData()
    print(data)

    times = calculate_times(data)
    for dir, tim in times.items():
        print(dir, ":", tim)

    print("\nOrder:")
    for dir in prioritize_lanes(times):
        print(dir)
