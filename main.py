import zipfile
from zipfile import ZipFile
import os
import shutil
import tkinter
from tkinter import filedialog
from functools import partial
import tkinter.messagebox as messagebox

# 포함 되어야 할 폴더
includes = ['/Assets', '/Packages', '/ProjectSettings']

# input 디렉토리 절대경로
dir0 = 'C:/morph/AvatarStudio/StagingProject'
dir1 = 'C:/morph/BuildProject/BuildProject_DLL'

# 산출될 파일 이름
outName0 = 'OpenStudio'
outName1 = 'Build'

# 산출 절대경로
output = 'C:/morph/Result'
out0 = output + '/' + outName0
out1 = output + '/' + outName1

dir_list = [dir0, dir1]  # input 디렉토리 리스트
directoryDictionary = {dir0: out0, dir1: out1}


def exist_path(directory):
    if os.path.isdir(directory):
        return True
    else:
        print("Not Exist ::: ", directory)
        return False


class ZipBuilder:
    window = tkinter.Tk()
    dir_count = 0
    label_text = []

    def __init__(self):
        self.window.title("ZipBuilder")
        self.window.geometry("350x300+100+100")

        top_label = tkinter.Label(text='디렉토리 경로를 변경할 수 있습니다.', width=40, relief='solid', fg='red')
        top_label.pack()

        start_button = tkinter.Button(self.window, text='Start', width=25, command=self.make_zip)
        start_button.place(x=80, y=250)

        for i in range(0, len(dir_list)):
            self.label_text.append(tkinter.StringVar())
            self.label_text[i].set(dir_list[i])

        #plus_button = tkinter.Button(self.window, text='+', width=20, command=self.add_button)
        #plus_button.pack()

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
        for i in range(0, len(dir_list)):
            dir_label = tkinter.Label(textvariable=self.label_text[i], width=40, relief='solid')
            dir_label.place(x=40, y=52*(i+1))

            dir_button = tkinter.Button(self.window, text='push', command=partial(self.open_dir, i))
            dir_button.place(y=50*(i+1))

    def open_dir(self, num):
        dir_name = filedialog.askdirectory(parent=self.window, initialdir="/", title='폴더를 선택해 주세요')
        print('num', num, '  Select : ', dir_name)
        if num < len(dir_list):
            dir_list[num] = dir_name
            self.label_text[num].set(dir_name)
        else:
            dir_list.append(dir_name)
            input_label = tkinter.Label(self.window, text=dir_name, width=35, relief='solid')
            input_label.pack()

            directoryDictionary[dir_name] = num
            output_label = tkinter.Label(self.window, text=dir_name, width=35, relief='solid')
            output_label.pack()

    def make_zip(self):
        print('------------ START -------------')
        # includes 내에 속한 폴더만 복사
        for directory in directoryDictionary:
            for folder in includes:
                if exist_path(directory + folder):
                    shutil.copytree(directory + folder, directoryDictionary[directory] + folder, dirs_exist_ok=True)
                    print("From : ", directory + folder, "    =====>    Copy To : ", directoryDictionary[directory] + folder)

        # zip 변환
        print("Zipping................")
        for out in directoryDictionary:
            filename = directoryDictionary[out]
            os.chdir(output)
            if exist_path(out):
                shutil.make_archive(filename, 'zip', out)

        print('------------ FINISH -------------')

        tkinter.messagebox.showinfo('완료', '완료 했습니다.')
        self.window.destroy()
        self.window.quit()


if __name__ == '__main__':
    # make_zip()
    ZipBuilder()
