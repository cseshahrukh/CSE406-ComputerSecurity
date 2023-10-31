#author: Md. Shahrukh Islam (1805098)
import fileinput
from bitvector_demo_1805098 import *
from help3_1805098 import *
from help2_1805098 import *
import time

def AES_key_input(key):
    #write key to a file
    f = open("keyInput2.txt", "w")
    f.write(key)
    f.close()
    
# implement AES encryption with 10 rounds 
def AES_Encryption(block, key):
    
    #print(block)
    
    #print(key) 2D array with 4 columns and onek rows 

    EncryptedText = ''


    stateMatrix = [['' for _ in range(4)] for _ in range(4)]

    for n in range(0,len(block)):
        for j in range(0,4):
            for i in range(0,4):
                stateMatrix[i][j] = key[j][i] ^ ord(block[n][j*4+i])
        #printHexArray2D(stateMatrix)
        #round 0 is done
        
        #print('After round 0 stateMatrix is:')
        #printHexArray2D(stateMatrix)
        # round 1 to 10
        for i in range(1,11):
            #substitude each element of stateMatrix with sbox
            for j in range(0,4):
                for k in range(0,4):
                    stateMatrix[j][k] = Sbox[stateMatrix[j][k]]

            #printHexArray2D(stateMatrix)
            #print()
            #shift rows
            stateMatrix = leftShiftArray2D(stateMatrix)
            #printHexArray2D(stateMatrix)
            #print()

            #for j in range(0,4):
                #for k in range(0,4):
                    #stateMatrix[j][k] = toASCII(stateMatrix[j][k])
            
            #no mix in last round 
            #now mix columns
            if(i!=10):
                stateMatrix = MixColumns(stateMatrix, True)

            #print()
            #printHexArray2D(stateMatrix)

            #add round key
            for j in range(0,4):
                for k in range(0,4):
                    stateMatrix[j][k] = stateMatrix[j][k] ^ key[i*4+k][j]
            #printHexArray2D(stateMatrix)

            #printAESOutput(stateMatrix, i)

        
        for j in range(0,4):
            for i in range(0,4):
                EncryptedText = EncryptedText + chr(stateMatrix[i][j])
        #print('In AES encryption EncryptedText is ' + EncryptedText)
    return EncryptedText

def AES_Decryption(block, key):
    #print('In decryption block is' + str(block))
    #print('hello')
    #print(block[0])

    #print('prining block[0] in hex')
    #printHexArrayString(block[0])
    #block is okay 
    decryptedText = ''

    #print(key) 2D array with 4 columns and onek rows 
    #Round 0

    #Add round key
    stateMatrix = [['' for _ in range(4)] for _ in range(4)]
    for n in range(0,len(block)):
        for j in range(0,4):
            for i in range(0,4):
                #stateMatrix[i][j] = key[j+40][i] ^ ord(block[0][j*4+i])
                stateMatrix[i][j] = ord(block[n][j*4+i])
        
        stateMatrix = [['' for _ in range(4)] for _ in range(4)]
        for j in range(0,4):
            for i in range(0,4):
                #stateMatrix[i][j] = key[j+40][i] ^ ord(block[0][j*4+i])
                stateMatrix[i][j] = ord(block[n][j*4+i]) ^ key[40+j][i]
        #printHexArray2D(stateMatrix)
        #round 0 is done
        #print('After round 0 stateMatrix is:')
        #printHexArray2D(stateMatrix)

        # round 1 to 10
        for i in range(1,11):
            
            #shift rows
            stateMatrix = leftInverseShiftArray2D(stateMatrix)
            #printHexArray2D(stateMatrix)
            #print()

            #inverse substitude each element of stateMatrix with sbox
            for j in range(0,4):
                for k in range(0,4):
                    stateMatrix[j][k] = InvSbox[stateMatrix[j][k]]

            #printHexArray2D(stateMatrix)
            #print()
            

            #add round key
            for j in range(0,4):
                for k in range(0,4):
                    stateMatrix[j][k] = stateMatrix[j][k] ^ key[40-i*4+k][j]
            #printHexArray2D(stateMatrix)


            #for j in range(0,4):
                #for k in range(0,4):
                    #stateMatrix[j][k] = toASCII(stateMatrix[j][k])
            
            #no mix in last round 
            #now inverse mix columns
            if(i!=10):
                stateMatrix = MixColumns(stateMatrix, False)

            #print()
            #printHexArray2D(stateMatrix)

        
            #printAESOutput(stateMatrix, i)

        
        for j in range(0,4):
            for i in range(0,4):
                decryptedText = decryptedText + chr(stateMatrix[i][j])
    return decryptedText

def AES_Encryption_Text(plainText, key):
    print('hello')
    printPlainText(plainText)
    print()
    printKey(key)
    print()

    #check if key is 16 bytes or not (128 bits)
    if(len(key)!=16):
        #if key is less than 16 bytes add non char to it
        if(len(key)<16):
            key = key + '\0'*(16-len(key))
        #if key is more than 16 bytes truncate it
        else:
            key = key[:16]
    
    blocks = []  # Declare the blocks array outside the if condition

    #check if plaintest is 16 bytes or not (128 bits)
    if(len(plainText)!=16):
        #divide plaintext into 16 byte blocks
        blocks = [plainText[i:i+16] for i in range(0, len(plainText), 16)]
        #if last block is less than 16 bytes add non char to it
        if(len(blocks[-1])<16):
            blocks[-1] = blocks[-1] + '\0'*(16-len(blocks[-1]))
    else:
        blocks.append(plainText)
    #copy contents of plaintext to blocks


    allkeys=keyExpansion(key)


    start_time = time.time()
    encryptedMsg=AES_Encryption(blocks, allkeys)
    
    printEncryptedText(encryptedMsg)
    print() 
    return encryptedMsg



