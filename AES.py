"""

AES encryption and decryption lib.
Made by Paul Knutson

Required functions:                 Status:
- XOR                               Done
- SubBytes with S-Box               Done
- LSO/RSO for elements and rows.    Done
- USO/DSO (Up/Down)                 Done (not tested)   (replace with column flip (row -> column) of matrix)
- Column -> Row matrix flip         Done
- MixColumns                        Done
- ARK? (LSO + XOR?) + key rounds    Not yet

Conversion functions:               Status:
- Hex --> Binary                    Done
- Binary --> Hex                    Done
- Unicode? --> Hex/Binary           Not yet


Steps in AES:
- AddRoundKey
    - XOR
- SubBytes
    - S-Box
- ShiftRows
    - LSO/RSO
- MixColumns
    - rowColFlip
    - LSO/RSO
    - S-Box
    - hexToBin
    - XOR x2
    - binToHex

"""

import csv



def bitwiseXOR(aa, bb):
    """ XOR two bits and return result """
    if(aa == bb):
        return "0"
    return "1"

def XOR(a, b):
    """ XOR a list, two elements at the time, and return the outcome """
    # check if length is the same. If not, change length?
    c = a
    #print(a)
    #print(b)

    for i in range(len(a)):
        c[i] = bitwiseXOR(a[i], b[i])
    #print(c)
    return c


def hexXOR(a, b):
    #print(hexToBin(a))
    #print(hexToBin(b))
    #print()
    #print(str(a) + " | " + str(b))
    aBin = hexToBin(a)
    bBin = hexToBin(b)
    #print(aBin)
    #print(bBin)
    #print()
    cBin = XOR(aBin, bBin)
    #print(cBin)
    c = binToHex(cBin)
    #print(c)
    return c





#a = [0, 1, 1, 0]
# = [1, 0, 1, 0]
#c = XOR(a, b)
#print(c)



def USO(listx, index, n=1):
    """ USO: Up (circular) Shift Operation - Shifts n=1 single element up """
    for j in range(n):
        tmp = listx[0][index]
        for i in range(len(listx) - 1):
            listx[i][index] = listx[i + 1][index]
        listx[len(listx) - 1][index] = tmp
    return listx

def DSO(listx, index, n=1):
    """ DSO: Down (circular) Shift Operation - Shifts n=1 single element down """
    for j in range(n):
        tmp = listx[len(listx) - 1][index]
        for i in range(len(listx) - 1):
            listx[len(listx) - i - 1][index] = listx[len(listx) - i - 2][index]
        listx[0] = tmp
    return listx


def LSO(listx, n=1):
    """ LSO: Left (circular) Shift Operation - Shifts n=1 single element to the left """
    for j in range(n):
        tmp = listx[0]
        for i in range(len(listx) - 1):
            listx[i] = listx[i + 1]
        listx[len(listx) - 1] = tmp
    return listx

def RSO(listx, n=1):
    """ RSO: Right (circular) Shift Operation - Shifts n=1 single element to the right """
    for j in range(n):
        tmp = listx[len(listx) - 1]
        for i in range(len(listx) - 1):
            listx[len(listx) - i - 1] = listx[len(listx) - i - 2]
        listx[0] = tmp
    return listx

#lst = ["A", "B", "C", "D", "E", "F"]
#print(lst)
#LSO(lst)    # Why does this function call affect the global variable lst!?
#print(lst)



def rowColFlip(Matrix):
    rowLen = len(Matrix[0])
    colLen = len(Matrix)
    newMatrix = [None] * rowLen

    for i in range(colLen):
        tmpCol = [None] * colLen
        for j in range(rowLen):
            tmpCol[j] = Matrix[j][i]
        newMatrix[i] = tmpCol

    return newMatrix



#A = [
#        [1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]
#    ]

#print(A)
#A = rowColFlip(A)
#print(A)


def binToList(binary):
    binaryList = [None] * len(binary)
    for i in range(len(binary)):
        binaryList[i] = binary[i]
    return binaryList

# 228: e4 -> 1110 0100
def hexToBin(hexa):
    #for i in range(len(hex)):
    #print(hexa)
    hexa = "0x" + hexa.upper()
    integer = int(hexa, 16)
    binary = bin(integer)
    binary = binary[2:]
    if(len(binary) < 8):
        for i in range(8 - len(binary)):
            binary = "0" + binary

    return binToList(binary)

