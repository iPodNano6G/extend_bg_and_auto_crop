# 기본 이미지 설정
FROM python:3.11.4-slim-bullseye

# 작업 디렉토리 설정
WORKDIR /app

# 의존성 설치
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0
    
# 소스코드 복사
COPY . .

WORKDIR /app/src
# Flask 명령으로 앱 실행
CMD [ "python", "-m" , "app", "run", "--host=0.0.0.0"]