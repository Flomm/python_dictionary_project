import tkinter as tk
import tkinter.ttk as ttk
import datetime
from data_process_functions import starting_letter, final_letter, anagram, palindrom
from file_handling_functions import process_input, write_output
dicts_folder = 'E:/fbger/Flóri/Coding/Projects/python_dictionary/dicts/'


# def test():
   


window = tk.Tk()
window.title('ReadDict')
window.geometry('800x1200')
window.configure(bg='grey')

file_name = tk.StringVar()
letter_input = tk.StringVar()
file_name.set('')
letter_input.set('')


button = tk.Button(window, text='Enter', bg='blue', fg='white', command=test)
add_name = tk.Entry(window, textvariable=file_name, width=10)
file_label = tk.Label(window, text='Choose a name for the output file:')
dicts_drop = ttk.Combobox(window, state='readonly', width=10)
drop_label = tk.Label(window, text='Choose a dictionary:')
choose_func = ttk.Combobox(window, state='readonly', width=25)
func_label = tk.Label(window, text='Choose a function:')
add_letter = tk.Entry(window, textvariable=letter_input, width=15)
letter_label = tk.Label(
    window, text='Add a letter or word, according to chosen function.')
log = tk.Text(window, state='disabled')
log.insert(1.0, 'Log\n')


dicts_drop['values'] = ['English', 'German', 'Spanish', 'French']
choose_func['values'] = ['Find all anagrams of a word',
                         'Find all palindroms', 'Find words with given first letter', 'Find words with given last letter']
dicts_drop.current(0)
choose_func.current(0)

add_name.grid(row=1, column=2, padx=20, pady=20)
file_label.grid(row=1, column=1, padx=10, pady=20)
dicts_drop.grid(row=2, column=2, padx=10, pady=20)
drop_label.grid(row=2, column=1, padx=10, pady=20)
choose_func.grid(row=3, column=2, padx=10, pady=20)
func_label.grid(row=3, column=1, padx=10, pady=20)
add_letter.grid(row=4, column=2, padx=10, pady=20)
letter_label.grid(row=4, column=1, padx=10, pady=20)
button.grid(row=5, column=1, padx=10, pady=20)
log.grid(row=1, column=3, padx=10)

window.mainloop()
