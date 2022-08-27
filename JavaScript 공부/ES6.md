# ES6

## ES6?

- ES : ECMAScript의 약자로 자바스크립트의 표준, 규격
- ES6 는 6번째로 출시된 ECMAScript
  <br></br>

## Index

---

[1. 템플릿 문자열](#1-템플릿-문자열)  
[2. 전개 연산자](#2-전개-연산자)  
[3. 가변변수](#3-가변-변수)

---

<br></br>

## 1. 템플릿 문자열

### 기존 자바스크립트 문자열 연결(ES6 이전)

병합 연산자(+)를 사용하여 문자열과 문자열 혹은 문자열과 변수를 연결함

```javascript
var string1 = " hello";
var string2 = " nice to meet you";
var person = { name: "Tom", job: "student" };

var greet = string1 + " " + string2;
//결과값 : hello nice to meet you

var introduce = "my name : " + person.name + " my job : " + person.job;
//결과값 : 'my name : Tom my job : student'
```

여러 문자열과 변수들을 합칠 경우 코드가 복잡해 보임

### 템플릿 문자열(ES6)

- 템플릿 문자열을 통해 코드를 좀더 보기 쉽게 작성 할 수 있다.
  - 템플릿 문자열에서 문자열 전체를 `(백틱)으로 감싸고 문자열 중간에 ${}을 통해 변수를 포함 할 수 있음

```javascript
var string1 = "hello";
var string2 = "nice to meet you";
var person = { name: "Tom", job: "student" };

var greet = `${string1} ${string2}`;
// 결과값 : hello nice to meet you

var introduce = `my name : ${person.name} my job : ${person.job}`;
// 결과값 : 'my name : Tom my job : student'
```

## 2. 전개 연산자

### 기존자바스크립트 배열 조작(ES6 이전)

배열 요소들을 잘라내거나 연결하려면 인덱싱을 한후 내장 함수를 사용하여야 했음

```

```

### ES6 배열 조작

```

```

## 3. 가변 변수
