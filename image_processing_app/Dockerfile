# 기본 이미지 설정
FROM python:3.10-slim

# 작업 디렉토리 설정
WORKDIR /app

RUN apt-get update && apt-get install -y libglib2.0-0
# 의존성 설치
RUN apt-get update && apt-get install -y libgl1-mesa-glx
#libgl1-mesa-glx
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
#소스코드 복사
COPY . .
WORKDIR /app/src
# Flask 명령으로 앱 실행
CMD [ "python", "app.py"]
#CMD [ "python", "-m" , "app", "run", "--host=0.0.0.0"]