import time
import random


class Cake:
    def __init__(self, tries: int, ingredients=None, home_made_cake=False):
        if ingredients is None:
            ingredients = []
        self.ingredients = ingredients
        self.home_made_cake = home_made_cake
        self.tries = tries
        self.messagesList = ["You are a culinary disaster and should not be allowed near the stove.",
                             "I know you're trying to make a homemade cake, but your recipe is turning into a disaster.",
                             "I don't know who told you to try baking, maybe you'd be better off doing the eating.",
                             "That is one way to ruin a cake.",
                             " If you bake a cake that way, you will end up with something more resembling a muffin."]

        self.messagesList2 = [" Second time's a charm, or so they say. Stay away from the kitchen.",
                              "It's good you have hopes but you've made a mess for the second time in a row, "
                              "I'm afraid we have to let you go."]

        self.successMessage = ["Perfect!", "Great!", "yum-yum", "Delicious"]
        self.numbers = [1, 2, 3, 4]


def Print(message: (str, int, float)) -> None:
    print(message)
    time.sleep(2)


class HomeMadeCake(Cake):
    def __init__(self):
        Cake.__init__(self, 2, ["flour", "egg", "baking soda", "vanilla essence", "powdered sugar", "butter", "milk"],
                      home_made_cake=True)

    def CheckSuccess(self, correct_option):
        while True:
            doFirstStep = int(input("Select 1, 2 or 3: "))
            if doFirstStep in self.numbers:
                if doFirstStep != correct_option:
                    print(random.choice(self.messagesList))
                    self.tries -= 1
                    if self.tries == 0:
                        print(random.choice(self.messagesList2))
                        break
                elif doFirstStep == correct_option:
                    self.tries = 2
                    Print(random.choice(self.successMessage))
                    break
            else:
                print("Option not in steps")

    def listIngredients(self):
        Print("We will be baking our HomeMadeCake with the following ingredients")
        Print(f"1. 3 cups of {self.ingredients[0]}")
        Print(f"2. 4 pieces of {self.ingredients[1]}")
        Print(f"3. 2 teaspoons of {self.ingredients[2]}")
        Print(f"4. 2 teaspoons of {self.ingredients[3]}")
        Print(f"5. 1.5 cups of {self.ingredients[4]}")
        Print(f"6. 1 cup of {self.ingredients[5]}")
        Print(f"7. 1 cup of {self.ingredients[6]}")

    def mixIngredients(self):
        self.listIngredients()

        Print("It's time to mix the ingredients together")
        Print("What do you do in the first step?")
        print("1. Combine flour and egg")
        print("2. Mix the baking soda with vanilla essence")
        print("3. Mix the butter and sugar together")
        self.CheckSuccess(3)

        Print("Mixing sugar and butter together")
        Print("Whisking the mixture")
        Print("Mixture is light and fluffy now")
        Print("What do we do next?")
        print("1. Add baking soda.")
        print("2. Add eggs.")
        print("3. Add milk")
        self.CheckSuccess(2)

        Print("Crack! We break the eggs open into a bowl")
        Print("Beating the eggs")
        Print("Adding the beaten eggs to the butter and sugar mixture")
        Print("Beating the mixture further...")
        Print("Just a little moment")
        Print("Almost there...")
        Print("Mixture is now white and creamy")
        Print("What do we do next?")
        print("1. Put the mixture into the oven")
        print("2. Add a little salt into the mixture and mix again")
        print("3. Mix flour and baking soda together")
        print("4. Pour it away")
        self.CheckSuccess(3)

        Print("Sifting flour and baking soda into another bowl")
        Print("This is done to evenly distribute the baking soda in the flour")
        Print("Adding the flour-soda mixture into the egg mixture.")
        Print("Oh snap! Our batter is not quite soft and fluffy as it should be")
        Print("You should add more milk")
        numOfTimes = 0
        while True:
            addMilk = input("Type 'add' to add milk: ").lower()
            if addMilk != "add":
                print("Not sure what to make of that.")
            elif addMilk == "add":
                numOfTimes += 1
                if numOfTimes == 3:
                    Print("Mixing...")
                    Print("That's perfect! We now have our batter as soft and fluffy as we love it!")
                    break
                elif numOfTimes < 3:
                    Print("Mixing...")
                    print("Not quite there yet! Add more")

        Print("We add vanilla essence to the mixture.")
        Print("Blending it in...")
        Print("This is important to camouflage the smell of the eggs and make the cake taste delicious")
        Print("It is time to bake the cake now")
