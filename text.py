import cv2
import boto3
import numpy as np
import streamlit as st

st.title("rekognition TextDetections")

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    file_bytes = uploaded_file.read()
    #rekognition 중 detect_text() 사용 방법
    session = boto3.Session(profile_name='default')
    client = session.client('rekognition')

    image = {'Bytes': file_bytes}
    response = client.detect_text(Image=image)
    #반환된 response 에서 데이터 출력
    textDetections = response['TextDetections']
    print('Detected text\n----------')
    #결과를 이미지에 표시
    nd_bytes = np.asarray(bytearray(file_bytes), dtype=np.uint8)
    im = cv2.imdecode(nd_bytes, 1)
    h, w, _ = im.shape
    
    for text in textDetections:
        print(text)
        if not 'ParentId' in text:
            t_color = (0, 255, 0)
            if text['Confidence'] < 90:
                t_color = (255, 0, 0)
            elif text['Confidence'] < 80:
                t_color = (0, 0, 255)
                
            bbox = text['Geometry']['BoundingBox']
            x1 = int(text['Geometry']['BoundingBox']['Left'] * w)
            y1 = int(text['Geometry']['BoundingBox']['Top'] * h)
            x2 = int((text['Geometry']['BoundingBox']['Left']+text['Geometry']['BoundingBox']['Width']) * w)
            y2 = int((text['Geometry']['BoundingBox']['Top']+text['Geometry']['BoundingBox']['Height']) * h)
            cv2.rectangle(im, (x1, y1), (x2, y2), t_color, 2)
            st.text(text['DetectedText'])


    st.image(im, channels="BGR")