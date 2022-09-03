# CSS 정리 노트 part 1

## 목차

---

[0. CSS란](#0-css란)

[I. CSS 기본 문법](#i-css-기본-문법)  
　　[1. CSS 기본 구성](#1-css-기본-구성)  
　　[2. 선택자](#2-선택자)  
　　[3. Cascade](#3-cascade)

[II. HTML에 CSS 적용하는 법](#ii-html에-css-적용하는-법)

[III. 텍스트, display, border](#iii-텍스트-display-border)  
　　[1. 텍스트 속성](#1-텍스트-속성)  
　　[2. display 속성](#2-display-속성)  
　　[3. border 속성](#3-border-속성)

[IV. 박스 모델](#iv-박스-모델)  
　　[1.박스 모델의 구성](#1-박스-모델의-구성)  
　　[2. 박스 모델 각 영역의 크기 조절](#2-박스-모델-각-영역의-크기-조절)  
　　[3. box-sizing](#3-box-sizing)  
　　[4. background](#4-background)

[V. float과 clear](#v-float과-clear)

[VI. position](#vi-position)  
　　[1. relative](#1-relative)  
　　[2. absolute](#2-absolute)  
　　[3. fixed](#3-fixed)  
　　[4. sticky](#4-sticky)

[VII. 상속](#vii-상속)

---

## 0. CSS란?

<p></p>

## I. CSS 기본 문법

### 1. CSS 기본 구성

```CSS
선택자　{
　속성명:　속성값;
}

/*예시 코드*/
div{                    /*div 태그에*/
  display: flexbox;     /*display 속성을 flexbox로 한다.*/
}
```

- 선택자 : 어떤 요소에 스타일을 적용할지
- 속성명 : 어떤 스타일을 정의하고 싶은지
- 속성값 : 어떻게 정의하고 싶은지

### 2. 선택자

- 태그 선택자 : tag{} &nbsp; - 특정 태그를 선택
- id 선택자 : #id{} &nbsp; - 특정 아이디를 선택
- 클래스 선택자 : .class{} &nbsp; - 특정 클래스 선택
- 전체 선택자 : \*{}

### 3. Cascade

<p>CSS는 계단식으로 동작함 같은 태그의 같은 속성을 변화시키는 두개의 CSS가 존재 할 경우 나중에 나온 명령을 따름(초기 명령을 덮어 씀)</p>

---

## II. HTML에 CSS 적용하는 법

- ### 인라인 스타일
  &nbsp; 태그에 바로 스타일 속성을 적용 하는 방법

```HTML
<p style ="color blue;">
    텍스트를 푸른색으로 표시하기
</p>
```

- ### 스타일 태그
  &nbsp; HTML 문서 안에 style 태그를 추가하여 작성하는 방법

```HTML
<style>
    p{color: red;}
</style>
```

- ### 문서간의 연결
  CSS 파일을 생성 후 HTML 파일에 연결하는 방법

```HTML
<linkh rel = "stylesheet" href = "./style.css">
```

head 태그 안에 작성 해야 함

---

## III. 텍스트, display, border

### 1. 텍스트 속성

- #### font-family
- #### font-size

- #### text -align

- #### color

### 2. display 속성

- #### block
  &nbsp; &nbsp; &nbsp; 속한 영역의 너비를 모두 차지하는 블록을 형성
- #### inline
  &nbsp; &nbsp; &nbsp; 필요한 만큼의 영역을 차지 (width와 height를 지정해 줄수 없음)
- #### inline-block
  &nbsp; &nbsp; &nbsp; inline 속성을 가지면서 width와 height를 지정할 수 있음
- #### none
  &nbsp; &nbsp; &nbsp; 요소를 표시 하지 않음
  ```CSS
  p{
    display: block;
  }
  ```

### 3. border 속성

```CSS
span{border: 2px solid green;} /*한번에 여러 속성을 지정해 줄 수 있는 "단축 속성"*/
```

- #### border-color : 색상 지정 (RGB값, 색상 이름등)
- #### border-width : 경계선의 두께 (thin, medium, none 외 px, em, rem 등의 단위)
- #### border-style : 경계선의 스타일 지정 (none, solid, dotted, dashed 등)

---

## IV. 박스 모델

### 1. 박스 모델의 구성

> 콘텐츠 영역 (content)
>
> > 안쪽 여백 (padding)
> >
> > > 경계선 (border)
> > >
> > > > 바깥쪽 여백(margin)

### 2. 박스 모델 각 영역의 크기 조절

- <h4> content :</h4> <p>&nbsp; width, height로 조절 가능</p>

```CSS
h1{
  width: 100px;
  heigh: 200px;
}
```

- <h4>padding :</h4> <p>&nbsp; padding -top, right, bottom, left</p>
- <h4>border :</h4> <p>&nbsp; border-width</p>
- <h4>margin :</h4> <p>&nbsp; margin - top, right, bottom, left</p>

```CSS
h1{
  margin-top : 100px;
  margin : 100px; 20px; /*위 아래 :100px, 좌우: 20px */
  padding : 20px 10px 30px 50px; /*순서대로 위, 오른쪽, 아래, 왼쪽의 패딩값 적용*/
}
```

### 3. box-sizing

<p>&nbsp; &nbsp; &nbsp; 기본적으로 with와 height는 content 영역만의 크기만 계산하기 때문에 　　padding과 border에 의해 요소의 크기가 달라질 수 있다. box-sizing을 통해 　　요소의 너비와 높이를 계산하는 방법을 달리하여 이를 방지할 수 있다.</p>

```CSS
/*요소의 너비와 높이를 계산하는 방법을 지정함*/
content-box : 기본값, 높이와 너비가 콘텐츠 영역만을 포함
border-box : 너비와 높이가 안쪽 여백과 테두리를 포함

ex)
div{
  box-sizing : border-box;
}
```

---

### 4. background

<p>　 　콘텐츠의 배경을 정의, 단축속성으로써 색상, 이미지, 반복등을 정의 할 수 있음</p>

```CSS
background-color        /*배경 색을 지정*/
background-image        /*배경 이미지를 지정*/
background-position     /*배경 이미지의 초기 위치를 지정*/
background-size         /*배경 이미지의 크기 지정*/
background-repeat       /*배경 이미지의 반복 방법 지정*/
```

---

## V. float과 clear

- ### float
<p>　　요소가 일반적인 문서 흐름에서 제외 되어 컨테이너의 왼쪽이나 오른쪽에 <br>　　배치되도록 함(흐름에서 제외되나 공간은 차지함)</p>

```CSS
float : none; /*원래 상태, 기본값*/
float : left; /*부모 박스의 왼편*/
float : right; /*부모 박스의 오른편*/
```

- ### clear

<p>　　float 이후의 요소가 float 요소의 아래로 내려가도록 함</p>

```CSS
clear : none; /*기본값*/
clear : left; /*float : left 요소 아래로*/
clear : right; /*float : right 요소 아래로*/
clear : both; /*float : left, float:right 요소 아래로*/
```

---

### VI. position

<p>　문서 상에 요소를 배치하는 방법을 정의 한다.</p>

```CSS
static      /*기본값, 일반적인 문서 흐름*/

relative    /*일반적인 문서흐름에 배치 하되, 상하좌우 위치값에 따라 오프셋 적용*/

absolute    /*일반적인 문서흐름에서 제거, 상위 요소중 가까운 position 지정 요소에 대해 상대적으로 오프셋 적용*/

fixed       /*일반적인 문서흐름에서 제거, 지정한 위치에 고정*/

sticky      /*일반적인 문서흐름에 따라 배치,
            스크롤 되는 가장 가까운 상위 요소에 대해 오프셋 적용 */
```

<p>오프셋 : 위치를 얼마만큼 이동 시키나</p>
<h3><p>예시</p></h3>

#### 1. relative

```CSS
/*relative: 원래 위치(문서 흐름상의 위치)보다 위에서부터 100px,
왼쪽에서부터 100px 떨어지도록 배치*/
div {
  position : relative;
  top : 100px; left: 100px;
}
```

#### 2. absolute

```CSS
/*absolute :일반적인 문서 흐름을 제거 하고
position 속성값이 적용된 상위 요소중 가장 가까운
상위요소를 기준으로 오프셋 적용(position 지정 요소가 없으면
브라우저 화면을 기준으로 오프셋 적용)*/

div{
  position : absolute;
  top : 50px; left: 50px;
}

/*상위 요소인 body가 position 지정 요소이므로 body를 기준으로 오프셋 적용*/
HTML

body{
  position : relative;
}
div {
  position : absolute;
}
<body>
  <div></div>
</body>
```

#### 3. fixed

```CSS
/*fixed : 문서 흐름 제거, 위치 고정
예시의 경우 위에서부터 50px, 왼쪽에서부터 50px에 고정*/
div {
  position : fixed;
  top : 50px; left : 50px;
}
```

#### 4. sticky

```CSS
/*sticky : 요소를 일반적인 문서흐름에 따라 배치, 스크롤 되는 가장 가까운
상위 요소에 대해 오프셋 적용
=>일반적으로 문서의 흐름을 따라가되 스크롤에 따라 지정된 위치에 도달하면
 그자리에 고정*/

div{
  position: sticky;
  top: 50px; left: 50px;
}

/*body 요소가 스크롤 되면서 div 요소가 body 기준으로 위에서부터 0px에
도달 하게 되면 그 자리에 고정*/
HTML

div {
  position : sticky;
  top : 0px;
}
<body>
  <div></div>
</body>
```

---
