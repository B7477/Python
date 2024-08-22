## Pig Latin Translator ##

# Description: In this program, the user will input a text file name (ending in .txt) as the input. Then the program will open the file inputed (so long as it is in
    # the same location as this file) and will convert the text file into a string, then a list of strings (words into a sentence). Then, as seen below, the program 
    # will translate the given text fill to the Pig Latin specified in the instructions.
    

def English_file():
    user_file = input("Please Enter File Name: ")
    with open (user_file, 'r') as text_file:
        new_file = text_file.read()
    #print(new_file)

    with open (user_file, 'r') as string_file:
        for word in string_file:
            strings = word.split()
            #print(strings)
    print(f'New File Contents:\n')

    with open('piglatin_translation.txt', 'w') as latin_file:

            for word in strings:
                translation = word[1:]+word[0]+'ay '
                print(translation, end=" ")
                latin_file.write(translation)


English_file()
