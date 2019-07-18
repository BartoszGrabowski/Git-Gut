from random import randint

gameBoard = []
gameBoardP2 = []
shipsBoard1 = []
shipsBoard2 = []

#populate game board 1
for x in range(6):
    gameBoard.append(["."] * 6)


for x in range(6):
    gameBoardP2.append(["."] * 6)
class Ship:
    def __init__(self, shipSize, shipXpos, shipYpos, rotation):
        self.shipSize = shipSize
        self.shipXpos = shipXpos
        self.shipYpos = shipYpos
        self.rotation = rotation
    def getShipXpos(self):
        return self.shipXpos
    def getShipYpos(self):
        return self.shipYpos
    def getShipSize(self):
        return self.shipSize

    def setShipXpos(self, shipXpos):
        self.shipXpos = shipXpos
    def setShipYpos(self, shipYpos):
        self.shipYpos = shipYpos
    def setShipSize(self, shipSize):
        self.shipSize = shipSize

def PrintBoards(gameBoard, gameBoard2):
    print("\nPlayer 1 board")
    for x in gameBoard:
        print(("  ").join(x))
    print("\n")
    print("Player 2 board")
    for x in gameBoard2:
        print(("  ").join(x))

def RandRow(gameBoard, shipSize):
    return randint(0, len(gameBoard) - (1 + shipSize))
def RandCol(gameBoard, shipSize):
    return randint(0, len(gameBoard[0]) - (1 + shipSize))

def CollisionDetection(gameBoard, ship):

    if ship.rotation == "V":
        if gameBoard[ship.getShipYpos()][ship.getShipXpos()] == "X":
            ship.setShipXpos(RandRow(gameBoard, ship.getShipSize()))
            ship.setShipYpos(RandCol(gameBoard, ship.getShipSize()))
            CollisionDetection(gameBoard, ship)

        for x in range(ship.shipSize):
            if gameBoard[ship.getShipYpos()+x][ship.getShipXpos()] == "X":
                ship.setShipXpos(RandRow(gameBoard, ship.getShipSize()))
                ship.setShipYpos(RandCol(gameBoard, ship.getShipSize()))
                CollisionDetection(gameBoard, ship)

    else:
        if gameBoard[ship.getShipYpos()][ship.getShipXpos()] == "X":
            ship.setShipXpos(RandRow(gameBoard, ship.getShipSize()))
            ship.setShipYpos(RandCol(gameBoard, ship.getShipSize()))
            CollisionDetection(gameBoard, ship)

        for x in range(ship.shipSize):
            if gameBoard[ship.getShipYpos()][ship.getShipXpos() + x] == "X":
                ship.setShipXpos(RandRow(gameBoard, ship.getShipSize()))
                ship.setShipYpos(RandCol(gameBoard, ship.getShipSize()))
                CollisionDetection(gameBoard, ship)


def PlaceShip(gameBoard, ship):
    CollisionDetection(gameBoard, ship)
    if ship.rotation == "V":
        gameBoard[ship.getShipYpos()][ship.getShipXpos()] = "X"
        for x in range(ship.shipSize):
            gameBoard[ship.getShipYpos()+x][ship.getShipXpos()] = "X"

    else:
        gameBoard[ship.getShipYpos()][ship.getShipXpos()] = "X"
        for x in range(ship.shipSize):
            gameBoard[ship.getShipYpos()][ship.getShipXpos() + x] = "X"

shipsBoard1.append(Ship(2, RandRow(gameBoard,2), RandCol(gameBoard,2), "V"))
shipsBoard1.append(Ship(3, RandRow(gameBoard,3), RandCol(gameBoard,3), "H"))
shipsBoard1.append(Ship(2, RandRow(gameBoard,2), RandCol(gameBoard,2), "V"))
shipsBoard1.append(Ship(3, RandRow(gameBoard,3), RandCol(gameBoard,3), "H"))

shipsBoard2.append(Ship(2, RandRow(gameBoardP2,2), RandCol(gameBoard,2), "V"))
shipsBoard2.append(Ship(3, RandRow(gameBoardP2,3), RandCol(gameBoard,3), "H"))
shipsBoard2.append(Ship(2, RandRow(gameBoardP2,2), RandCol(gameBoard,2), "V"))
shipsBoard2.append(Ship(3, RandRow(gameBoardP2,3), RandCol(gameBoard,3), "H"))

for x in shipsBoard1:
    PlaceShip(gameBoard, x)

for x in shipsBoard2:
    PlaceShip(gameBoardP2, x)
playFlag = True
player1Turn = True
player1Board = gameBoard
player2BoardMask = gameBoardP2.copy()
print(len(gameBoard))
while playFlag:
    if player1Turn:
        print("\nPlayer 1 Turn ! ")
        playInput = int(input("input 1 to shoot, 2 to exit"))
        if playInput == 1:
            player2BoardMask = gameBoardP2.copy()
            for x in range(len(gameBoardP2)):
                for z in range(len(gameBoardP2[x])):
                    if gameBoardP2[x][z] == "X":
                        gameBoardP2[x][z] = "."


            PrintBoards(gameBoard, gameBoardP2)
            inputRow = int(input("Player 1 enter row number you want to shoot at: ")) - 1
            inputCol = int(input("Player 1 enter column number you want to shoot at: ")) - 1
            if inputRow >= len(gameBoardP2) or inputCol >= len(gameBoardP2[0]):
                print("YOU SHOOT OUTSIDE OF THE BOARD FOOL!")
            else:
                if player2BoardMask[inputRow][inputCol] == "X":
                    print("HIT HIT HIT")
                    player2BoardMask[inputRow][inputCol] = "O"
                elif player2BoardMask[inputRow][inputCol] == "O":
                    print("WE ALREADY SHOOT THERE CAP")
                else:
                    print("sorry cap we missed completly")
                    player2BoardMask[inputRow][inputCol] = "O"
            #

            gameBoardP2 = player2BoardMask.copy()
        elif playInput == 2:
            playFlag = False
        player1Turn = False
    else:
        print("\n Player 2 Turn ! ")
        PrintBoards(gameBoard, gameBoardP2 )
        inputRow = int(input("Player 2 enter row number you want to shoot at: ")) - 1
        inputCol = int(input("Player 2 enter column number you want to shoot at: ")) - 1
        if inputRow >= len(gameBoard) or inputCol >= len(gameBoard[0]):
            print("YOU SHOOT OUTSIDE OF THE BOARD FOOL!")
        else:
            if gameBoard[inputRow][inputCol] == "X":
                print("HIT HIT HIT")
                gameBoard[inputRow][inputCol] = "O"
            elif gameBoard[inputRow][inputCol] == "O":
                print("WE ALREADY SHOOT THERE CAP")
            else:
                print("sorry cap we missed completly")
                gameBoard[inputRow][inputCol] = "O"

        player1Turn = True



