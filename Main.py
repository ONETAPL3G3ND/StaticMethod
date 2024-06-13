#https://github.com/ONETAPL3G3ND
class Tools:
    def __init__(self, name):
        self.name = name

    def Use(self):
        print(f"You are using {self.name}")

    @staticmethod
    def take_in_hand():
        print("You picked up the instrument")

if __name__ == "__main__":
    shovel = Tools("shovel")

    Tools.take_in_hand()
    shovel.Use() #Tools.Use() Error
