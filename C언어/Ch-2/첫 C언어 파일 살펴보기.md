# 첫 C언어 파일 살펴보기

```C
#include <stdio.h>

int main (void)
{
    printf("Hello World!");
    return 0l
}
```

## 1. #include <stdio.h>

- **#** 으로 시작하는 문장은 C언어의 **전처리기** 부분

- **#include** : 소스코드 안 특정 파일(headerfile)을 현재 위치에 포함시키는 전처리기
- **stdio.h** : 입출력 함수에 관련된 정보를 가지고 있음

## 2. int main (void)

- main 함수를 지정 하는 문장
- **main 함수** : C언어 프로그램중에서 가장 처음으로 시작되는 함수
- **int main (void)** : main 함수를 지정화되 출력값은 int형, 입력값은 void(없음)
