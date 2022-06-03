import zipfile
from zipfile import ZipFile
import tkinter
import os
import shutil

# 포함 되어야 할 폴더
includes = ['/Assets', '/Packages', '/ProjectSettings']

# input 디렉토리 절대경로
avatarStudioDir = 'C:/morph/AvatarStudio/StagingProject'
buildDir = 'C:/morph/BuildProject/BuildProject_DLL'
#webGLDir = 'C:/morph/WebGL Viewer'

# 산출 절대경로
output = 'C:/morph/Test'
avatarStudioOut = output + '/OpenStudio'
buildOut = output + '/Build'
#webGLOut = output + '/WebGL'

directoryDictionary = {avatarStudioDir: avatarStudioOut, buildDir: buildOut}

# 산출될 파일 이름
avatarStudioOutName = 'OpenStudio'
buildName = 'Build'
#webGLName = 'WebGL'

outputDictionary = {avatarStudioOut: avatarStudioOutName, buildOut: buildName}

def existPath(directory):
    if os.path.isdir(directory):
        return True
    else:
        print("Not Exist ::: ", directory)
        return False

def makeZip():
    print('------------ START -------------')
    # includes에 속한 폴더만 복사
    for directory in directoryDictionary:
        # if directory == buildDir:
        #    includes.append('/Library')
        for folder in includes:
            if existPath(directory + folder):
                shutil.copytree(directory + folder, directoryDictionary[directory] + folder, dirs_exist_ok=True)
                print("Copy To ::: ", directoryDictionary[directory] + folder)

    # zip으로 변환
    print("Zipping................")
    for out in outputDictionary:
        filename = outputDictionary[out]
        os.chdir(output)
        shutil.make_archive(filename, 'zip', out)

    print('------------ FINISH -------------')

def guiInit():
    window = tkinter.Tk()

    window.title("ZipBuilder")
    window.geometry("300x300+100+100")

    startButton = tkinter.Button(window, text='Start', width=20, overrelief='solid', command=makeZip)
    startButton.place(x=80, y=100)

    window.mainloop()

if __name__ == '__main__':
    guiInit()
