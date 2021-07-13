def construct_car(brand, max_speed):
    return {
        "brand": brand,
        "engine": False,
        "max_speed": max_speed,
        "speed": 0
    }


def start_engine(car):
    car["engine"] = True
    print("Engine started")
    return car


def stop_engine(car):
    car["engine"] = False
    print("Engine stopped")
    return car


def speed_up(car, amount):
    if car["engine"]:
        car["speed"] = min(car["speed"] + amount, car["max_speed"])
        print(f"Your speed is {car['speed']}")
    else:
        print("Start engine")

    return car


def slow_down(car, amount):
    if car["engine"]:
        car["speed"] = max(car["speed"] - amount, 0)
        print(f"Your speed is {car['speed']}")
    else:
        print("Start engine")

    return car


toyota = construct_car('auris', 194)
ford = construct_car('s-max', 240)
start_engine(toyota)
start_engine(ford)
# print(auto)
speed_up(toyota, 20)
speed_up(ford, 50)
# stop_engine(auto)
# speed_up(toyota, 40)
# speed_up(toyota, 500)
# slow_down(toyota, 20)
# slow_down(toyota, 400)
print(toyota)
print(ford)
