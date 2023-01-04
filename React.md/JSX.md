# JSX

## JSX?

- JSX(Jaca Script XML) : Jaca Script에 XML을 추가해 확장한 문법
- JSX는 리액트 엘리멘트를 생성함

```JSX
const element = <h1>Hello, world!</h1>;
```

위의 예시처럼 마치 html 과 자바스크립트 문법이 혼용된것 처럼 생김

## JS 공식 문법은 아니다
- 리액트 프로젝트를 개발할때 사용되므로 공식적인 자바스크립트 문법은 아님

## JSX에 표현식 포함하기
```js
const name = "DELYUGAM";
const element = <h1>Hello, {name}</h1>;
```
- JSX는 위처럼 자바스크립트의 거의 모든 표현식을 