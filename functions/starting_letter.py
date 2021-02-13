def starting_letter(letter, text):
    output_list = []
    for word in text:
        if word[0] == letter:
            output_list.append(word)
    return output_list
