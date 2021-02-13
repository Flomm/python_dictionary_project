def process_input(path):
    formatted_list = []
    dict = open(path + 'test.txt')
    for row in dict:
        if row[-1] == '\n':
            row = row[:-1]
        formatted_list.append(row)
    dict.close()
    return formatted_list
