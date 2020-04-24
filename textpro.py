interrogatives = ("how", "when", "why", "where")

def maker(sentence):
    if sentence.startswith(interrogatives):
        return f"{sentence.capitalize()}? "
    else:
        return f"{sentence.capitalize()}. "

current_str = ''
sentence_list = []
while True:
    current_str = str(input("Say something: "))
    if current_str == '\end':
        break
    sentence_list.append(current_str)

for sentence in sentence_list:
    print(maker(sentence), end="")
