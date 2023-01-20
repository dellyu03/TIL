# HTML 문서와 자바스크립트 파일 연결하기

> ### [1. Inline 방식](#1-inline-ebb0a9ec8b9d-1)  
> ### [2. script 태그로 HTML문서 안에 자바스크립트 코드 작성](#2-script-ed839ceab7b8eba19c-htmlebacb8ec849c-ec9588ec9790-ec9e90ebb094ec8aa4ed81aceba6bded8ab8-ecbd94eb939c-ec9e91ec84b1-1)
> ### [3. HTML에 외부 자바스크립트 파일 연결](#3-htmlec9790-ec99b8ebb680-ec9e90ebb094ec8aa4ed81aceba6bded8ab8-ed8c8cec9dbc-ec97b0eab2b0-1)

<br>


## 1. Inline 방식
> #### HTML 태그에 직접 자바스크립트 코드를 작성
- HTML 문서안에 있는 자바스크립트 코드가 필요한 태그안에 직접 자바스크립트 코드를 작성

```HTML
<!DOCTYPE html>
<html>
<body>
    <button type="button" onclick="alert('Hello!')"/>안녕하세요!</button>
</body>
</html>
```

> #### 장점 : 태그에 연관된 스크립트가 분명하게 드러남
> #### 단점 : 정보와 제어가 섞여 있기 때문에 정보로서의 가치가 떨어짐

<br>

## 2. script 태그로 HTML문서 안에 자바스크립트 코드 작성
> #### HTML 문서 내부 script 태그에  자바스크립트 코드를 작성

## 2-1 
- HTML 문서에 script 태그 안에 필요한 자바스크립트 코드를 작성함

```HTML
<!DOCTYPE html>
<html>
<body>
    <button id = "greeting">안녕하세요!</button>
    <script type="text/javascript">
        var greet = document.getElementById('greeting');
        greet.addEventListener('click', function(){
            alert('안녕하세요');
        })
    </script>
</body>
</html>
```
<br>

## 2-2

<br>

## 3. HTML에 외부 자바스크립트 파일 연결
> #### HTML문서 내부가 아닌 외부에서 작성한 파일을 HTML 문서에 연결

- 필요한 자바스크립트 코드를 외부 js 파일에 저장한 후 HTML 파일에 해당 자바스크립트 파일을 연결하는 방식

HTML 파일
```HTML
<!DOCTYPE html>
<html>
<body>
    <input type="button" id="hw" value="Hello world" />
    <script type="text/javascript" src="script2.js"></script>
</body>
</html>
```


js 파일
```js
var hw = document.getElementById('hw');
hw.addEventListener('click', function(){
    alert('Hello world');
})
```