def AES_Decryption_Text(encryptedMsg, key):
    blocks2 = []  # Declare the blocks array outside the if condition

    #check if plaintest is 16 bytes or not (128 bits)
    if(len(encryptedMsg)!=16):
        #divide plaintext into 16 byte blocks
        blocks2 = [encryptedMsg[i:i+16] for i in range(0, len(encryptedMsg), 16)]
        #if last block is less than 16 bytes add non char to it
        if(len(blocks2[-1])<16):
            blocks2[-1] = blocks2[-1] + '\0'*(16-len(blocks2[-1]))
    else:
        blocks2.append(encryptedMsg)

    allkeys=keyExpansion(key)

    againPlainText = AES_Decryption(blocks2, allkeys)
    #orinal file e null ta truncate
    againPlainText = againPlainText.replace('\0', '')

    printDecryptedText(againPlainText)
    print()
    file = open('decryptedText.txt', 'w')
    file.write(againPlainText)
    file.close()
    return againPlainText

# main function
def main():

    plainText=''
    for line in fileinput.input(files ='plaintextInput.txt'):
        plainText = plainText + line

    printPlainText(plainText)



    key=''
    # Using fileinput.input() method
    for line in fileinput.input(files ='keyInput.txt'):
        key = key + line

    #input key length from inputHellman.txt file
    keyLength = int(open('inputHellman.txt', 'r').readline())
    print('key length is: ', keyLength)
    print()
    printKey(key)
    print()
    
    keyByte=keyLength//8
    # Start the timer
    start_time = time.time()
    #check if key is 16 bytes or not (128 bits)
    if(len(key)!=keyByte):
        #if key is less than 16 bytes add non char to it
        if(len(key)<keyByte):
            key = key + '\0'*(keyByte-len(key))
        #if key is more than 16 bytes truncate it
        else:
            key = key[:keyByte]
    
    blocks = []  # Declare the blocks array outside the if condition

    #check if plaintest is 16 bytes or not (128 bits)
    if(len(plainText)!=16):
        #divide plaintext into 16 byte blocks
        blocks = [plainText[i:i+16] for i in range(0, len(plainText), 16)]
        #if last block is less than 16 bytes add non char to it
        if(len(blocks[-1])<16):
            blocks[-1] = blocks[-1] + '\0'*(16-len(blocks[-1]))
    else:
        blocks.append(plainText)
    #copy contents of plaintext to blocks




    
    allkeys=keyExpansion(key, keyLength)

    # End the timer
    end_time = time.time()

    # Calculate the elapsed time
    elapsed_time_key_schedule = end_time - start_time

    
    #print(allkeys)
    #print('In main blocks are')
    #print(blocks[0])

    start_time = time.time()
    encryptedMsg=AES_Encryption(blocks, allkeys)
    # End the timer
    end_time = time.time()

    
    printEncryptedText(encryptedMsg)
    print() 

    # Calculate the elapsed time
    elapsed_time_encryption = end_time - start_time

    



    blocks2 = []  # Declare the blocks array outside the if condition

    #check if plaintest is 16 bytes or not (128 bits)
    if(len(encryptedMsg)!=keyByte):
        #divide plaintext into 16 byte blocks
        blocks2 = [encryptedMsg[i:i+16] for i in range(0, len(encryptedMsg), 16)]
        #if last block is less than 16 bytes add non char to it
        if(len(blocks2[-1])<16):
            blocks2[-1] = blocks2[-1] + '\0'*(16-len(blocks2[-1]))
    else:
        blocks2.append(encryptedMsg)

    start_time = time.time()
    againPlainText = AES_Decryption(blocks2, allkeys)
    #orinal file e null ta truncate
    againPlainText = againPlainText.replace('\0', '')
    end_time = time.time()
    
    printDecryptedText(againPlainText)
    print()

    # Calculate the elapsed time
    elapsed_time_decryption = end_time - start_time

    
    #print('plaintext is',plainText)
    #print('block is ', blocks)

    
    #print('againPlainText is',againPlainText)
    #write the decrypted text to file
    file = open('decryptedText.txt', 'w')
    file.write(againPlainText)
    file.close()

    print('Execution time details:')
    # Print the runtime
    # Print the runtime with 20 decimal places
    print("Key Scheduling : {:.20f} seconds".format(elapsed_time_key_schedule))

    # Print the runtime
    # Print the runtime with 20 decimal places
    print("Encryption Time : {:.20f} seconds".format(elapsed_time_encryption))

    # Print the runtime
    # Print the runtime with 20 decimal places
    print("Decryption Time : {:.20f} seconds".format(elapsed_time_decryption))


    if(plainText==againPlainText):
        print('Decryption is correct')


if __name__ == "__main__":
    main()