# Git 시작 하기

## Git이란?

2005년에 리누스 토르발스가 개발한 분산 버전 관리 시스템

-> 파일의 변경 사항을 저장하고 관리해주는 시스템

### 깃으로 할 수 있는것

- 버전관리
- 백업
- 협업

## git 설치

> 윈도우 버전

- 깃 홈페이지 접속해서 설치 https://git-scm.com/

> MAC 버전

- 깃 홈페이지 접속해서 설치
- HomeBrew로 설치
  - HomeBrew가 설치 되어 있다면 터미널에서 아래 명령어 입력

```
brew install git
```

## git 환경 설정

- 깃에 사용자 정보 추가

```
git config --global user.name "UserName"
git config --global user.email "UserEmail"
```

- 예시

```
git config --global user.name "Delyugam"
git config --global user.email "seunghwan081@gmail.com"
```
