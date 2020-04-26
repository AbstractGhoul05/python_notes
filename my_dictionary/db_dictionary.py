import mysql.connector
from difflib import SequenceMatcher, get_close_matches

con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

data_list = list()

# cursor = con.cursor()

# query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = 'inlay' ")
# results = cursor.fetchall()

# print(results[0])

def give_meaning(word):
    cursor = con.cursor()
    query = cursor.execute(f"SELECT * FROM Dictionary WHERE Expression = '{word}'")
    meaning_list = cursor.fetchall()
    if len(meaning_list) == 0:
        data_list = list()
        if len(data_list) ==  0:
            query = cursor.execute("SELECT Expression FROM Dictionary")
            all_data = cursor.fetchall()
            data_list = [data[0] for data in all_data]
        close_words = get_close_matches(word, data_list)
        for close_word in close_words:
            control_str = str(input(f"Did you mean {close_word}? (y/n): "))
            if control_str.lower() == 'y':
                return give_meaning(close_word)
        return "No words found!"
    else:
        final_meaning = ''

        for meaning in meaning_list:
            final_meaning += meaning[1] + '\n'

        return final_meaning


print("Welcome to my Dictionary!!!\n")

while True:
    word = str(input("Enter a word: "))
    if word == "q":
        break
    print(give_meaning(word))
