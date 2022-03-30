class Menu:
    def __init__(self, menu: dict):
        self.menu = menu

    def printMenu(self):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        for i in self.menu:
            print(f"{i}. {self.menu[i]}")
        print("0. Exit")

    def getResponse(self, feedBack):
        while True:
            try:
                self.response = int(input(f"{feedBack}"))
                if self.response <= len(self.menu) and self.response >= 0:
                    return self.response
                else:
                    print("That is not an accepted answer, try again:", end=" ")
            except:
                print("Only Int values are accepted for menus. Try again!", end=" ")