from wordle_list import words_list

def find_words_with_correct_letters(words_list, correct_letters):
    matching_words = [word for word in words_list if all(letter in word for letter in correct_letters)]
    return matching_words

# Introduction and setting guessed leters into a list
print("\nHello, I am Wordle Assistant. I am here to assist you with your wordle.")
def wordle_assistant():
    guessed_word = input("\nPlease provide the correct characters of the word you have guessed with no commas or spaces.\nFor example: If the word you have guessed is 'Radio' and the the correct letters are r, d, and o, insert rdo.\nPlease provide those characters below:\n\n")
    guessed_letters = list(guessed_word)
    print("\nList of correct letters:\n", guessed_letters)

    # Create a list of correct letters from the guessed word
    correct_letters = [letter for letter in guessed_word if letter in guessed_letters]

    # Find words in the word list that contain the correct letters
    matching_words = find_words_with_correct_letters(words_list, correct_letters)
    print("\nPossible solutions:\n", matching_words)

    wordle_complete = input("\nHave you complete the wordle? Y or N:\n")
    if wordle_complete.lower() == "y": 
        print("\n🎉Congratulations!!!🎉 I am glad that I was able to help. Goodbye. 👋\n")
        exit()
    else:
        return wordle_assistant()
    
wordle_assistant()
