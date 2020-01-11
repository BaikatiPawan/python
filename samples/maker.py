def format_sentence(sentence):
    capitalized = sentence.capitalize()
    interagations = ("how","what","why")
    if sentence.startswith((interagations)):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)


paragraph =[]
while True:
    user_input = input("Say something... : ")
    if user_input == "\end":
        break
    else:
        paragraph.append(format_sentence(user_input))

print(" ".join(paragraph))









