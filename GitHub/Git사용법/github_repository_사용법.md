# GitHub repository 사용법

1. GitHub 홈페이지에서 클론하고자 하는 repository로 간다
2. 클론하고자 하는 repository의 URL 주소 복사
3. 터미널로 가서 repository파일을 보관할 디렉터리로 이동한다.
4. `git clone repository-url` 입력 (repository-url = 복사한 URL)

# GitHub 사용법

### 1. git 설치

```
brew install git
```

### 2. 파일 생성

- 작업 파일을 저장할 파일을 생성

### 3. git 저장소 생성

- 터미널을 켜고 생성한 파일 디렉터리로 이동 후 아래 명령어로 저장소 생성

```
git init
```

### 4. 스테이징

```
git add 파일명
git add .       //현재 폴더의 모든 파일을 스테이징
```

### 5. 커밋

```
git commit -m "커밋 메시지"
git commit -a
```

### 6. 푸쉬

```
git push
```
