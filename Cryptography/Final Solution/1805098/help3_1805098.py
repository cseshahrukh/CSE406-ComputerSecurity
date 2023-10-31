#author: Md. Shahrukh Islam (1805098)
from bitvector_demo_1805098 import *
import binascii

Rcon = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36,  0x6C, 0xD8, 0xAB, 0x4D]
def printPlainText(plainText):
    print("Plain Text:")
    print("In ASCII: "+plainText)

    # Converting string to hex
    hexString = bytes(plainText, 'utf-8').hex()
    print("In Hex: " + hexString)

def printEncryptedText(encryptedMsg):
    print('Cipher Text:')
    # Convert ASCII to hex
    hexString = ''.join(format(ord(c), '02x') for c in encryptedMsg)
    print("In Hex: " + hexString)
    

    print('In ASCII: '+encryptedMsg)

    # If i do this then c2 c4 like special things are printed 
    # Converting ASCII to hex
    #hexString = bytes(encryptedMsg, 'utf-8').hex()
    #print("In Hex: " + hexString)

def printDecryptedText(encryptedMsg):
    print('Deciphered Text:')
    # Convert ASCII to hex
    hexString = ''.join(format(ord(c), '02x') for c in encryptedMsg)
    print("In Hex: " + hexString)
    

    print('In ASCII: '+encryptedMsg)

    # If i do this then c2 c4 like special things are printed 
    # Converting ASCII to hex
    #hexString = bytes(encryptedMsg, 'utf-8').hex()
    #print("In Hex: " + hexString)


def printKey(key):
    print("Key:")
    print("In ASCII: "+key)

    # Converting string to hex
    hexString = bytes(key, 'utf-8').hex()
    print("In Hex: " + hexString)

# hexadecimal to decimal conversion
def hex2dec(s):
    return int(s, 16)

# decimal to hexadecimal conversion
def dec2hex(n):
    s = hex(n)
    return s[2:]

# left shift an array by 1
def leftShiftArray(my_array):
    temp = my_array[0]
    for i in range(0,3):
        my_array[i] = my_array[i+1]
    my_array[3] = temp
    return my_array

# left shift an 2D array by row number
def leftShiftArray2D(my_array):
    for i in range(0,4):
        if i==0:
            continue
        elif i==1:
            temp = my_array[i][0]
            for j in range(0,3):
                my_array[i][j] = my_array[i][j+1]
            my_array[i][3] = temp
        elif i==2:
            temp = my_array[i][0]
            temp2 = my_array[i][1]
            
            my_array[i][1] = my_array[i][3]
            my_array[i][0] = my_array[i][2]
            my_array[i][2] = temp
            my_array[i][3] = temp2
        elif i==3:
            temp = my_array[i][0]
            temp2 = my_array[i][1]
            temp3 = my_array[i][2]
            
            my_array[i][0] = my_array[i][3]
            my_array[i][1] = temp
            my_array[i][2] = temp2
            my_array[i][3] = temp3
    return my_array


# left shift an 2D array by row number
def leftInverseShiftArray2D(my_array):
    for i in range(0,4):
        if i==0:
            continue
        elif i==1:
            temp = my_array[i][3]
            for j in range(3,0,-1):
                my_array[i][j] = my_array[i][j-1]
            my_array[i][0] = temp
        elif i==2:
            temp = my_array[i][0]
            temp2 = my_array[i][1]
            
            my_array[i][1] = my_array[i][3]
            my_array[i][0] = my_array[i][2]
            my_array[i][2] = temp
            my_array[i][3] = temp2
        elif i==3:
            temp0 = my_array[i][0]
            temp1 = my_array[i][1]
            temp2 = my_array[i][2]
            temp3=my_array[i][3]
            
            my_array[i][0] = temp1
            my_array[i][1] = temp2
            my_array[i][2] = temp3
            my_array[i][3] = temp0
    return my_array


#implement hexadecimal value print that takes a byte array
def printHexArray(my_array):
    print("Hexadecimal value: ")
    for i in range(0, len(my_array)):
        print(hex(my_array[i]), end=" ")
    #print() 

#function for printing hex values of a string 
def printHexArrayString(my_array):
    #print("Hexadecimal value: ")
    for i in range(0, len(my_array)):
        print(hex(ord(my_array[i])), end=" ")
    print()
#print the 2D array in hexadecimal format
def printHexArray2D(my_array):
    #print("Hexadecimal value: ")
    for i in range(0, len(my_array)):
        for j in range(0, len(my_array[i])):
            print(hex(my_array[i][j]), end=" ")
        print()
    #print()
    
#implement g function
def g(word, roundConstant):
    hex_number=roundConstant
    
    element_1 = (hex_number >>(6*4)) & 0x3
    element_2 = (hex_number >>(4*4)) & 0x3
    element_3 = (hex_number >>(2*4)) & 0x3
    element_4 = (hex_number >>0) & 0x3

    

    my_array = [0, 0, 0, 0]

    #rotate word
    my_array=leftShiftArray(word)

    #print("After left shift: ")
    #print(word)
    #printHexArray(word)
    #print('size of word[0] is')
    #"""
           #substitute bytes
    for i in range(0,4):
        #get ascii value of word[i]
        #my_array[i] = word[i]
        #convert to decimal
        #my_array[i] = hex2dec(word[i])
        #print('my_array[i] is ' + str(my_array[i]) + ' and type is ' + str(type(my_array[i])))
        my_array[i] = Sbox[my_array[i]]
    
    """
    my_array[0]=my_array[0]^element_1
    my_array[1]=my_array[1]^element_2
    my_array[2]=my_array[2]^element_3
    my_array[3]=my_array[3]^element_4
    """


    my_array[0]=my_array[0]^roundConstant
    #ASCII to char conversion
    #for i in range(0,4):
        #my_array[i] = chr(my_array[i])
    return my_array
    #"""
 
# This fuction takes a key and returns the expanded key of 10 rounds
def keyExpansion(key, keySize):
    #print("Key Expansion")
    # round 0
    # 4 byte means 1 word; total 4 words as 16 bytes 
    # word 
    # w te all round er key gula store rakhbo
    w=[]

   
    # row of w is 4 
    for i in range(4):
        word = [ord(c) for c in key[4*i:4*(i+1)]]
        w.append(word)
        #w.append(key[4*i:4*(i+1)])
    #print('In keyExpansion: ')
    
    keyByte=keySize//8

    #for 128 bits i from 4 to 44

    extra=keyByte-16 
    #for 128 bits extra=0
    #for 192 bits extra=8
    #for 256 bits extra=16

    # round 1 to 10
    for i in range(4,44+extra):
        
        temp = w[i-1]
        temp = list(temp)  # Convert the string to a list
        if i%4 == 0:
            
            temp = g(temp, Rcon[i//4 -1 ])
            #roundConstant = roundConstant + 1
        
        for j in range(0,4):
                #print('temp[j] size is ' + str(len(temp[j])))
                #print('w[i-4][j] size is ' + str(len(w[i-4][j])))

                #print type of temp[j]
                #print('temp[j] type is ', type(temp[j]))
                #print('w[i-4][j] type is ', type(w[i-4][j]))
            temp[j] = temp[j] ^ w[i-4][j]
    
        w.append(temp)

    """
    for i in range(len(w)):
        printHexArray(w[i])
        if i%4 == 3:
            print()
    """

    return w
