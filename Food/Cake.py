import time
import random


# The class Cake has a constructor that takes two arguments, ingredients and home_made_cake.
# The constructor initializes the instance variables ingredients and home_made_cake.
# The instance variable ingredients is initialized to an empty list if no argument is passed to the constructor.
# The instance variable home_made_cake is initialized to False if no argument is passed to the constructor.
# The class also has two instance variables, messagesList and messagesList2, which are initialized to list of strings.
# The class also has an instance variable successMessage, which is initialized to a list of strings.
# The class also has an instance variable numbers, which is initialized to a list of integers.
class Cake:
    def __init__(self, ingredients: any = None) -> None:
        """
        The function __init__ is a constructor that initializes the class Cake with the attributes ingredients,
        home_made_cake, messagesList, messagesList2, successMessage, and numbers

        :param ingredients: a list of ingredients that the player has to use to make the cake
        """

        if ingredients is None:
            ingredients = []
        self.ingredients = ingredients
        self.messagesList = ["You are a culinary disaster and should not be allowed near the stove.",
                             "I know you're trying to make a homemade cake, but your recipe is turning a disaster.",
                             "I don't know who told you to try baking, maybe you'd be better off doing the eating.",
                             "That is one way to ruin a cake.",
                             " If you bake a cake that way, you will end up with something more resembling a muffin."]

        self.messagesList2 = [" Second time's a charm, or so they say. Stay away from the kitchen.",
                              "It's good you have hopes but you've made a mess for the second time in a row, "
                              "I'm afraid we have to let you go."]

        self.successMessage = ["Perfect!", "Great!", "yum-yum", "Delicious"]
        self.numbers = [1, 2, 3, 4]

        # A function that checks if the user has selected the correct option.


def Print(message: any) -> None:
    """
    Prints a message to the screen and waits 2 seconds before continuing

    :param message: The message to be printed
    :type message: any
    """
    print(message)
    time.sleep(0.01)


# We are baking a cake, and we need to follow the instructions to bake it
class HomeMadeCake(Cake):
    def __init__(self):
        """
        The function __init__() is a constructor that initializes the attributes of the class Cake
        """
        Cake.__init__(self, ["flour", "egg", "baking soda", "vanilla essence", "powdered sugar", "butter", "milk"])

    def CheckSuccess(self, correct_option: int) -> None:

        while True:

            try:
                doFirstStep = int(input("Select 1, 2 or 3: "))

                if doFirstStep == correct_option:
                    Print(random.choice(self.successMessage))
                    break

                elif doFirstStep != correct_option:
                    Print(random.choice(self.messagesList))
                    Print("Try again!")

            except ValueError:
                print("Please select from the available options.")

    def listIngredients(self) -> None:
        """
        This function prints out the ingredients of the cake
        """
        Print("We will be baking our HomeMadeCake with the following ingredients")
        Print(f"1. 3 cups of {self.ingredients[0]}")
        Print(f"2. 4 pieces of {self.ingredients[1]}")
        Print(f"3. 2 teaspoons of {self.ingredients[2]}")
        Print(f"4. 2 teaspoons of {self.ingredients[3]}")
        Print(f"5. 1.5 cups of {self.ingredients[4]}")
        Print(f"6. 1 cup of {self.ingredients[5]}")
        Print(f"7. 1 cup of {self.ingredients[6]}")

    def mixIngredients(self) -> None:
        """
        The function mixes the ingredients together and asks the user to choose the correct steps to mix the ingredients
        """
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


class ClassicCupcake(Cake):
    def __init__(self):
        Cake.__init__(self, ["1 3/4 flour(not self-rising)", "1 1/4 cups unbleached all-purpose flour", "2 cups sugar",
                             "1 tbsp. baking powder", "3/4 tsp. salt", "4 sticks unsalted cubed butter", "4 large eggs",
                             "1 cup whole milk", "1 tsp. pure vanilla extract", "6 cups confectioners' sugar",
                             "1/2 cup milk", "2 tsp. vanilla extract"])

    def CheckSuccess(self, correct_option: int) -> None:

        while True:

            try:
                doFirstStep = int(input("Select 1, 2 or 3: "))

                if doFirstStep == correct_option:
                    Print(random.choice(self.successMessage))
                    break

                elif doFirstStep != correct_option:
                    Print(random.choice(self.messagesList))
                    Print("Try again!")

            except ValueError:
                print("Please select from the available options.")

    def listIngredients(self) -> None:
        Print("We will be baking our Classic Cupcake with the following ingredients.")
        Print(self.ingredients[0])
        Print(self.ingredients[1])
        Print(self.ingredients[2])
        Print(self.ingredients[3])
        Print(self.ingredients[4])
        Print(self.ingredients[5])
        Print(self.ingredients[6])
        Print(self.ingredients[7])
        Print(self.ingredients[8])
        Print(self.ingredients[9])
        Print(self.ingredients[10])
        Print(self.ingredients[11])

    def mixIngredients(self) -> None:
        self.listIngredients()

        Print("Lining up cupcake pan with paper liners.")
        Print("Setting pan aside")
        Print("Now that this has been done.")
        Print("What do you do next?")
        print("1. Place the cupcake pan in the oven to preheat it.")
        print("2. Fill the baking cups with milk.")
        print("3. Combine the flour, sugar, baking powder and salt in a bowl.")
        self.CheckSuccess(3)

        Print("Mixing the ingredients together")
        Print("Ingredients are now perfectly mixed")
        Print("What do you do next?")
        print("1. Add the butter to the mixture and then eggs")
        print("2. Add sugar to the mixture and then butter.")
        print("3. Add milk to the mixture and then eggs.")
        self.CheckSuccess(1)

        Print("Adding 4 sticks of unsalted cubed butter to the mixture.")
        Print("Mixing...")
        Print("The butter is now coated with flour")
        Print("Breaking the eggs")
        Print("Adding the eggs to the mixture and mixing thoroughly")
        Print("All the eggs are now fully incorporated into the mixture")
        Print("What do you do next?")
        print("1. Add sugar to the mixture and mix it.")
        print("2. Add milk and vanilla extract to the mixture and mix it.")
        print("3. Add salt to the mixture and mix it.")
        self.CheckSuccess(2)

        Print("Adding 1 cup of milk and 1 teaspoon of vanilla extract to the batter")
        Print("Mixing thoroughly")
        Print("The ingredients are now completely mixed")
        Print("Filling 2/3 of each baking cup with the batter")
        Print("It's time to bake")
