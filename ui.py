from tkinter import *
from tkinter import ttk
from main import generate_password


def copy2clipboard():
    root.clipboard_clear()
    root.clipboard_append(new_pass_label['text'])
    copy_button['text'] = 'Copied !'
    root.update()
    return


def display_password():
    try:
        pass_len = int(pass_len_box.get())
    except ValueError:
        new_pass_label['text'] = 'Password length must be numeric'
        new_pass_label.pack()
        return

    upper = upper_chk.instate(['selected'])
    nums = nums_chk.instate(['selected'])
    symbols = symbols_chk.instate(['selected'])

    new_pass_label['text'] = generate_password(pass_len, upper, nums, symbols)
    copy_button['text'] = 'Copy to clipboard'
    new_pass_label.pack()
    copy_button.pack()
    
    return


root = Tk()
root.title('Password generator')

# element creation
header_label = Label(root, text="Generate a random password, if nothing is selected, password wil be lowercase only")
pass_len_label = Label(root, text='Password Length')
pass_len_box = Entry(root)
upper_chk = ttk.Checkbutton(root, text='Uppercase characters (fe: A,K,B)')
upper_chk.state(['!alternate'])
nums_chk = ttk.Checkbutton(root, text='Numbers (fe: 1,5,9)')
nums_chk.state(['!alternate'])
symbols_chk = ttk.Checkbutton(root, text='Symbols (fe: @,?,!)')
symbols_chk.state(['!alternate'])
generate_button = Button(root, text='Generate Password', command=display_password)
new_pass_label = Label(root)
copy_button = Button(root, text='', command=copy2clipboard)

# element placement
header_label.pack()
pass_len_label.pack()
pass_len_box.pack()
upper_chk.pack()
nums_chk.pack()
symbols_chk.pack()
generate_button.pack()

if __name__ == "__main__":
    root.mainloop()
