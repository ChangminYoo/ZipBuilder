import os
import shutil
import tkinter
from tkinter import filedialog
from tkinter import ttk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from functools import partial
import tkinter.messagebox as messagebox
import webbrowser

# 포함 되어야 할 폴더
includes = ['/Assets', '/Packages', '/ProjectSettings']

# 이동시킬 기본 폴더
move_targets = ['com.unity.sharp-zip-lib@1.2.2-preview.2',
                'Ifland AvatarEngine',
                'Ifland AvatarEngine Using ExPlugins',
                'ifland.tra@2.3.45',
                # 나중에 TReal 폴더도 추가 예정
                ]


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

    move_to = 'Packages'

    def __init__(self):
        self.dir_count = 0
        self.label_text = []  # zip path text list
        self.entry_list = []  # mover entry list - target folder to move

        self.windowWidth = 450
        self.windowHeight = 450

        self.window = ttk.Window(themename='cosmo')
        self.move_input_text = tkinter.StringVar()
        self.move_output_text = tkinter.StringVar()
        self.out_text = tkinter.StringVar(value=self.out_dir)  # zip output path text

        self.window.title("ZipBuilder")
        self.window.update()
        self.window.geometry("{}x{}+500+300".format(self.windowWidth, self.windowHeight))

        # notebook
        notebook = ttk.Notebook(self.window, width=self.windowWidth, height=self.windowHeight)
        notebook.pack()
        self.frame_zip = tkinter.Frame(self.window)
        notebook.add(self.frame_zip, text='Zipper')
        self.frame_move = tkinter.Frame(self.window)
        notebook.add(self.frame_move, text='Mover')

        # set Zipper
        for directory in self.dir_list:
            self.dir_dictionary[directory] = self.make_out_name(directory)
        self.set_zipper_gui()

        # set Mover
        for target in move_targets:
            name = tkinter.StringVar()
            name.set(target)
            self.entry_list.append(name)
        self.set_mover_GUI()

        self.window.mainloop()

    # region Zipper
    def set_zipper_frame(self):
        ttk.Label(self.frame_zip, text="디렉토리를 변경할 수 있습니다.").pack()

        input_frame = ttk.LabelFrame(self.frame_zip, text="Input", padding=(20, 10))
        input_frame.place(x=15, y=40, width=self.windowWidth - 30, height=210)

        output_frame = ttk.LabelFrame(self.frame_zip, text='Output')
        output_frame.place(x=15, y=280, width=self.windowWidth - 30, height=70)

    def set_zipper_gui(self):
        self.set_zipper_frame()

        for i in range(0, len(self.dir_list)):
            self.label_text.append(tkinter.StringVar())
            self.label_text[i].set(self.dir_list[i])

        for i in range(0, len(self.dir_list)):
            dir_label = ttk.Label(self.frame_zip, textvariable=self.label_text[i], width=45,
                                  relief='sunken', anchor=tkinter.CENTER)
            dir_label.place(x=100, y=70 * (i + 1))
            dir_button = ttk.Button(self.frame_zip, text='Path', style='Accent.TButton', width=5,
                                    command=partial(self.open_dir_zip, i, True))
            dir_button.place(x=30, y=65 * (i + 1))

        ttk.Button(self.frame_zip, text='+', width=5, command=self.add_zipper_button).place(x=370, y=252)

        out_label = ttk.Label(self.frame_zip, textvariable=self.out_text, width=40,
                              relief='sunken', anchor=tkinter.CENTER)
        out_label.place(x=130, y=312)
        output_button = ttk.Button(self.frame_zip, text='Output', width=8, style='Accent.TButton',
                                   command=partial(self.open_dir_zip, 0, False))
        output_button.place(x=28, y=307)

        start_button = ttk.Button(self.frame_zip, text='Start', width=25, command=self.make_zip)
        start_button.place(x=120, y=365)

    def add_zipper_button(self):
        index = len(self.dir_list)
        if index >= 3:
            return

        self.dir_list.append('C:/')
        self.label_text.append(tkinter.StringVar())
        self.label_text[index].set(self.dir_list[index])

        dir_label = ttk.Label(self.frame_zip, textvariable=self.label_text[index], width=45, relief='sunken',
                              anchor=tkinter.CENTER)
        dir_label.place(x=100, y=67 * (index + 1))
        dir_button = ttk.Button(self.frame_zip, text='Path', style='Accent.TButton', width=5,
                                command=partial(self.open_dir_zip, index, True))
        dir_button.place(x=30, y=65 * (index + 1))
        self.dir_dictionary[self.dir_list[index]] = self.make_out_name(self.dir_list[index])

    def open_dir_zip(self, num, is_input):
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

    # endregion

    # region Mover
    def set_mover_GUI(self):
        ttk.Label(self.frame_move, text='디렉토리를 변경할 수 있습니다.').pack()
        self.move_input_text.set('C:/')

        input_frame = ttk.LabelFrame(self.frame_move, text='Input', padding=(20, 10))
        input_frame.place(x=15, y=30, width=self.windowWidth - 30, height=280)

        input_label = ttk.Label(self.frame_move, textvariable=self.move_input_text,
                                relief='sunken', width=45, anchor=tkinter.CENTER)
        input_label.place(x=100, y=60)
        input_button = ttk.Button(self.frame_move, text='Path', style='Accent.TButton',
                                  width=5, command=partial(self.open_dir_move))
        input_button.place(x=30, y=55)

        move_label = ttk.Label(self.frame_move, text='Move List')
        move_label.place(x=30, y=(100 + (40 * len(self.entry_list) / 2)))

        for i in range(0, len(self.entry_list)):
            entry = ttk.Entry(self.frame_move, textvariable=self.entry_list[i], width=40)
            entry.place(x=100, y=110 + (i * 40))

        ttk.Button(self.frame_move, text='+', width=3, command=self.add_mover_button).place(x=390, y=312)

        move_button = ttk.Button(self.frame_move, text='Move', width=25, command=self.move_folder)
        move_button.place(x=120, y=365)

    def add_mover_button(self):
        index = len(self.entry_list)
        if index >= 5:
            return

        self.entry_list.append(tkinter.StringVar())
        self.entry_list[index].set('')

        entry = ttk.Entry(self.frame_move, textvariable=self.entry_list[index], width=40)
        entry.place(x=100, y=110 + (index * 40))

    # endregion

    def open_dir_move(self):
        dir_name = filedialog.askdirectory(parent=self.window, initialdir="/", title='폴더를 선택해 주세요')
        self.move_input_text.set(dir_name)

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

    def move_folder(self):
        print('------------ Move -------------')
        to = self.move_input_text.get() + '/' + self.move_to
        if not self.exist_path(to):
            print('Input Path Error')
            return
        for folder in self.entry_list:
            if not folder.get() == '':
                move = self.move_input_text.get() + '/Assets/' + folder.get()
                if self.exist_path(move):
                    shutil.move(move, to)
        print('------------  FINISH  ------------ ')
        webbrowser.open(to)


if __name__ == '__main__':
    ZipBuilder()
