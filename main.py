def caesar(rot,text,encrypted): # Defines procedure
     
    alphabet = list('abcdefghijklmnopqrstuvwxyz') # creates list of characters
    uppercase = list('ABCDEFGHIJKLMNOPQRSTUBWXYZ') # creates list of uppercase characters
    new_list = list(text) # divides text input to characters
    print_list = [] # creates list to print

    # for each character 
    for x in new_list: 
        
        if x in alphabet: # if lowercase
            newindex = alphabet.index(x) # find index of the character
            print_list.append(alphabet[(newindex + rot) % 26]) # calculate the shift and add it to the list
        elif x in uppercase: # if uppercase
            newindex = uppercase.index(x) # find index of character
            print_list.append(uppercase[(newindex + rot) % 26]) # calculate the shift and add it to the list
        else : # otherwise
            print_list.append(x) # add the other character to the list
         
        
    str1 = ''.join(print_list) # convert the shifted list to a string
    print ("The string " + str(text) + " shifted by " + str(rot) + " results in the string " + (str1)) # print results
    
#caesar(5,"hello",True)

def main():
    
    rot_input = int(input("Enter the rotation amount: "))
    text_input = str(input("Enter the string: "))
    true_false = str(input("Enter e(encrypted) or d(decrypted): "))

    # if encrypted
    if true_false == 'e':
        caesar(rot_input,text_input,true_false)
    elif true_false == "d": # if decrypted
        caesar(-1*rot_input,text_input,true_false) # change the shift to inverse

main() # calls procedure
