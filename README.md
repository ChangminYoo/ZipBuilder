# 목표
 프로젝트 빌드 간소화 / 자동화를 위한 프로그램 개발.

 여러 프로젝트에 적용이 쉽도록 유틸성 높이도록 수정 필요.

# aop-cicd
## 1. mover
Input, Output 경로 지정, 산출 폴더 이름 설정 후 Move 버튼으로 시작.
FolderList 에 있는 폴더들을 Packages 폴더 내로 이동시킨다.

## 2. zipper
push 버튼으로 input 경로 지정, 산출 경로 지정 후 Start 버튼으로 시작.

설정 변수값
 - 포함 되어야 할 폴더 : '/Assets', '/Packages', '/ProjectSettings' -> 변경시 코드 수정 필요
 - input의 추가 및 제거
 - output의 상위 폴더이름

# unity-batchbuilder
1. 프로젝트에 .bat 파일 생성
2. 프로그램 실행
3. 버튼으로 현재 프로젝트 버전의 유니티 경로, 프로젝트 경로 지정, 
빌드 타겟 선택후 Build 버튼으로 시작
