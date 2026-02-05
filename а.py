class PowerControl:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False


class BrightnessControl:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.brightness = 50

    def set_brightness(self, b):
        self.brightness = max(0, min(100, b))


class TemperatureControl:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.temperature = 22

    def set_temperature(self, t):
        self.temperature = max(-50, min(100, t))


class VoiceControl:
    def voice_command(self, cmd):
        if "включи" in cmd:
            self.turn_on()
        elif "выключи" in cmd:
            self.turn_off()


class SmartLamp(PowerControl, BrightnessControl):
    def __init__(self, name):
        self.name = name
        super().__init__()

    def get_status(self):
        if self.is_on:
            return f"Лампа '{self.name}': включена, яркость {self.brightness}%"
        return f"Лампа '{self.name}': выключена"


class SmartThermostat(PowerControl, TemperatureControl):
    def __init__(self, name):
        self.name = name
        super().__init__()

    def get_status(self):
        if self.is_on:
            return f"Термостат '{self.name}': включен, температура {self.temperature}°C"
        return f"Термостат '{self.name}': выключен"


class SmartAC(PowerControl, BrightnessControl, TemperatureControl, VoiceControl):
    def __init__(self, name):
        self.name = name
        super().__init__()

    def get_status(self):
        if self.is_on:
            return f"Кондиционер '{self.name}': включен, {self.temperature}°C, яркость {self.brightness}%"
        return f"Кондиционер '{self.name}': выключен"