from decryption import decryption
from encryption import encryption

#in my code i split the encyption and decryption into two files. Once user
#inputs a message it is encrypted user the length of my last name, Weetom,
#as the key for the ceaser cyper. I used the ASCII values to decided what he
#encrypted output will be. This way, special characters like !,.$&* can be
#encrypted and decrypted. This program is to be the test to check that the code
#works as intended

decrypt = decryption()
encrypt = encryption()
message = raw_input("Input message:")
encoded_msg = encrypt.encode(message)
print (encoded_msg)

usr_input = raw_input("Would you like to decode message? Y/N: ")
if  (usr_input == "Y") or (usr_input == 'y'):
    print(decrypt.decode(encoded_msg))
else:
    print("Have a good day")
