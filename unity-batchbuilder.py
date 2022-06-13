import tkinter
from tkinter import filedialog
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox
import os
import webbrowser
import pathlib

class BatchBuilder:
    default_unity_path = 'C:/Program Files/Unity/Hub/Editor/'
    batch_file = r'.bat'
    build_dir = '/Build/'

    def __init__(self):
        self.combobox = None
        self.window = tkinter.Tk()
        self.unity_dir_text = tkinter.StringVar()
        self.project_dir_text = tkinter.StringVar()

        self.gui_init()

    def run_batch_file(self):
        self.write_batch_file()
        os.system(self.batch_file)

        print("-------------------Complete Build!!--------------------")

        webbrowser.open(self.project_dir_text.get()+self.build_dir)
        tkinter.messagebox.showinfo('완료', '완료 했습니다.')
        self.window.destroy()
        self.window.quit()

    def write_batch_file(self):
        print("-------------------Start Build--------------------")

        self.batch_file =\
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
        self.window.geometry("350x300+100+100")

        # Unity 경로
        tkinter.Label(self.window, text='유니티 경로를 선택해 주세요.', width=40).pack()
        unity_dir_button = tkinter.Button(self.window, text='path', command=self.open_file)
        unity_dir_button.place(y=18)
        unity_dir_label = tkinter.Label(self.window, textvariable=self.unity_dir_text, width=35, relief='sunken')
        unity_dir_label.pack()

        # 빌드 할 프로젝트 경로
        tkinter.Label(self.window, text='빌드 경로를 설정해 주세요.', width=40).pack()
        project_dir_button = tkinter.Button(self.window, text='path', command=self.open_dir)
        project_dir_button.place(y=60)
        project_dir_label = tkinter.Label(self.window, textvariable=self.project_dir_text, width=35, relief='sunken')
        project_dir_label.pack()

        # 빌드 타겟 설정
        tkinter.Label(self.window, text='빌드 타겟을 설정해 주세요.', width=40).pack()
        values = ['win64', 'android', 'ios', 'webgl']
        self.combobox = ttk.Combobox(self.window, height=5, values=values)
        self.combobox.set('webgl')
        self.combobox.pack()

        start_button = tkinter.Button(self.window, text='Build', width=25, command=self.run_batch_file)
        start_button.place(x=80, y=250)

        self.window.mainloop()


if __name__ == '__main__':
    BatchBuilder()
