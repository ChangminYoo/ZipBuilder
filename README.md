## 목표
 프로젝트 빌드 간소화 / 자동화를 위한 프로그램 개발.

 여러 프로젝트에 적용이 쉽도록 유틸성 높이도록 수정 필요.

# zipbuilder
push 버튼으로 input 경로 지정, 산출 경로 지정 후 Start 버튼으로 시작.

## 설정 변수값
 코드 수정 필요 
 - 포함 되어야 할 폴더 : '/Assets', '/Packages', '/ProjectSettings'
 - input의 추가 및 제거
 - output의 상위 폴더이름

 경로 수정 가능
 - input 경로
 - output 경로

# unity-batchbuilder
1. 프로젝트에 .bat 파일 생성
2. 프로그램 실행
3. 버튼으로 현재 프로젝트 버전의 유니티 경로, 프로젝트 경로 지정, 
빌드 타겟 선택후 Build 버튼으로 시작


# 파워쉘에서 파이썬 프로그램 실행 방법
해당 경로에서 파워쉘 실행후 명령어 실행(파이썬 설치 필요)
py -3 이름.py
 
# 파이썬 실행파일 생성 방법
프로젝트 경로 쉘에서 명령어 실행
1. pip install pyinstaller  (처음에만)
2. pyinstaller --onfile 이름.py

