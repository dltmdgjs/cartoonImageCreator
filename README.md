# Cartoon Image Creator

### 기능
- OpenCV를 이용하여 기존의 이미지를 만화 스타일로 변경하는 기능
  

#### 기능 설명
- cvtColor를 이용해 이미지의 색상공간을 변환함(컬러 -> 그레이)
- medianBlur를 이용해 이미지 색상을 부드럽게 함
- adaptiveThreshold를 이용해 binary(흑백) 이미지(edges)를 생성함
- dilate를 이용해 선을 두껍게(팽창)함
- bilateralFilter를 이용해 기존 이미지를 edge-preserving and smoothing함
- bitwise_and를 이용해 기존 이미지에 edges를 mask함

### 만화 느낌이 잘 표현되는 이미지 데모
<img width="700" alt="스크린샷 2025-03-20 오후 10 05 13" src="https://github.com/user-attachments/assets/137ffdb0-c913-480c-b79a-e5c942aa4060" />
<img width="700" alt="스크린샷 2025-03-20 오후 10 07 25" src="https://github.com/user-attachments/assets/a63814da-b6e5-488f-b381-b2f0de94c805" />
<img width="700" alt="스크린샷 2025-03-20 오후 10 09 45" src="https://github.com/user-attachments/assets/cbb7a99b-2450-4b4d-9802-61e20968e07d" />


### 만화 느낌이 잘 표현되지 않는 이미지 데모
<img width="700" alt="스크린샷 2025-03-20 오후 10 06 56" src="https://github.com/user-attachments/assets/a31a454d-6b5c-4c34-822c-5c73f0714359" />
<img width="700" alt="스크린샷 2025-03-20 오후 10 04 14" src="https://github.com/user-attachments/assets/f1ac4a45-2a24-4c38-b1c9-268e0648bae1" />
<img width="700" alt="스크린샷 2025-03-20 오후 10 07 55" src="https://github.com/user-attachments/assets/6b5ea253-51d7-4108-93e6-9d9680f447dc" />


### 분석 (자신의 알고리즘 한계점)
- 카툰 이미지의 주 특징인 엣지의 느낌이 이미지의 전체적인 밝기로 인해서 살지 않거나, 엣지 자체가 얇거나 너무 두꺼움.
- 또한 자유의 여신상 이미지의 경우 dilate를 주었으나 여전히 엣지가 얇음.
- 반면 고양이 이미지의 경우에도 dilate를 똑같이 주었으나 엣지가 너무 두꺼움.
- 결론적으로 색상의 대비가 뚜렷하고, 건물과 같이 색상의 경계가 뚜렷하게 표현되는 이미지들은 카툰화가 잘 됨.
- 하지만, 색상이 한쪽으로 치우쳐져 있거나(너무 밝거나, 어두움), 경계가 뚜렷하지 않은 경우 카툰화가 잘 안됨.
