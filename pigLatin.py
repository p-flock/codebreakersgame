
import time
translation = ""

def play():
    print("The objective of using Pig Latin is to conceal messages from others not familiar with the rules. A fault proof method of encryption that is best used to secure your most valuable communications. Give it a go!" + "\n" + "\n" + "\n")
    time.sleep(3)
    phraseTranslate = input("Enter the phrase you would like to have translated to Pig Latin: " + "\n")
    parser(phraseTranslate)

def parser(input_string):
    #parses user input into individual words to be translated

    parsed = input_string.split(" ")
    translate(parsed)

def translate(parsed_list):
    global translation
    for word in parsed_list:
        if (word[0] in 'bcdfghjklmnpqrstvwxzy' and word[1] in 'aeiouy'):
            #print("word[0]: ", word[0], "word[1]: ", word[1])
            newWord = word[1:] + word[0] + 'ay'
            translation += newWord + " "
        elif (word[0] in 'bcdfghjklmnpqrstvwxz' and word[1] in 'bcdfghjklmnpqrstvwxz'):
            newWord = word[2:] + word[0:2] + 'ay'
            translation += newWord + " "
        elif (word[0] in 'aeiouy'):
            newWord = word + 'way'
            translation += newWord + " "
        else:
            translation += str(word)
    print("\n" + "Your super secret message: ", translation, "\n")
    time.sleep(2)
    answer = input("Want to play again? Y/N" + "\n")
    if answer in ["y", "Y", "YES", "yes"]:
        translation = ''
        phraseTranslate = input("\n" + "Enter the phrase you would like to have translated to Pig Latin: " + "\n")
        parser(phraseTranslate)
    else:
        return
