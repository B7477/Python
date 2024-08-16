
## Encrypting Text ## 

# Description: In this program, the user is prompted to input an EXISTING text file name
        # (ending in .txt) and the program will read and turn the text file
        # into a string, which then will be encoded by the dictionary below
        # ultimatly resulting in a complete encoded new text file.


# this is the dictionary created to encrypt what ever character is shown in the old text file into a
    # different character for the new text file
    ## Example: Dict = { key: value, ... }
    
Encrypt_Code = {'A':')','a':'0','B':'(','b':'9','C':'*','c':'8',\
                'D':'&','d':'7','E':'^','e':'6','F':'%','f':'5',\
                'G':'$','g':'4','H':'#','h':'3','I':'@','i':'2',\
                'J':'!','j':'1','K':'Z','k':'z','L':'Y','l':'y',\
                'M':'X','m':'x','N':'W','n':'w','O':'V','o':'v',\
                'P':'U','p':'u','Q':'T','q':'t','R':'S','r':'s',\
                'S':'R','s':'r','T':'Q','t':'q','U':'P','u':'p',\
                'V':'O','v':'o','W':'N','w':'n','X':'M','x':'m',\
                'Y':'L','y':'l','Z':'K','z':'k','!':'J','1':'j',\
                '@':'I','2':'i','#':'H','3':'h','$':'G','4':'g',\
                '%':'F','5':'f','^':'E','6':'e','&':'D','7':'d',\
                '*':'C','8':'c','(':'B','9':'b',')':'A','0':'a',\
                ':':',',',':':','?':'.','.':'?','<':'>','>':'<',\
                "'":'"','"':"'",'+':'-','-':'+','=':';',';':'=',\
                '{':'[','[':'{','}':']',']':'}'}

def encrypting():


    user_file = input("Please Enter File Name: ")

    # create a new file string with the contents of the text file entered by the user
    with open (user_file, 'r+') as text_file:
        new_file = text_file.read()
        print("Original String: ", new_file)

        converted_file = ""

        # because the contents of the file was a string, we can convert each element of that string
        for i in range(0, len(new_file)):

            # check the dictionary aboves keys with each element of the string (array)
            # also, if the character is within the keys of the dictionary, concat the new character to the converted_file string
            # if the character is not in the dictionary, the character will stay as is in the newly convereted file
            if new_file[i] in Encrypt_Code.keys():
                converted_file += Encrypt_Code[new_file[i]]
            else:
                converted_file += new_file[i]
       
        print("Altered String: ", converted_file)

    # create a new text file, and write the newly converted file into it
    with open('Converted_String.txt', 'w') as encrypted_file:
        encrypted_file.write(converted_file)


        
encrypting()
