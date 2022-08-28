# 브랜치 미설정 오류 fatal: The current branch master has no upstream branch.

## 원인

기본 브랜치 설정을 안해줘서 생기는 문제

## 해결

브랜치 설정을 해준다

```
git push --set-upstream origin master
```
