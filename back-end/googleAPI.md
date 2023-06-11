구글 Cloud Vision API의 설정법을 다룹니다.
sudo apt-get install apt-transport-https ca-certificates gnupg  

echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt  

cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list  

curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo tee /usr/share/keyrings/cloud.google.gpg  

sudo apt-get update && sudo apt-get install google-cloud-cli  

gcloud init  

export GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"  

export GOOGLE_APPLICATION_CREDENTIALS="/home/sang/automated_image_processing/automated_image_processing/automated_image_processing/back-end/google_cloud_vision_key.json"

google.api_core.exceptions.Unauthenticated: 401 Request had invalid authentication credentials. Expected OAuth 2 access token, login cookie or other valid authentication credential. See https://developers.google.com/identity/sign-in/web/devconsole-project. [reason: "ACCESS_TOKEN_EXPIRED"...
-> 시간 에러입니다. 작동중인 서버의 시간을 확인해주세요. WSL환경에서 자주 발생합니다. 재부팅이 답입니다.

sudo chown -R mongodb:mongodb /var/lib/mongodb
sudo chown mongodb:mongodb /tmp/mongodb-27017.sock