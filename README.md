# ZipBuilder

## 설정 변수값
 - 포함 되어야 할 폴더 : '/Assets', '/Packages', '/ProjectSettings'
 - input 폴더 경로 : 'C:/morph/AvatarStudio/StagingProject' , 'C:/morph/BuildProject/BuildProject_DLL'
 - output 폴더 경로 : 'C:/morph/Result'
 - output 이름 : OpenStudio, Build

 디렉토리 추가시 각 input/output dictionary에도 추가 필요
 
## 목표
 프로젝트 빌드 간소화 / 자동화를 위한 프로그램 개발.

 여러 프로젝트에 적용이 쉽도록 유틸성 높이도록 수정 필요.
 
## 실행파일 생성
프로젝트 경로 터미널에서 명령어 실행 
1. pip install pyinstaller  (처음에만)
2. pyinstaller --onfile main.py
