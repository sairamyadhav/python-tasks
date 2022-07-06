class restaurant:
    def __init__(self):
        self.menu = {"main courses":{"grilled fish and potatoes":150, "chicken and rice":100}, "drinks":{"mineral water": 20, "coffee":7, "tea":5}, "starters":{"tomato soup": 10, "chicken soup":20, "crispy corn":30},"salads":{"chicken salad":30, "mutton salad":40}}
        self.items = ["main courses", "drinks", "starters", "salads"]
    def display(self, item_type):
        item = self.items[item_type - 1]
        if item not in self.menu:
            print()
            print("item type not present")
            print()
        else:
            print()
            for i in self.menu[item]:
                print(i, "     " + str(self.menu[item][i]) + "$")
            print()
menu = restaurant()

while True:
    try:
        item_type = int(input("please choose the category you like to order \n (1) main courses \n (2) drinks \n (3) starters \n (4) salads \n (5) exit \n"))
        if item_type == 5:
            break
        menu.display(item_type)
    except Exception:
        print()
        print("invalid input")
        print()
