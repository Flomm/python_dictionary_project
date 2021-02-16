def write_output(raw_output, file_name):
    try:
        new_file = open(f'./outputs/{file_name}.txt', 'a+')
        for word in raw_output:
            new_file.write(f'{word}\n')
        new_file.close()
        return f'{file_name}.txt has been succesfully created!'
    except:
        return 'There was a problem during writing the file. Please try again.'
