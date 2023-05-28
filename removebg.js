const axios = require('axios');
const FormData = require('form-data');
const fs = require('fs');

const apiEndpoint = 'https://api.remove.bg/v1.0/removebg';
const apiKey = 'XDHDuzSvAA46GQ84ZEtw2WFc';
var images = [
  './images/first_images/result.png',
  './images/first_images/result_withClothes.png',
  './images/first_images/result_vertical_noFace.png',
  './images/first_images/result_panorama_withFace.png',
  './images/first_images/result_panorama_noFace.png',
  './images/first_images/result_onlyClothes.png',
  // 폴더 1의 이미지 목록

  './images/second_images/result.png',
  './images/second_images/result_withClothes.png',
  './images/second_images/result_vertical_noFace.png',
  './images/second_images/result_vertical_withFace.png',
  './images/second_images/result_panorama_noFace.png',
  './images/second_images/result_onlyClothes.png',
  // 폴더 2의 이미지 목록

  './images/third_images/result.png',
  './images/third_images/result_withClothes.png',
  './images/third_images/result_vertical_noFace.png',
  './images/third_images/result_panorama_withFace.png',
  './images/third_images/result_panorama_noFace.png',
  './images/third_images/result_onlyClothes.png',
  // 폴더 3의 이미지 목록
];

// 비동기 함수로 감싸서 await를 사용할 수 있도록 합니다.
async function processImages() {
  for (let i = 0; i < images.length; i++) {
    const imagePath = images[i];

    const formData = new FormData();
    formData.append('size', 'auto');
    formData.append('bg_color', '0000');
    formData.append('image_file', fs.createReadStream(imagePath));

    try {
      const response = await axios.post(apiEndpoint, formData, {
        responseType: 'arraybuffer',
        headers: {
          ...formData.getHeaders(),
          'X-Api-Key': apiKey,
        },
        encoding: null,
      });

      if (response.status !== 200) {
        console.error('Error:', response.status, response.statusText);
        continue; // 다음 이미지로 넘어갑니다.
      }

      const outputFilePath = `removeBgImage_${i + 1}.png`;
      fs.writeFileSync(outputFilePath, response.data);
      console.log(
        `이미지 ${i + 1}의 배경을 제거하여 ${outputFilePath}로 저장했습니다.`
      );
    } catch (error) {
      console.error('Request failed:', error);
    }
  }
}

processImages();
