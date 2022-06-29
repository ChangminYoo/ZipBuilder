import os
import tkinter
from tkinter import filedialog
from tkinter import ttk
import ttkbootstrap
import tkinter.messagebox as messagebox
import os
import webbrowser

class BatchBuilder:
    default_unity_path = 'C:/Program Files/Unity/Hub/Editor/'
    batch_file = r'.bat'
    build_dir = '/Build/'
    targets = ['win64', 'android', 'ios', 'webgl']

    def __init__(self):
        self.combobox = None
        self.window = ttkbootstrap.Window(themename='journal')
        self.unity_dir_text = tkinter.StringVar()
        self.project_dir_text = tkinter.StringVar()

        self.gui_init()

    def run_batch_file(self):
        self.write_batch_file()
        os.system(self.batch_file)

        print("-------------------Complete Build!!--------------------")

        webbrowser.open(self.project_dir_text.get() + self.build_dir)
        tkinter.messagebox.showinfo('완료', '완료 했습니다.')
        self.window.destroy()
        self.window.quit()

    def write_batch_file(self):
        print("-------------------Start Build--------------------")

        self.batch_file = \
            [file for file in os.listdir(self.project_dir_text.get()) if file.endswith(self.batch_file)][0]

        os.chdir(self.project_dir_text.get())
        with open(self.batch_file, 'w') as file:
            w = '"' + self.unity_dir_text.get().replace('/', '\\') + '"'
            w += ' -quit -batchmode'
            w += ' -buildTarget ' + self.combobox.get().replace('/', '\\')
            w += ' -projectPath ' + '"' + self.project_dir_text.get().replace('/', '\\') + '"'
            w += ' -executeMethod ' + '"Build.AutoBuild"'
            w += ' -logFile ' + '"' + self.project_dir_text.get().replace('/', '\\') + '\\Build\\build_log.log' + '"'
            file.write(w)
            print("Write Complete ::: " + self.batch_file)

    def open_dir(self):
        dir_name = filedialog.askdirectory(parent=self.window, initialdir="C:/", title='폴더를 선택해 주세요')
        self.project_dir_text.set(dir_name)

    def open_file(self):
        filename = filedialog.askopenfilename(initialdir=self.default_unity_path, title='유니티 실행파일을 선택해 주세요',
                                              filetypes=[('응용 프로그램', '*.exe')])
        print(filename)
        self.unity_dir_text.set(filename)

    def gui_init(self):
        self.window.title("UnityBatchBuilder")
        self.window.geometry("400x300+300+300")

        # Unity 경로
        unity_path_label = ttk.Label(self.window, text='유니티 경로를 설정해 주세요.')
        unity_path_label.place(x=110, y=20)
        unity_dir_button = ttk.Button(self.window, text='path', command=self.open_file, width=8, style="Accent.TButton")
        unity_dir_button.place(x=5, y=40)
        unity_dir_label = ttk.Label(self.window, textvariable=self.unity_dir_text, width=40, relief='sunken')
        unity_dir_label.place(x=100, y=45)

        # 빌드 할 프로젝트 경로
        build_path_label = ttk.Label(self.window, text='빌드 경로를 설정해 주세요.')
        build_path_label.place(x=110, y=85)
        project_dir_button = ttk.Button(self.window, text='path', command=self.open_dir, width=8, style="Accent.TButton")
        project_dir_button.place(x=5, y=110)
        project_dir_label = ttk.Label(self.window, textvariable=self.project_dir_text, width=40, relief='sunken')
        project_dir_label.place(x=100, y=115)

        # 빌드 타겟 설정
        build_target_label = tkinter.Label(self.window, text='빌드 타겟을 선택해 주세요.', width=40)
        build_target_label.place(x=50, y=155)

        self.combobox = ttk.Combobox(self.window, state='readonly', height=5, values=self.targets)
        self.combobox.set('webgl')
        self.combobox.place(x=120, y=190)

        start_button = ttk.Button(self.window, text='Build', width=25, command=self.run_batch_file)
        start_button.place(x=100, y=250)

        self.window.mainloop()


if __name__ == '__main__':
    BatchBuilder()
