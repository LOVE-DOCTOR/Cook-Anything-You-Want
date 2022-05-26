import time
from Food.Cake import HomeMadeCake, Print


def setTempToCelsius(temperature_type: int) -> float:
    if temperature_type == 2:
        temperature = int(input("Set temperature here(in °F) 32°F - 482°C: "))
        convertToCelsius = (temperature - 32) * (5 / 9)
        return convertToCelsius

    elif temperature_type == 3:
        temperature = int or float(input("Set temperature here(in °K) 273.15°K - 523.15°K: "))
        convertToCelsius = temperature + 273.15
        return convertToCelsius


class Oven:

    def __init__(self, temperature: int = 0, timer: int = 0, state: bool = False):
        """
        This function initializes the class with the default values of temperature, timer, and state.

        :param temperature: The temperature of the oven, defaults to 0 (optional)
        :param timer: The amount of time the oven should be on for, defaults to 0 (optional)
        :param state: True or False, defaults to False (optional)
        """
        self.temperature = temperature
        self.timer = timer
        self.state = state

    def putOvenOn(self) -> bool:
        # Asking the user if they want to put on the oven.
        selectState = ["y", "n"]
        print("Do you want to put on the oven? y/n")
        while True:
            switchState = input("Here: ").lower()
            if switchState == "y":
                self.state = True
                Print("Starting oven...")
                Print("Oven is now on")
                break
            # It's setting the state to the current state.
            elif switchState == "n":
                self.state = self.state
                print("Come back when you have something to bake.")
                break

            elif switchState not in selectState:
                print("Select y/n")

        return self.state

    def bakeAtCelsius(self, type_: float = 0, tt=0):
        while True:
            try:
                if tt == 0 and type_ == 0:
                    self.temperature = int(input("Set temperature here(in °C) 0°C - 250°C: "))
                    if self.temperature < 0 or self.temperature > 250:
                        print("You can only set a temperature in the given range.")
                    else:
                        break
                elif tt == 2 or tt == 3:
                    self.temperature = type_
                    if self.temperature < 0 or self.temperature > 250:
                        print("You can only set a temperature in the given range.")
                    else:
                        break

            except ValueError:
                print("Please type in only integer values.")

        Print("Set the timer for the duration you want to bake for.")

        while True:
            try:
                self.timer = int(input("Set the timer(in minutes): "))
                break
            except ValueError:
                print("Please type in only integer values.")
        print("")

        Print(f"Temperature set to {self.temperature}°C")
        Print(f"Timer set to {self.timer}")
        Print("Final mixture is poured into a container of the desired shape.")
        Print("Placing the container into the oven.")
        Print("Baking...")
        Print("Please wait!")
        time.sleep(60)

        if self.temperature == 180 and (self.timer == 30 or self.timer == 35):
            Print("Ping!")
            Print("Your Homemade cake is now ready.")
            Print("Great job, Baker.")

        elif self.temperature > 180 and (self.timer > 35):
            Print("Ping!")
            Print("You must have left your cake for too long in the oven or set a temperature too hot.")
            Print("Your burnt homemade cake is now ready.")

        elif self.temperature < 180 and self.timer == 30 or 35:
            Print("Ping!")
            Print("Your cake is not well baked, you must have set a temperature too low for the time specified.")
            Print("Here is your cake.")

        else:
            Print("Ping!")
            Print("You have not made your best cake yet and you have a long way to go.")
            Print("Have your cake anyways.")

    def startMix(self) -> int:
        Print("What do you want to bake?")
        while True:
            try:
                Print("1. Cake")
                foodToBake = int(input("Here: "))
                break
            except ValueError:
                Print("Please select from the options you're given.")

        if foodToBake == 1:
            Print("What kind of cake would you like to bake?")
            Print("1. Homemade Cake")
            cakeType = int(input("Here: "))
            if cakeType == 1:
                cake = HomeMadeCake()
                cake.mixIngredients()
                state = self.putOvenOn()
                if state is False:
                    print("Oven is not on.")
                    time.sleep(1)
                    print("Sleeping...")
                else:
                    pass
            return cakeType
        else:
            print("Option not available yet")

    def startBaking(self) -> None:
        Print("To start baking, you have to set the desired temperature of the oven")
        Print("Remember to set an optimal temperature to avoid under-baking or burning your food.")

        while True:
            try:
                temperature_type = int(input("Set temperature unit to 1. Celsius, 2. Fahrenheit, 3. Kelvin: "))

                if temperature_type == 1 or temperature_type == 2 or temperature_type == 3:
                    break
                else:
                    print("Please select a valid unit of temperature.")

            except ValueError:
                print("Please select from the options above")

        if temperature_type == 1:
            self.bakeAtCelsius()
        elif temperature_type == 2:
            tt_type = 2
            type__ = setTempToCelsius(2)
            self.bakeAtCelsius(type__, tt_type)
        elif temperature_type == 3:
            tt_type = 3
            type__ = setTempToCelsius(3)
            self.bakeAtCelsius(type__, tt_type)


if __name__ == '__main__':
    startBake = Oven()
    startBake.startMix()
    startBake.startBaking()
