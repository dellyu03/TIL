# 브랜치 미설정 오류 fatal: The current branch master has no upstream branch.

## 원인

기본 브랜치 설정을 안해줘서 생기는 문제

## 해결

브랜치 설정을 해준다

```
git push --set-upstream origin master
```

#### 새 브랜치를 만들 때마다 설정하기 번거롭기 때문에 아래 명령어를 통해 브랜치 설정 명령어 생략

```
git config --global push.default current
```
