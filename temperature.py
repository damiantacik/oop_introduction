class Temperature:
    def __init__(self, temp):
        self.temp_c = temp

    @property
    def temp_c(self):
        return f"{self._temp_c}°C"

    @temp_c.setter
    def temp_c(self, value):
        if value < -273.15:
            raise ValueError(f"Too cold: {value}")
        self._temp_c = value

    @property
    def temp_k(self):
        return f"{self._temp_c + 273.15} K"

    @temp_k.setter
    def temp_k(self, value):
        self.temp_c = value - 273.15

    @property
    def temp_f(self):
        return f"{32 + 9 / 5 * self._temp_c}°F"

    @temp_f.setter
    def temp_f(self, value):
        self.temp_c = 5 / 9 * (value - 32)


t = Temperature(70)
t.temp_k = 0
t.temp_c = 0
t.temp_f = -370
print(t.temp_c)
print(t.temp_f)
print(t.temp_k)
