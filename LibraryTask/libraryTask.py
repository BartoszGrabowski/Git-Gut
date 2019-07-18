import csv
class Item:
    def __init__(self, itemId, price, status):
        self.itemId = itemId
        self.price = price
        self.status = status

class Book(Item):
    def __init__(self, author, title, genre, itemId, price,status,  checkedOutBy = "null"):
        Item.__init__(self, itemId, price, status)
        self.author = author
        self.title = title
        self.genre = genre
        self.checkedOutBy = checkedOutBy

    def CheckStatus(self):
        return self.status

    def CheckInBook(self):
        self.status = "Avaiable to check out"
        self.checkedOutBy = "null"
        print("Checked in" + self.title)

    def CheckOutBook(self, checkedOutBy):
        self.status = "checked out"
        self.checkedOutBy = checkedOutBy
        print("Checked out" + self.title)

    def BookUpdate(self, price, author, title, genre):
        self.price = price
        self.author = author
        self.title = title
        self.genre = genre

    def UpdateId(self, itemId):
        self.itemId = itemId




class Newspaper(Item):
    def __init__(self, name, timeOfPublish,  itemId, price, status, checkedOutBy="null"):
        Item.__init__(self, itemId, price, status)
        self.name = name
        self.timeOfPublish = timeOfPublish
        self.checkedOutBy = checkedOutBy


    def CheckStatus(self):
        return self.status

    def CheckInNewspaper(self):
        self.status = "Avaiable to check out"
        self.checkedOutBy = "null"
        print("Checked in" + self.name)

    def CheckOutNewspaper(self, checkedOutBy):
        self.status = "checked out"
        self.checkedOutBy = checkedOutBy
        print("Checked out" + self.name)
    def NewspaperUpdate(self,price,name,timeOfPublish):
        self.price = price
        self.name = name
        self.timeOfPublish = timeOfPublish

    def UpdateId(self, itemId):
        self.itemId = itemId


class GovDocument(Item):
        def __init__(self, createdBy, name, itemId, price, status, isConfidental, checkedOutBy="null"):
            Item.__init__(self, itemId, price, status)
            self.createdBy = createdBy
            self.name = name
            self.isConfidental = isConfidental
            self.checkedOutBy = checkedOutBy

        def CheckStatus(self):
            return self.status

        def CheckInGovDoc(self):
            self.status = "Avaiable to check out"
            self.checkedOutBy = "null"
            print("Checked in" + self.name)

        def CheckOutGovDoc(self, checkedOutBy):
            self.status = "checked out"
            self.checkedOutBy = checkedOutBy
            print("Checked out" + self.name)
        def GovDocUpdate(self,price,createdBy,name,isConfidental):
            self.price = price
            self.createdBy = createdBy
            self.name = name
            self.isConfidental = isConfidental

        def UpdateId(self, itemId):
            self.itemId = itemId

class Client():
    def __init__(self, clientID, cName, cAddress, cPhoneNo):
        self.clientID = clientID
        self.cName = cName
        self.cAddress = cAddress
        self.cPhoneNo = cPhoneNo

    def UpdateClientDetails(self,cName, cAddress, cPhoneNo):
        self.cName = cName
        self.cAddress = cAddress
        self.cPhoneNo = cPhoneNo

    def PuchaseBook(self):
        pass

    def UpdateId(self, clientID):
        self.clientID = clientID

def SaveFunction():
    print("SAVING")
    bookListFile = open("bookList.txt", "w")
    newsPaperFile = open("newspapers.txt", "w")
    govDocFile = open("govDoc.txt", "w")
    clientFile = open("Clients.txt", "w")

    for x in bookList:
        bookListFile.write(str(x.itemId) + "," + str(x.title) + "," + str(x.author) + "," + str(x.genre)  + "," + str(x.price) + "," + str(x.status) + "," + str(x.checkedOutBy) + "\n")

    for x in newspapersList:
        newsPaperFile.write(str(x.itemId) + "," + str(x.timeOfPublish) + "," + str(x.name) + "," + str(x.price)  + "," + str(x.status) + "," + str(x.checkedOutBy) + "\n")

    for x in govdocList:
        govDocFile.write(str(x.itemId) + "," + str(x.createdBy) + "," + str(x.name) + "," + str(x.price) + "," + str(x.status) + "," + str(x.isConfidental) + "," + str(x.checkedOutBy) + "\n")

    for x in customerList:
        clientFile.write(str(x.clientID) + "," + str(x.cName) + "," + str(x.cAddress) + "," + str(x.cPhoneNo) + "\n")

