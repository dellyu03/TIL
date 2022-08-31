# .gitignore

- git 버전관리에서 제외할 파일을 지정함
- 공개하면 안되는 정보 들을 .gitignore 파일을 이용해서 public으로 공개된 GitHub 저장소에서 표시되지 않도록 할 수 있음

## .gitignore 설정

- 프로젝트 파일에서 .gitignore 생성
- 파일에 제외하고자 하는 파일의 이름을 입력

## gitignore 파일 규칙

- #: 주석
- /fileN : 현재 폴더 중에 fileN이란 파일 안에 있는 모든 파일 ignore
- fileN/ : 프로젝트 전체 폴더 중에 fileN이란 파일 안에 있는 모든 파일 ignore
- doc/\*.txt : 현재 폴더 중에 doc 폴더 바로 밑에 있는 .txt 확장자 파일 ignore
- doc/\*_/_.pdf : 현재 폴더 doc 폴더 하위의 모든 .pdf 확장자 파일 ignore

## .gitignore 관련 추가 명령어

- ignore 한 파일이 changes에 계속 뜰 때  
  깃의 캐시가 문제 되어 생기는 문제이기 때문에 아래 명령어로 캐시를 삭제해준다.

```
git rm -r --cached .  //현재 디렉토리의 캐시 삭제
```
