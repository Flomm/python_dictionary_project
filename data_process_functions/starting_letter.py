def starting_letter(letter, text):
    output_list = []
    for word in text:
        if len(word) != 0:
            if word[0].lower() == letter.lower():
                output_list.append(word)
    return output_list
