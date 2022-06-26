import zipfile
from zipfile import ZipFile
import os
import shutil
import tkinter
from tkinter import filedialog
from tkinter import ttk
from functools import partial
import tkinter.messagebox as messagebox
import webbrowser

# 포함 되어야 할 폴더
includes = ['/Assets', '/Packages', '/ProjectSettings']


class ZipBuilder:
    # input 디렉토리 절대경로
    dir0 = 'C:/'
    dir1 = 'C:/'
    # input 디렉토리 리스트
    dir_list = [dir0]

    # 산출 상위 폴더 이름
    folder_name = 'Result'
    # 산출 절대경로
    out_dir = 'C:/' + folder_name

    # input에서 각 산출될 이름을 저장
    dir_dictionary = {}

    def __init__(self):
        self.dir_count = 0
        self.label_text = []

        self.window = tkinter.Tk()

        self.windowWidth = 450
        self.windowHeight = 420

        self.window.tk.call("source", "azure.tcl")
        self.window.tk.call("set_theme", "light")

        self.out_text = tkinter.StringVar(value=self.out_dir)
        self.window.title("ZipBuilder")
        self.window.update()
        self.window.geometry("{}x{}+500+300".format(self.windowWidth, self.windowHeight))

        for directory in self.dir_list:
            self.dir_dictionary[directory] = self.make_out_name(directory)
        self.set_frame()
        self.set_buttons()

        self.window.mainloop()

    def set_frame(self):
        ttk.Label(text="디렉토리를 변경할 수 있습니다.").pack()

        input_frame = ttk.LabelFrame(text="Input", padding=(20, 10))
        input_frame.place(x=15, y=40, width=self.windowWidth - 30, height=210)

        output_frame = ttk.LabelFrame(text='Output')
        output_frame.place(x=15, y=280, width=self.windowWidth - 30, height=70)

    def set_buttons(self):
        style = ttk.Style()
        style.configure('Accent.TButton', foreground='white')

        for i in range(0, len(self.dir_list)):
            self.label_text.append(tkinter.StringVar())
            self.label_text[i].set(self.dir_list[i])

        for i in range(0, len(self.dir_list)):
            dir_label = ttk.Label(textvariable=self.label_text[i], width=45, relief='sunken', anchor=tkinter.CENTER)
            dir_label.place(x=100, y=70 * (i + 1))
            dir_button = ttk.Button(self.window, text='Path', style='Accent.TButton', width=5,
                                    command=partial(self.open_dir, i, True))
            dir_button.place(x=30, y=65 * (i + 1))

        ttk.Button(text='+', width=5, command=self.add_button).place(x=370, y=252)

        out_label = ttk.Label(textvariable=self.out_text, width=40, relief='sunken', anchor=tkinter.CENTER)
        out_label.place(x=130, y=312)
        output_button = ttk.Button(text='Output', width=8, style='Accent.TButton', command=partial(self.open_dir, 0, False))
        output_button.place(x=28, y=307)

        start_button = ttk.Button(text='Start', width=25, command=self.make_zip)
        start_button.place(x=120, y=365)

    def add_button(self):
        index = len(self.dir_list)

        if index >= 3:
            return

        self.dir_list.append('C:/')
        self.label_text.append(tkinter.StringVar())
        self.label_text[index].set(self.dir_list[index])

        dir_label = ttk.Label(textvariable=self.label_text[index], width=45, relief='sunken', anchor=tkinter.CENTER)
        dir_label.place(x=100, y=67 * (index + 1))
        dir_button = ttk.Button(self.window, text='Path', style='Accent.TButton', width=5,
                                command=partial(self.open_dir, index, True))
        dir_button.place(x=30, y=65 * (index + 1))

        self.dir_dictionary[self.dir_list[index]] = self.make_out_name(self.dir_list[index])

    def open_dir(self, num, is_input):
        dir_name = filedialog.askdirectory(parent=self.window, initialdir="/", title='폴더를 선택해 주세요')
        print('Select : ', dir_name)

        if is_input:
            if self.dir_list[num] in self.dir_dictionary:
                self.dir_dictionary.pop(self.dir_list[num])
            self.dir_dictionary[dir_name] = self.make_out_name(dir_name)
            self.dir_list[num] = dir_name
            self.label_text[num].set(dir_name)
        else:
            self.out_dir = dir_name
            self.out_text.set(dir_name + self.folder_name)
            for directory in self.dir_dictionary:
                self.dir_dictionary[directory] = self.make_out_name(directory)

    def make_out_name(self, st):
        string = st.split('/')
        return self.out_dir + '/' + self.folder_name + '/' + string[len(string) - 1]

    def exist_path(self, directory):
        if os.path.isdir(directory):
            return True
        else:
            print("Not Exist ::: ", directory)
            return False

    def make_zip(self):
        print('------------ START -------------')
        # includes 내에 속한 폴더만 복사
        for directory in self.dir_dictionary:
            for folder in includes:
                if self.exist_path(directory + folder):
                    shutil.copytree(directory + folder, self.dir_dictionary[directory] + folder, dirs_exist_ok=True)
                    print("From : ", directory + folder,
                          "    =====>    Copy To : ", self.dir_dictionary[directory] + folder)

        # zip 변환
        print("Zipping................")
        for out in self.dir_dictionary:
            filename = self.dir_dictionary[out]
            os.chdir(self.out_dir)
            if self.exist_path(out):
                shutil.make_archive(filename, 'zip', filename)

        print('------------ FINISH -------------')

        tkinter.messagebox.showinfo('완료', '완료 했습니다.')
        self.window.destroy()
        self.window.quit()
        webbrowser.open(self.out_dir)


if __name__ == '__main__':
    ZipBuilder()
