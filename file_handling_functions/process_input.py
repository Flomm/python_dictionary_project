def process_input(file_name):
    try:
        dicts_folder = 'E:/fbger/Flóri/Coding/Projects/python_dictionary/dicts/'
        formatted_list = []
        dict = open(dicts_folder + f'{file_name}.txt', "r", encoding='utf-8')
        for row in dict:
            if row[-1] == '\n':
                row = row[:-1]
            formatted_list.append(row)
        dict.close()
        return formatted_list
    except:
        return 'File does not exist.'
