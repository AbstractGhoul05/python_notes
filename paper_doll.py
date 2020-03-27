def paper_doll(word):
    word_copy = ''
    for i in word:
        for x in range(0, 3):
            word_copy += i
    
    return word_copy

print(paper_doll('Hello'))