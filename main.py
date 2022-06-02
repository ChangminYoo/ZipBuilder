import zipfile
from zipfile import ZipFile
import os
import shutil

# Directory Path
dirPath = 'C:/morph/'
inputPath = 'AvatarStudio/StagingProject'
includes = ['/Assets', '/Packages', '/ProjectSettings']
outputPath = 'test.zip'

def zipFilesInDir():
    owd = os.getcwd()  # 현재 working directory를 기록
    os.chdir(dirPath)  # 압축 파일 생성할 폴더로 working directory 를 이동
    zipObj = ZipFile(outputPath, 'w')

    for folderName, subfolders, filenames in os.walk(inputPath):
        zipObj.write(folderName, compress_type=zipfile.ZIP_DEFLATED)
        for filename in filenames:
            zipObj.write(os.path.join(folderName, filename), compress_type=zipfile.ZIP_DEFLATED)

    os.chdir(owd)
    zipObj.close()

def zipFilesInDir2():
    pass

if __name__ == '__main__':
    out = 'C:/morph/Test'

    avatarStudioDir = 'C:/morph/AvatarStudio/StagingProject'
    buildDir = 'C:/morph/BuildProject/BuildProject_DLL'
    webGLDir = 'C:/morph/WebGL Viewer'

    avatarStudioOut = out + '/OpenStudio'
    buildOut = out + '/Build'
    webGLOut = out + '/WebGL'

    for folder in includes:
        shutil.copytree(avatarStudioDir + folder, avatarStudioOut + folder)
        shutil.copytree(buildDir + folder, buildOut + folder)

    filename = 'Test'
    os.chdir('C:/morph')
    shutil.make_archive(filename, 'zip', out)