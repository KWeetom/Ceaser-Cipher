keystring = 'Weetom'
keyvalue = len(keystring)
#print (keyvalue)
    
class encryption:
    
    def encode(self, base_message):
         charlist = []
         new_message = ""

         #this loop splits string into a list of chars and shift it by key value
         #and adds that new value to the output string
         for c in base_message:
                charlist.append(c)
                value = ord(c) + keyvalue
                new_message += chr(value)
                

         return new_message

