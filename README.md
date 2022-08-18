# Introduction

내일배움캠프 팀 f4의 머신러닝 프로젝트 저장소입니다.

Welcome to the teamf4_mlp wiki!

![169920346-d6bff1f3-23b5-4cbb-bff1-1c31492e0532](https://user-images.githubusercontent.com/97969957/169922205-7db05bcc-9268-40c6-a816-6da3f0e8ef3b.png)

내일배움캠프 AI 2기 팀 F4의 프로젝트 기록을 담은 깃허브 위키페이지입니다!

# 🤹‍♀️ 팀 구성원

### 👨‍💻 김태인 [블로그 링크](https://velog.io/@kti0940)

### 👨‍💻 김희정 [블로그 링크](https://khjhj3808.tistory.com/)

### 👨‍💻 한예슬 [블로그 링크](https://velog.io/@tasha_han_1234)

### 👨‍💻 황영상 [블로그 링크](http://velog.io/@migdracios)

# 📌 프로젝트 AI\_카멜레온!

- AI 카멜레온은 사용자가 사진을 업로드하면 세그멘테이션을 통해 사물을 분리하고, 분리된 사물을 각각의 알록달록한 GIF로 만들어주는 웹입니다.
- 셀피를 업로드하여, 세그멘테이션을 통해 뒷배경색을 지정된 컬러 팔레트로 변경하게 됩니다.
- 지정된 여러 개의 색 팔레트 이미지를 모두 출력하여 gif로 생성합니다.
- 생성된 사진은 다운로드하는 것으로 소장할 수 있습니다!

# 기술 스택

## 백엔드

<div style="display:flex">
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white">
    <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=Flask&logoColor=white">
</div>

## 프론트엔드

<div style="display:flex">
    <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=JavaScript&logoColor=white">
    <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=HTML5&logoColor=white">
    <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=CSS3&logoColor=white">
</div>

## 데이터베이스

<img src="https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=MongoDB&logoColor=white">
  
## 머신러닝

<div style="display:flex">
    <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=PyTorch&logoColor=white">
    <img src="https://img.shields.io/badge/scikit-learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white">
</div>

# 프로젝트 구조

- 서버 사이드 렌더링으로 되어있으며, EC2로 배포했었습니다.

# 서비스 플로우

## 사진 업로드

- 사용자는 업로드 버튼을 클릭해 사진을 업로드할 수 있습니다.
- 업로드한 사진은 세그멘테이션 머신러닝을 통하여 GIF 변환작업을 시작합니다.
- 사진 변환이 완료되면, 사진을 다운로드 할 수 있는 페이지로 이동합니다.

## 사진 다운로드

- 변환이 완료된 사진은 다운로드 페이지에서 확인할 수 있습니다.
- 사용자는 다운로드 버튼을 클릭하여 다운로드 할 수 있습니다.

# 🔥[Starting Assginment](https://github.com/tunEmvegnomb/ai_chameleon/wiki)
