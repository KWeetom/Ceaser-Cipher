keystring = 'Weetom'
keyvalue = len(keystring)
#print (keyvalue)
class decryption():
    def decode(self, encoded_message):
         charlist2 = []
         old_message = ""


         #this loop splits string into a list of chars and shifts to the left 
         #by key value and adds that new value to the output string
         for c in encoded_message:
                charlist2.append(c)
                value = ord(c) - keyvalue
                old_message += chr(value)
                

        
         return old_message
  