run = True

bookList = []
newspapersList = []
govdocList = []
customerList = []

with open("bookList.txt" , "r") as bookRead:
    reader = csv.reader(bookRead)
    for row in reader:
        bookList.append(Book(row[2], row[1], row[3], row[0], row[4], row[5], row[6]))
    bookRead.close()
with open("newspapers.txt" , "r") as newspaperRead:
    reader = csv.reader(newspaperRead)
    for row in reader:
        newspapersList.append(Newspaper(row[2], row[1], row[0], row[3], row[4], row[5]))
    newspaperRead.close()

with open("govDoc.txt", "r") as govRead:
    reader = csv.reader(govRead)
    for row in reader:
        govdocList.append(GovDocument(row[1],row[2],row[0],row[3],row[4],row[5], row[6]))
    govRead.close()

with open("Clients.txt", "r") as ClientRead:
    reader = csv.reader(ClientRead)
    for row in reader:
        customerList.append(Client(row[0],row[1],row[2],row[3]))
    ClientRead.close()



print("WELCOME TO LIBRARY MANAGER 9000 \n THE BEST LIBRARY MANAGMENT SOFTWARE TO DATE\n INPUT MENU NUMBER TO SELECT")

while run :

    userInput = int(input("Main Menu: \n 1.Check out item \n 2.Check in item\n 3.Add new item\n 4.Remove item\n 5.Update item"
                          " \n 6.Register new customer \n 7.Delete customer data \n 8.Update customer data \n 9.Exit application"))

    if userInput == 1:
        #check out item
        userInput3 = int(input("What item to check out \n 1.book \n 2.newspaper \n 3.government document"))
        if userInput3 == 1:
            checkOutBook = int(input("type in ID of a book to check out\n"))
            CheckOutBookClient = input("type in name of customer checking out book \n")
            bookList[checkOutBook-1].CheckOutBook(CheckOutBookClient)
        elif userInput3 == 2:
            checkOutNewspaper = int(input("type in ID of a newspaper to check out"))
            CheckOutNewspaperClient = input("type in name of customer checking out newspaper \n")
            newspapersList[checkOutNewspaper - 1].CheckOutNewspaper(CheckOutNewspaperClient)
        elif userInput3 == 3:
            checkOutGovDoc = int(input("type in ID of a government document to check out"))
            CheckOutGovDocClient = input("type in name of customer checking out government document \n")
            govdocList[checkOutGovDoc - 1].CheckOutGovDoc(CheckOutGovDocClient)

    elif userInput == 2:
        #check in item
        userInput4 = int(input("What item to check in \n 1.book \n 2.newspaper \n 3.government document"))
        if userInput4 == 1:
            checkInBook = int(input("type in ID of a book to check in\n"))
            bookList[checkInBook-1].CheckInBook()
        elif userInput4 == 2:
            checkInNewspaper = int(input("type in ID of a newspaper to check in"))
            newspapersList[checkInNewspaper - 1].CheckInNewspaper()
        elif userInput4 == 3:
            checkInGovDoc = int(input("type in ID of a government document to check in"))
            govdocList[checkInGovDoc - 1].CheckInGovDoc()
    elif userInput == 3:
        # new item
        userInput2 = int(input("What item to input \n 1.New book \n 2.New newspaper \n 3.New government document"))
        if userInput2 == 1:
            newBookTitle = input("Please enter book title: \n")
            newBookAuthor = input("Please enter book author: \n")
            newBookGenre = input("Please enter book Genre: \n")
            newBookPrice = input("Please enter book price: \n")
            newBookStatus = "Avaiable to check out"
            newBookID = len(bookList) + 1
            bookList.append(Book(newBookAuthor, newBookTitle,newBookGenre,newBookID,newBookPrice, newBookStatus ))
        elif userInput2 == 2:
            newNewspaperName = input("Please enter newspaper name: \n")
            newNewspaperDateOfPublishment = input("Please enter date when newspaper was published: \n")
            newNewspaperPrice = input("Please enter newspaper price: \n")
            newNewspaperStatus = "Avaiable to check out"
            newNewspaperID = len(newspapersList) + 1
            newspapersList.append((Newspaper(newNewspaperName,newNewspaperDateOfPublishment,newNewspaperID, newNewspaperPrice,newNewspaperStatus)))
        elif userInput2 == 3:
            newGovDocOrgin = input("Please enter government documet orgin: \n")
            newGovDocName = input("Please enter government document name: \n")
            newGovDocPrice = input("Please enter document price: \n")
            newGovDocConfidental= input("Type in 1 if document is confidental 2 if not: \n")
            govDocStatus = "Avaiable to check out"
            govDocConfi = False
            govDocID = len(govdocList) + 1
            if newGovDocConfidental == 1: govDocConfi = True
            govdocList.append(GovDocument(newGovDocOrgin,newGovDocName,govDocID,newGovDocPrice,govDocStatus,govDocConfi))
    elif userInput == 4:
        # remove item
        userInput5 = int(input("What item to remove in \n 1.book \n 2.newspaper \n 3.government document"))
        if userInput5 == 1:
            removeBook = int(input("type in ID of a book to delete\n"))
            bookList.pop(removeBook-1)
            for x in range(len(bookList)):
                bookList[x].UpdateId(x+1)
        elif userInput5 == 2:
            removeNewspaper = int(input("type in ID of a newspaper to delete"))
            newspapersList.pop(removeNewspaper-1)
            for x in range(len(newspapersList)):
                newspapersList[x].UpdateId(x+1)
        elif userInput5 == 3:
            removeGovDoc = int(input("type in ID of a government document to delete"))
            govdocList.pop(removeGovDoc-1)
            for x in range(len(govdocList)):
                govdocList[x].UpdateId(x+1)
    elif userInput == 5:
        # update item
        userInput6 = int(input("What item to update in \n 1.book \n 2.newspaper \n 3.government document"))
        if userInput6 == 1:
            updateBook = int(input("type in ID of a book to update\n"))
            print("selected book name: " + str(bookList[updateBook-1].title))
            updateBookTitle = input("Please enter new book title: \n")
            updateBookAuthor = input("Please enter new book author: \n")
            updateBookGenre = input("Please enter new book Genre: \n")
            updateBookPrice = input("Please enter new book price: \n")
            bookList[updateBook-1].BookUpdate(updateBookPrice, updateBookAuthor,updateBookTitle, updateBookGenre,)

        elif userInput6 == 2:
            updateNewspaper = int(input("type in ID of a newspaper to update"))
            print("selected newspaper name: " + str(newspapersList[updateNewspaper-1].name))
            updateNewspaperName = input("Please update newspaper name: \n")
            updateNewspaperDateOfPublishment = input("Please update date when newspaper was published: \n")
            updateNewspaperPrice = input("Please update newspaper price: \n")
            newspapersList[updateNewspaper-1].NewspaperUpdate(updateNewspaperPrice, updateNewspaperName, updateNewspaperDateOfPublishment)


        elif userInput6 == 3:
            updateGovDoc = int(input("type in ID of a government document to update"))
            print("selected Government document name: " + str(govdocList[updateGovDoc-1].name))
            updateGovDocOrgin = input("Please enter government documet orgin: \n")
            updateGovDocName = input("Please enter government document name: \n")
            updateGovDocPrice = input("Please enter document price: \n")
            updateGovDocConfi = input("Please enter True if document is confidental, False if not")
            govdocList[updateGovDoc-1].GovDocUpdate(updateGovDocPrice,updateGovDocOrgin, updateGovDocName,updateGovDocConfi)

    elif userInput == 6:
        #new customer
        newClientName = input("Please enter new client name: \n")
        newClientaddress = input("Please enter new client address: \n")
        newClientPhoneNumber = input("Please enter new phone number: \n")
        newClientID = len(customerList) + 1
        customerList.append(Client(newClientID, newClientName,newClientaddress,newClientPhoneNumber))
    elif userInput == 7:
        # del customer
        removeClient = int(input("type in ID of a client to delete\n"))
        customerList.pop(removeClient - 1)
        for x in range(len(customerList)):
            customerList[x].UpdateId(x + 1)
    elif userInput == 8:
        # update costomer
        updateCustomer = int(input("type in ID of a customer to update\n"))
        print("selected cumstomer name: " + str(customerList[updateCustomer - 1].cName))
        updateClient = input("Please enter new client name: \n")
        updateClientAddress = input("Please enter new client address: \n")
        updateClientPhoneNumber = input("Please enter new client phone number: \n")
        customerList[updateCustomer - 1].UpdateClientDetails(updateClient, updateClientAddress, updateClientPhoneNumber)
    elif userInput == 9:
        SaveFunction()
        exit("Bye")
    else:
        print("WRONG INPUT TRY AGAIN")
        break


#TODO:
    #GovDocs is confidental is always set as false
    #allow user to update only 1 field instead of whole entry
    #add date when item was checked out

