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
    dir0 = 'C:/morph/AvatarStudio/StagingProject'
    dir1 = 'C:/morph/BuildProject/BuildProject_DLL'
    # input 디렉토리 리스트
    dir_list = [dir0, dir1]

    # 산출 절대경로
    out_dir = 'C:/morph/Result'
    # 산출 상위 폴더 이름
    folder_name = 'Result/'

    # input에서 각 산출될 이름을 저장
    dir_dictionary = {}

    def __init__(self):
        self.window = tkinter.Tk()
        self.dir_count = 0
        self.label_text = []
        self.window.title("ZipBuilder")
        self.window.geometry("350x300+100+100")

        for directory in self.dir_list:
            string_list = directory.split('/')
            self.dir_dictionary[directory] = self.out_dir + '/' + self.folder_name + string_list[len(string_list) - 2]

        self.set_buttons()

        self.window.mainloop()

    def add_button(self):
        if self.dir_count > 2:
            return
        # input
        input_button = tkinter.Button(self.window, text='Input', command=lambda: self.open_dir(self.dir_count))
        input_button.pack()

        self.dir_count += 1

    def set_buttons(self):
        top_label = tkinter.Label(text='디렉토리 경로를 변경할 수 있습니다.', width=40, relief='solid', fg='red')
        top_label.pack()

        output_button = tkinter.Button(self.window, text='산출 경로 수정', width=25,
                                       command=self.open_output_dir)
        output_button.place(x=80, y=200)

        start_button = tkinter.Button(self.window, text='Start', width=25, command=self.make_zip)
        start_button.place(x=80, y=250)

        for i in range(0, len(self.dir_list)):
            self.label_text.append(tkinter.StringVar())
            self.label_text[i].set(self.dir_list[i])

        for i in range(0, len(self.dir_list)):
            dir_label = tkinter.Label(textvariable=self.label_text[i], width=40, relief='solid')
            dir_label.place(x=40, y=52*(i+1))

            dir_button = tkinter.Button(self.window, text='push', command=partial(self.open_dir, i))
            dir_button.place(y=50*(i+1))

    def open_dir(self, num):
        dir_name = filedialog.askdirectory(parent=self.window, initialdir="/", title='폴더를 선택해 주세요')
        print('num', num, '  Select : ', dir_name)
        if num < len(self.dir_list):
            self.dir_list[num] = dir_name
            self.label_text[num].set(dir_name)
        else:
            pass

    def open_output_dir(self):
        dir_name = filedialog.askdirectory(parent=self.window, initialdir="/", title='폴더를 선택해 주세요')
        self.out_dir = dir_name
        for directory in self.dir_dictionary:
            string_list = directory.split('/')
            self.dir_dictionary[directory] = self.out_dir + '/' + self.folder_name + string_list[len(string_list) - 2]

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


