import tkinter
from tkinter import filedialog

# 디렉토리 리스트
dir_list = []
dir_count = 2


def gui_init():
    global window
    window = tkinter.Tk()

    window.title("ZipBuilder")
    window.geometry("300x300+100+100")

    set_buttons()

    window.mainloop()


def set_buttons():
    #add_dir = tkinter.Button(window, text='+', width=5, overrelief='solid', command=add_directory)
    #add_dir.grid(row=1, column=0)
    #remove_dir = tkinter.Button(window, text='-', width=5, overrelief='solid', command=add_directory)
    #remove_dir.grid(row=1, column=1)

    top_label = tkinter.Label(text="디렉토리를 추가/제거할 수 있습니다.", width=30, relief='solid', fg='red')
    top_label.grid(row=1, column=2)

    dir_button1 = tkinter.Button(window, text='push', command=open_dir)
    dir_button1.grid(row=4, column=0)

    dir_button2 = tkinter.Button(window, text='push', command=open_dir)
    dir_button2.grid(row=5, column=0)

    dir_label1 = tkinter.Label()

def open_dir():
    dir_name = filedialog.askdirectory(parent=window, initialdir="/", title='폴더를 선택해주세요')
    print('Select : ', dir_name)
    dir_list.append(dir_name)