# 14: 1110 -> e
def singleBinToHex(binaryList):
    #print(binaryList)
    binStr = "".join(binaryList)
    #print(binStr)
    #print()
    if      (binStr == "0000"):
        return "0"
    elif    (binStr == "0001"):
        return "1"
    elif    (binStr == "0010"):
        return "2"
    elif    (binStr == "0011"):
        return "3"
    elif    (binStr == "0100"):
        return "4"
    elif    (binStr == "0101"):
        return "5"
    elif    (binStr == "0110"):
        return "6"
    elif    (binStr == "0111"):
        return "7"
    elif    (binStr == "1000"):
        return "8"
    elif    (binStr == "1001"):
        return "9"
    elif    (binStr == "1010"):
        return "a"
    elif    (binStr == "1011"):
        return "b"
    elif    (binStr == "1100"):
        return "c"
    elif    (binStr == "1101"):
        return "d"
    elif    (binStr == "1110"):
        return "e"
    elif    (binStr == "1111"):
        return "f"


# 228: 1110 0100 -> e4
def binToHex(binaryList):
    #print(binaryList)
    nums = int(len(binaryList) / 4)
    hexa = [None] * nums
    counter = 0
    for i in range(nums):
        tmpBin = [None] * 4
        for j in range(4):
            tmpBin[j] = binaryList[counter]
            counter += 1
        hexa[i] = singleBinToHex(tmpBin)
    #print(hexa)
    return "".join(hexa)



#hexad = "e4"
#print(hexToBin(hexad))

#binar = [1, 1, 1, 0,   0, 1, 0, 0]
#print(binToHex(binar))


def is_digit(x):
    """ Check if number and a single digit xE[0, 9] """
    try:
        x = int(x)
        if (x >= 0 and x <= 9):
            return True
        else:
            return False
    except:
        return False

def SBoxIndex(x):
    start = 0
    if is_digit(x):
        return int(x) + start
    x = x.lower()
    if   (x == "a"):
        return (10 + start)
    elif (x == "b"):
        return (11 + start)
    elif (x == "c"):
        return (12 + start)
    elif (x == "d"):
        return (13 + start)
    elif (x == "e"):
        return (14 + start)
    elif (x == "f"):
        return (15 + start)


def constructSBox():
    SBoxMatrix = []
    with open('SBox.csv', 'rt') as csvSBOX:
        table = csv.reader(csvSBOX, delimiter=',', quotechar='|')
        # for row in spamreader:
        #    print (row)
        tmp = []
        for row in table:
            tmp = row[:16]
            # print(tmp)
            SBoxMatrix.append(tmp)

    SBoxMatrix.pop(len(SBoxMatrix) - 1)
    #print(SBoxMatrix)
    return SBoxMatrix

def SBox(pos):
    SBoxMatrix = constructSBox()

    posy = SBoxIndex(pos[0])
    posx = SBoxIndex(pos[1])
    #print(posx)
    #print(posy)

    return SBoxMatrix[posy][posx]

#print(SBox("cf"))



def SBoxList(hexList):
    for i in range(len(hexList)):
        hexList[i] = SBox(hexList[i])
    return hexList



def roundConstant(i):
    altVar = hex(((2 ** i) % 229))[2:]  # Not quite sure why 229 here.
    if (len(altVar) < 2):
        altVar = "0" + altVar
    altCol = [altVar, "00", "00", "00"]

    #print(altCol)
    return altCol


def MixColumn(Matrix):
    Columns = Matrix
    #Columns.append()

    for i in range(len(Columns) * 5 - 3):
        newCol = Columns[i + 3][:]
        #print(newCol)
        if(i%4 == 0):
            newCol = LSO(newCol)
            newCol = SBoxList(newCol)
        oldCol = Columns[i]
        if(i%4==0):
            altCol = roundConstant(int(i/4))

        #print(newCol)
        #print(oldCol)
        #print(altCol)
        #print()

        first = [None] * 4
        second = [None] * 4
        for p in range(4):
            #print("XOR: " + str(newCol[p] + " | " + str(oldCol[p])))
            first[p] = hexXOR(newCol[p], oldCol[p])
            #print("= " + str(first[p]))
        #print(first)
        if(i%4 == 0):
            for p in range(4):
                second[p] = hexXOR(first[p], altCol[p])

            Columns.append(second)
        else:
            Columns.append(first)
    printCols(Columns)







def printCols(Matrix):
    for i in range(len(Matrix[0])):
        for j in range(len(Matrix)):
            print(Matrix[j][i], end="\t")
        print()

def printRows(Matrix):
    for i in range(len(Matrix)):
        for j in range(len(Matrix[0])):
            print(Matrix[i][j], end="\t")
        print()

A = [
        ["2b", "7e", "15", "16"],
        ["28", "ae", "d2", "a6"],
        ["ab", "f7", "15", "88"],
        ["09", "cf", "4f", "3c"]
    ]
#printCols(A)
#print()
#printRows(A)

MixColumn(A)




#a = "2b"
#b = "8a"
#c = "01"
#d = hexXOR(a, b)
#e = hexXOR(d, c)

#print(e)

# fak git and github
