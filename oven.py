import time
from Food.Cake import HomeMadeCake, Print


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
                temperature_type = int(input("Set temperature unit to 1. Celsius, 2. Fahrenheit, 3. Kelvin"))

                if temperature_type == 1 or temperature_type == 2 or temperature_type == 3:
                    break
                else:
                    print("Please select a valid unit of temperature.")

            except ValueError:
                print("Please select from the options above")

        while True:
            try:
                if temperature_type == 1:
                    self.temperature = int(input("Set temperature here(in °C) 0°C - 250°C: "))


            except ValueError:
                print("Please select from the options above")

        Print(f"You have now successfully set the temperature of the oven to {self.temperature}°C")


if __name__ == '__main__':
    startBaking = Oven()
    startBaking.startMix()
