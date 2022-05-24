import time
from Food.Cake import HomeMadeCake


class Oven:

    def __init__(self, temperature=0, timer=0, state=False):
        self.temperature = temperature
        self.timer = timer
        self.state = state

    def putOvenOn(self):
        selectState = ["y", "n"]
        print("Do you want to put on the oven? y/n")
        while True:
            switchState = input("Here: ").lower()
            if switchState == "y":
                self.state = True
                print("Starting oven...")
                time.sleep(3)
                print("Oven is now on")
                break
            elif switchState == "n":
                self.state = self.state
                print("Come back when you have something to bake.")
                break

            elif switchState not in selectState:
                print("Select y/n")

        return self.state

    def startMix(self):
        state = self.putOvenOn()
        if state is True:
            print("What do you want to bake?")
            while True:
                try:
                    print("1. Cake")
                    foodToBake = int(input("Here: "))
                    break
                except ValueError:
                    print("Please select from the options you're given.")

            if foodToBake == 1:
                print("What kind of cake would you like to bake?")
                print("1. Homemade Cake")
                homemadeCake = int(input("Here: "))
                if homemadeCake == 1:
                    cake = HomeMadeCake()
                    cake.mixIngredients()
            else:
                print("Option not available yet")
        else:
            print("Oven is not on.")
            time.sleep(1)
            print("Sleeping...")


if __name__ == '__main__':
    startBaking = Oven()
    startBaking.startMix()
