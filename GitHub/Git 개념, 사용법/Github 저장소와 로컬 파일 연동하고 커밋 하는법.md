# Github 저장소와 로컬 파일 연동하고 커밋 하는법

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

## git clone

## 깃허브 저장소와 로컬 파일 연동

1.git 초기화

```
git init
```

2. 저장소 연결

```
git remote add origin "repository URL"   //연동할 저장소의 URL
```
