import zipfile
from zipfile import ZipFile
import os
import shutil
import gui

# 포함 되어야 할 폴더
includes = ['/Assets', '/Packages', '/ProjectSettings']

# input 디렉토리 절대경로
avatarStudioDir = 'C:/morph/AvatarStudio/StagingProject'
buildDir = 'C:/morph/BuildProject/BuildProject_DLL'
# webGLDir = 'C:/morph/WebGL Viewer'

# 산출 절대경로
output = 'C:/morph/Test'
avatarStudioOut = output + '/OpenStudio'
buildOut = output + '/Build'
# webGLOut = output + '/WebGL'

directoryDictionary = {avatarStudioDir: avatarStudioOut, buildDir: buildOut}

# 산출될 파일 이름
avatarStudioOutName = 'OpenStudio'
buildName = 'Build'
# webGLName = 'WebGL'

outputDictionary = {avatarStudioOut: avatarStudioOutName, buildOut: buildName}


def exist_path(directory):
    if os.path.isdir(directory):
        return True
    else:
        print("Not Exist ::: ", directory)
        return False


def make_zip():
    print('------------ START -------------')
    # includes 내에 속한 폴더만 복사
    for directory in directoryDictionary:
        for folder in includes:
            if exist_path(directory + folder):
                shutil.copytree(directory + folder, directoryDictionary[directory] + folder, dirs_exist_ok=True)
                print("Copy To ::: ", directoryDictionary[directory] + folder)

    # zip 변환
    print("Zipping................")
    for out in outputDictionary:
        if exist_path(output):
            filename = outputDictionary[out]
            os.chdir(output)
            shutil.make_archive(filename, 'zip', out)

    print('------------ FINISH -------------')


if __name__ == '__main__':
    gui.gui_init()
