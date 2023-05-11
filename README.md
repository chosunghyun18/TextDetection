## Cloud -9 Streamlit 으로 웹서비스 만들기

# TextDetection

Amazon Recognition - TextDetection

1. requirements.txt 파일을 만들고 필요한 라이브러리들을 입력

2. 저장 후 pip install -r requirements.txt

3. text.py 작성

## 실행 터미널 환경

- root 경로에 resize.sh 파일을 생성

### 파일 권한 부여

chmod +x resize.sh

### 원하는 사이즈로 실행 다음 하단 3개중 1개만

./resize.sh 20 # 20GB 로 늘리기

./resize.sh 30 # 30GB 로 늘리기 : 최소

./resize.sh 40 # 40GB 로 늘리기

streamlit run text.py

### ex

![ca](https://github.com/chosunghyun18/TextDetection/assets/37647483/4b5a3c06-8b0c-47bb-b8b4-5cd035698509)

![ccv1](https://github.com/chosunghyun18/TextDetection/assets/37647483/c29aa2c3-4a47-4351-89ee-56a71e68c417)
