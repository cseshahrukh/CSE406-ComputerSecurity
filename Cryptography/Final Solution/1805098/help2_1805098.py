#author: Md. Shahrukh Islam (1805098)
from bitvector_demo_1805098 import *
import numpy as np
Mixer = [
    [BitVector(hexstring="02"), BitVector(hexstring="03"), BitVector(hexstring="01"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="03"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="03")],
    [BitVector(hexstring="03"), BitVector(hexstring="01"), BitVector(hexstring="01"), BitVector(hexstring="02")]
]

InvMixer = [
    [BitVector(hexstring="0E"), BitVector(hexstring="0B"), BitVector(hexstring="0D"), BitVector(hexstring="09")],
    [BitVector(hexstring="09"), BitVector(hexstring="0E"), BitVector(hexstring="0B"), BitVector(hexstring="0D")],
    [BitVector(hexstring="0D"), BitVector(hexstring="09"), BitVector(hexstring="0E"), BitVector(hexstring="0B")],
    [BitVector(hexstring="0B"), BitVector(hexstring="0D"), BitVector(hexstring="09"), BitVector(hexstring="0E")]
]
column = row = 4
COL = ROW =4

def toASCII(decimal_value):
    # Convert the decimal value to the corresponding ASCII character
    ascii_char = chr(decimal_value)
    # Convert the ASCII character to uppercase
    uppercase_char = ascii_char.upper()

    #print(uppercase_char)
    return uppercase_char


## Mix Column
def mixColumns(state_matrix, mode):
    #print the mode
    print('mode is: ', mode)
    #mode 1 for encryption, else for decryption
    result = [[""]*column for i in range(row)]
    for i in range(len(Mixer)):   #iteration by row of mixer
        for j in range(len(state_matrix[0])):    # iterating by column of state matrix
            for k in range(len(state_matrix)):             # iterating by rows of state matrix
                if mode == 1:      ## Encryption
                    print('before')
                    mult = Mixer[i][k].gf_multiply_modular(BitVector(hexstring=state_matrix[k][j]), AES_modulus, 8)
                    print('after')
                else:
                    mult = InvMixer[i][k].gf_multiply_modular(BitVector(hexstring=state_matrix[k][j]), AES_modulus, 8)
                result[i][j] = (BitVector(hexstring=result[i][j]) ^ (mult)).get_bitvector_in_hex()
    result = np.array(result)
    return result

def MixColumns(mat,isEncryptMode=True):
    if isEncryptMode:
        mixer = Mixer
    else:
        mixer = InvMixer
    ROW = len(mixer)
    COL = len(mat[0])


    
    ret = [[BitVector(intVal=0, size=8) for _ in range(COL)] for _ in range(ROW)]


    for i in range(ROW):
        for j in range(COL):
            for k in range(ROW):
                ret[i][j] ^= mixer[i][k].gf_multiply_modular(BitVector(intVal=mat[k][j]), AES_modulus, 8)


    # Print the result
    """
    for row in ret:
        for elem in row:
            print(elem.get_bitvector_in_hex(), end=' ')
        print()
    """
    

    # Convert hexadecimal values to integers
    for i in range(len(ret)):
        for j in range(len(ret[0])):
            ret[i][j] = ret[i][j].intValue()
        


    return ret

def printAESOutput(stateMatrix, round): 
    print('AES Output for Round ', round)
    #print("Hexadecimal value: ")
    for j in range(0, len(stateMatrix[0])):
        for i in range(0, len(stateMatrix)):
            print(hex(stateMatrix[i][j]), end=" ")
    print()
