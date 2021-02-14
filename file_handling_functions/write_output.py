def write_output(raw_output, file_name):
    try:
        dicts_folder = 'E:/fbger/Flóri/Coding/Projects/python_dictionary/outputs/'
        new_file = open(f'{dicts_folder}{file_name}.txt', 'a+')
        for word in raw_output:
            new_file.write(f'{word}\n')
        new_file.close()
    except:
        print('There was a problem during writing the file.')
