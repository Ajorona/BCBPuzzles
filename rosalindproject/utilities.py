import os, time

class Menu():
    def __init__(self, options):
        self.options = options
        self.range = len(options)

    def run(self):
        Menu.display(self.options)
        return Menu.getInput(self.range)

    @staticmethod
    def display(options):
        print("Rosalind Project Algorithm CLI")
        print("Enter [Number] to invoke [Option]")
        for index, option in enumerate(options):
            print("{}: {}".format((index+1), option))

    @staticmethod
    def clearScreen():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def pause():
        time.sleep(0.2)

    @staticmethod
    def getInput(inputRange):
        while True:
            userInput = input(">> ")
            try:
                userInput = int(userInput)
                if userInput-1 in range(inputRange):
                    return userInput
            except ValueError:
                print("Invalid Option. Try Again.")

if __name__ == "__main__":
    menu = Menu(['A', 'B', 'C', 'D', 'E'])
    userInput = menu.run()
    print(userInput)
