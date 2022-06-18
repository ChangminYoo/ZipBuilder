import zipfile
from zipfile import ZipFile
import os
import shutil
import tkinter
from tkinter import filedialog
from functools import partial
import tkinter.messagebox as messagebox
import webbrowser

# 포함 되어야 할 폴더
includes = ['/Assets', '/Packages', '/ProjectSettings']


class ZipBuilder:
    # input 디렉토리 절대경로
    dir0 = ''
    dir1 = ''
    # input 디렉토리 리스트
    dir_list = [dir0, dir1]

    # 산출 상위 폴더 이름
    folder_name = 'Result'
    # 산출 절대경로
    out_dir = 'C:/' + folder_name

    # input에서 각 산출될 이름을 저장
    dir_dictionary = {}

    def __init__(self):
        self.window = tkinter.Tk()
        self.dir_count = 0
        self.label_text = []
        self.out_text = tkinter.StringVar(value=self.out_dir)

        self.window.title("ZipBuilder")
        self.window.geometry("350x300+100+100")

        for directory in self.dir_list:
            self.dir_dictionary[directory] = self.make_out_name(directory)

        self.set_buttons()

        self.window.mainloop()

    def set_buttons(self):
        top_label = tkinter.Label(text='디렉토리 경로를 변경할 수 있습니다.', width=40, relief='solid', fg='red')
        top_label.pack()

        out_label = tkinter.Label(textvariable=self.out_text, width=35, relief='solid')
        out_label.place(x=60, y=207)
        output_button = tkinter.Button(self.window, text='산출경로', command=partial(self.open_dir, 0, False))
        output_button.place(y=205)

        start_button = tkinter.Button(self.window, text='Start', width=25, command=self.make_zip)
        start_button.place(x=80, y=250)

        for i in range(0, len(self.dir_list)):
            self.label_text.append(tkinter.StringVar())
            self.label_text[i].set(self.dir_list[i])

        for i in range(0, len(self.dir_list)):
            dir_label = tkinter.Label(textvariable=self.label_text[i], width=40, relief='solid')
            dir_label.place(x=40, y=52*(i+1))

            dir_button = tkinter.Button(self.window, text='push', command=partial(self.open_dir, i, True))
            dir_button.place(y=50*(i+1))

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


