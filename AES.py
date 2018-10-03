"""

AES encryption and decryption lib.
Made by Paul Knutson

Required functions:                 Status:
- XOR                               Done
- SubBytes with S-Box               Done
- LSO/RSO for elements and rows.    Done
- USO/DSO (Up/Down)                 Done (not tested)
- MixColumns                        Not yet
- ARK? (LSO + XOR?) + key rounds    Not yet

Conversion functions:               Status:
- Hex --> Binary                    Not yet
- Binary --> Hex                    Not yet
- Unicode? --> Hex/Binary           Not yet

"""

import csv



def bitwiseXOR(aa, bb):
    """ XOR two bits and return result """
    if(aa == bb):
        return 0
    return 1

def XOR(a, b):
    """ XOR a list, two elements at the time, and return the outcome """
    # check if length is the same. If not, change length?
    c = a
    for i in range(len(a)):
        c[i] = bitwiseXOR(a[i], b[i])
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

    posx = SBoxIndex(pos[0])
    posy = SBoxIndex(pos[1])
    print(posx)
    print(posy)

    return SBoxMatrix[posy][posx]

#print(SBox("b9"))
