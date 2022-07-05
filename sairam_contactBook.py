import re

class ContactBook:

    # this method initializes contact book    
    def __init__(self):
        self.contactBook = {}
        self.counter = 1

    # this method is to view add new contact to contact book    
    def addContact(self, name, phone, email, address):
        newContact = [name, phone, email, address]
        for i in self.contactBook:
            if self.contactBook[i] == newContact:
                print()
                print("contact with similar details already exists at index position " + str(i))
                print()
                return
        self.contactBook[self.counter] = newContact
        self.counter += 1


    # this method is to view entire contact book    
    def viewContactBook(self):
        if self.contactBook == {}:
            print()
            print("no entries in contact book")
            print()
            return
        for i in self.contactBook:
            print(i, self.contactBook[i])
    def searchBook(self, pos):
        if pos not in self.contactBook:
            print()
            print("no entry at position " + str(pos))
            print()
            return
        print()
        print(self.contactBook[pos])
        print()

def validateName(name):
    if name.isalpha() == False:
        print()
        print("Invalid name, enter a proper string")
        print()
        return 0
    return 1

def validatePhone(phone):
    if phone.isnumeric() == False:
        print()
        print("Invalid phone, enter a proper number")
        print()
        return 0
    return 1

def validateEmail(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.fullmatch(regex, email):
        print()
        print("Invalid email, enter a proper email")
        print()
        return 0
    return 1

def validateAddress(address):
    if type(address) != str:
        print()
        print("Invalid address, enter a proper address")
        print()
        return 0
    return 1

book = ContactBook()
print("-----Welcome to contact book-----")

# --- main ---

while True:
    print("press 1 to enter new contact details")
    print("press 2 to view existing contact details")
    print("press 3 to search contact at particular position")
    print("press exit() to exit contact details")
    print()
    inp = input("enter your choice -> ")
    if inp == "exit()":
        break
    if inp.isnumeric() == False:
        print("enter number in the range 1 - 3")
        continue
    inp = int(inp)
    # if type(inp) != int:
    #     print("Invalid input expected integer in range 1 - 3, given " + str(type(inp)))
    if inp < 1 or inp > 3:
        print("Invalid input expected integer in range 1 - 3, given " + str(type(inp)))
        continue
    else:
        if inp == 1:
            a, b, c, d = 0, 0, 0, 0
            while True:
                print("enter name, phone, email, address in order")
                name = input("enter name of contact -> ")
                a = validateName(name)
                if a == 0:
                    continue
                phone = input("enter phone of contact -> ")
                b = validatePhone(phone)
                if b == 0:
                    continue
                email = input("enter email of contact -> ")
                c = validateEmail(email)
                if c == 0:
                    continue
                address = input("enter address of contact -> ")
                d = validateAddress(address)
                if d == 0:
                    continue
                if a == 1 and b == 1 and c == 1 and d == 1:
                    book.addContact(name, phone, email, address)
                    break
        elif inp == 2:
            book.viewContactBook()
        elif inp == 3:
            pos = int(input("enter position -> "))
            book.searchBook(pos)
