class Auto(object):

    def __init__(self, brand, max_speed):
        self.brand = brand
        self.max_speed = max_speed
        self.speed = 0
        self.engine = False

    def start_engine(self):
        self.engine = True
        print("Engine started")

    def stop_engine(self):
        self.engine = False
        print("Engine stopped")

    def speed_up(self, amount):
        if self.engine:
            self.speed = min(self.speed + amount, self.max_speed)
            print(f"Your speed is {self.speed}")
        else:
            print("Start engine")

    def slow_down(self, amount):
        if self.engine:
            self.speed = max(self.speed - amount, 0)
            print(f"Your speed is {self.speed}")
        else:
            print("Start engine")


class Van(Auto):
    def __init__(self, brand, max_speed, seats):
        super().__init__(brand, max_speed)
        self.seats = seats


bmw = Van("e36", 190, 8)
toyota = Auto("auris", 290)

bmw.speed_up(20)
bmw.start_engine()
bmw.speed_up(30)
bmw.speed_up(300)
bmw.slow_down(20)
