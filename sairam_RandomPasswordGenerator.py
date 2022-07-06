import random

class randomPassGen:
    
    def __init__(self):
        self.passw = ""
    
    def createPass(self, length):
        if length < 6:
            print()
            print("enter length of pass greater than 5")
            print()
            return
        if length < 1:
            print()
            print("enter a positive number")
            print()
            return
        return self.generatePass(length)
    
    def generatePass(self, length):
        for i in range(length // 6):
            a = random.randint(33, 48)
            b = random.randint(48, 58)
            c = random.randint(58, 65)
            d = random.randint(65, 91)
            e = random.randint(91, 97)
            f = random.randint(97, 123)
            self.passw += chr(d)
            self.passw += chr(b)
            self.passw += chr(c)
            self.passw += chr(a)
            self.passw += chr(e)
            self.passw += chr(f)
        for i in range(length - (len(self.passw))):
            self.passw += chr(random.randint(33, 123))
        return self.passw
passw = randomPassGen()
print()
print("-----random password generator-----")
while True:
    inpu = input("1 -> ask a random pass\n2 -> exit\n")
    if inpu == "1":
        try:
            inp = int(input("enter a length of pass -> "))
        except Exception:
            print("enter an integer of length greater than 5")
            break
        print(passw.createPass(inp))
    elif inpu == "2":
        break
    else:
        print("enter a proper choice")
