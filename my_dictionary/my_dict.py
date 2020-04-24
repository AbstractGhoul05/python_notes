import json
from difflib import SequenceMatcher, get_close_matches

data_dict = {}
with open("data.json") as data_file:
    data_dict = json.load(data_file)

def give_meaning(word):
    try:
        meaning_list = data_dict[word.lower()]
    except KeyError:
        close_words = get_close_matches(word, data_dict.keys())
        for close_word in close_words:
            control_str = str(input(f"Did you mean {close_word}? (y/n): "))
            if control_str.lower() == 'y':
                return give_meaning(close_word)
        return "No words found!"
    else:
        final_meaning = ''

        for meaning in meaning_list:
            final_meaning += meaning + '\n'

        return final_meaning


print("Welcome to my Dictionary!!!\n")

while True:
    word = str(input("Enter a word: "))
    if word == "q":
        break
    print(give_meaning(word))
