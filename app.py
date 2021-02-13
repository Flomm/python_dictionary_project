from functions import starting_letter, process_input, final_letter
dicts_folder = 'E:/fbger/Flóri/Coding/Projects/python_dictionary/dicts/'

words = process_input(dicts_folder)

firstb = starting_letter('b', words)
print(firstb)

lasto = final_letter('o', words)
print(lasto)
