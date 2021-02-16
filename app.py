import tkinter as tk
import tkinter.ttk as ttk
import datetime

from data_process_functions import starting_letter, final_letter, anagram, palindrom
from file_handling_functions import process_input, write_output


def write_log(log_message):
    log.configure(state='normal')
    log.insert(
        'end', f'{log_message}  {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}\n')
    log.configure(state='disabled')


def run_chosen_func():
    if add_name.get() == '':
        write_log('Please add a name for the file.')
        return False
    input_dict = process_input(dicts_drop.get())
    if type(input_dict) is str:
        write_log(input_dict)
        return False

    if choose_func.current() == 0:
        if letter_input.get() == '':
            write_log('Please add a word.')
            return False
        output_list = anagram(letter_input.get(), input_dict)
    elif choose_func.current() == 1:
        output_list = palindrom(input_dict)
    elif choose_func.current() == 2:
        if len(letter_input.get()) != 1:
            write_log('Please add a letter.')
            return False
        output_list = starting_letter(letter_input.get(), input_dict)
    elif choose_func.current() == 3:
        if len(letter_input.get()) != 1:
            write_log('Please add a letter.')
            return False
        output_list = final_letter(letter_input.get(), input_dict)

    result_log = write_output(output_list, add_name.get())
    write_log(result_log)
    file_name.set('')
    letter_input.set('')
    return True


# create and configure window
window = tk.Tk()
window.title('ReadDict')
window.geometry('1100x500')
window.configure(bg='#333B3F')
# create string variables for the entries
file_name = tk.StringVar()
letter_input = tk.StringVar()
file_name.set('')
letter_input.set('')
# create and pack frames
left_frame = tk.LabelFrame(bg='#0078D7', bd=2)
left_frame.pack(side='left', padx=20, pady=20)
right_frame = tk.LabelFrame(bg='#0078D7', text='LOG')
right_frame.pack(side='right', padx=20, pady=20)
# create other widgets
button = tk.Button(left_frame, text='Enter',
                   bg='#333B3F', fg='white', command=run_chosen_func)
add_name = tk.Entry(left_frame, textvariable=file_name, width=10)
file_label = tk.Label(left_frame, text='Choose a name for the output file:')
dicts_drop = ttk.Combobox(left_frame, state='readonly', width=10)
drop_label = tk.Label(left_frame, text='Choose a dictionary:')
choose_func = ttk.Combobox(left_frame, state='readonly', width=25)
func_label = tk.Label(left_frame, text='Choose a function:')
add_letter = tk.Entry(left_frame, textvariable=letter_input, width=15)
letter_label = tk.Label(
    left_frame, text='Add a letter or word, according to chosen function:')
log = tk.Text(right_frame, state='normal', width=50,
              height=19, cursor='arrow', bg='#333B3F', fg='white')
scroll_bar = ttk.Scrollbar(right_frame)
scroll_bar.config(command=log.yview)
log.config(yscrollcommand=scroll_bar.set)
# configure comboboxes
dicts_drop['values'] = ['English', 'German', 'French']
choose_func['values'] = ['Find all anagrams of a word',
                         'Find all palindroms', 'Find words with given first letter', 'Find words with given last letter']
dicts_drop.current(0)
choose_func.current(0)
# set grid representation
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
# launch window
window.mainloop()
