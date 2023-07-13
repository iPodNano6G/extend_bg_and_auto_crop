백엔드 부분의 코드가 저장된 폴더입니다.
배포를 위한 준비가 부족하여, 코드를 실행시키기 까다로운 상황입니다. 곧 개선할 계획입니다.

실행하기 위해서 다음의 조건을 만족해야합니다. 
1. back-end 폴더에 u-net 가중치 파일을 배치해야합니다. 
2. .env을 파일 생성하고 openAI api키를 삽입해야합니다.    
3. requirment.txt에 기입된 패키지들을 설치해야합니다.
```bash
pip install -r requirements.txt
```
4. Google CLI를 설치해야 합니다. 설치를 위해서는 다음 링크의 절차를 따라주세요. 
https://cloud.google.com/vision/docs/detect-labels-image-client-libraries?hl=ko#local-shell

위의 조건을 만족했다면 Root 폴더를 src로 바꾸고 다음의 명령어를 입력해 실행합니다.
```Bash
python main.py <다운로드할 파일의 정보가 입력된 json 파일>
```
해당 작업을 실행하면 상품의 이름에 해당하는 폴더에 원본 이미지와 결과물이 저장됩니다.