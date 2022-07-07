# student height record system

# driver code
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
            print(i, str(self.record[i]) + "in feets")
            print()
        print("----------")
    def deleteRecord(self, name):
        if name not in self.record:
            print("no record found")
        else:
            del self.record[name]
sr = studentRecord()

print("-----WELCOME-----")
while True:
    print()
    print("please choose from below options")
    print()
    print("1 - add new record\n2 - search record\n3 - view all records\n4 - delete record\n5 - exit")
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
                if inpu < 1 or inpu > 3:
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
            name = input("enter name -> ")
            if len(name) < 1:
                print()
                print("invalid input")
                print()
                break
            if name.isalpha() == False:
                print()
                print("invalid input")
                print()
                break
            sr.deleteRecord(name)
        elif inp == 5:
            break
        else:
            print()
            print("choose an option from the list")
            print()
    except Exception:
        print("invalid input")
        break
