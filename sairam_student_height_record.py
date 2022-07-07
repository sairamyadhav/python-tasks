# student height record system

class studentRecord:
    def __init__(self):
        self.record = {}
    def addRecord(self, name, height):
        self.record[name] = height
    def searchRecord(self, name):
        if name in self.record:
            print()
            print(name, "is " + str(self.record[name]) + " feet")
            print()
        else:
            print()
            print("record not found")
            print()
    def viewRecords(self):
        if len(self.record) == 0:
            print()
            print("no records found yet")
            print()
            return
        print("----------")
        for i in self.record:
            print(i, self.record[i])
            print()
        print("----------")
sr = studentRecord()

print("-----WELCOME-----")
while True:
    print()
    print("please choose from below options")
    print()
    print("1 - add new record\n2 - search record\n3 - view all records\n4 - exit")
    print()
    try:
        inp = int(input("ENTER -> "))
        if inp == 1:
            name = input("enter name of record -> ")
            if len(name) == 0:
                print("invalid input")
                break
            elif name.isalpha() == False:
                print("invalid input")
                break
            print()
            print("1 - in cms\n2 - in inches\n3 - in feet\n")
            try:
                inpu = int(input("choose -> "))
                if inpu < 1 or height > 3:
                    raise Exception
                height = float(input("enter height -> "))
                if height < 1:
                    raise Exception
                if inpu == 1:
                    height = height * 0.0328084
                elif inpu == 2:
                    height = height * 0.0833333
                elif inpu == 3:
                    height = height
                sr.addRecord(name, height)
            except Exception:
                print("invalid input")
                break
        elif inp == 2:
            name = input("enter name -> ")
            if name.isalpha() == False:
                print("invalid input")
                break
            if len(name) == 0:
                print("invalid input")
                break
            sr.searchRecord(name)
        elif inp == 3:
            sr.viewRecords()
        elif inp == 4:
            break
        else:
            print()
            print("choose an option from the list")
            print()
    except Exception:
        print("invalid input")
        break
