def pig_latin(word):
    first_letter = word[0]
    if first_letter in "aeiou":
        word += 'ay'
    else:
        word = word[1:] + first_letter + 'ay'
    return word

new_word = pig_latin('ello')
print(new_word)