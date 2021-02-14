def palindrom(text):
    output_list = []
    for word in text:
        if word.lower() == word[::-1].lower():
            output_list.append(word)
    return output_list
