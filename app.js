const imageList = [
  { src: './images/first_images/result.png', description: '첫 번째 이미지' },
  {
    src: './images/first_images/result_withClothes.png',
    description: '옷이 있는 첫 번째 이미지',
  },
  {
    src: './images/first_images/result_vertical_noFace.png',
    description: '얼굴 없는 수직 첫 번째 이미지',
  },
  {
    src: './images/first_images/result_panorama_withFace.png',
    description: '얼굴이 있는 파노라마 첫 번째 이미지',
  },
  {
    src: './images/first_images/result_panorama_noFace.png',
    description: '얼굴 없는 파노라마 첫 번째 이미지',
  },
  {
    src: './images/first_images/result_onlyClothes.png',
    description: '옷만 있는 첫 번째 이미지',
  },
  // 폴더 1의 이미지 목록

  { src: './images/second_images/result.png', description: '두 번째 이미지' },
  {
    src: './images/second_images/result_withClothes.png',
    description: '옷이 있는 두 번째 이미지',
  },
  {
    src: './images/second_images/result_vertical_noFace.png',
    description: '얼굴 없는 수직 두 번째 이미지',
  },
  {
    src: './images/second_images/result_vertical_withFace.png',
    description: '얼굴이 있는 수직 두 번째 이미지',
  },
  {
    src: './images/second_images/result_panorama_noFace.png',
    description: '얼굴 없는 파노라마 두 번째 이미지',
  },
  {
    src: './images/second_images/result_onlyClothes.png',
    description: '옷만 있는 두 번째 이미지',
  },
  // 폴더 2의 이미지 목록

  { src: './images/third_images/result.png', description: '세 번째 이미지' },
  {
    src: './images/third_images/result_withClothes.png',
    description: '옷이 있는 세 번째 이미지',
  },
  {
    src: './images/third_images/result_vertical_noFace.png',
    description: '얼굴 없는 수직 세 번째 이미지',
  },
  {
    src: './images/third_images/result_panorama_withFace.png',
    description: '얼굴이 있는 파노라마 세 번째 이미지',
  },
  {
    src: './images/third_images/result_panorama_noFace.png',
    description: '얼굴 없는 파노라마 세 번째 이미지',
  },
  {
    src: './images/third_images/result_onlyClothes.png',
    description: '옷만 있는 세 번째 이미지',
  },
  // 폴더 3의 이미지 목록
];

const bgList = [
  { src: './removeBgImage_1.png', description: '첫 번째 이미지' },
  {
    src: './removeBgImage_2.png',
    description: '옷이 있는 첫 번째 이미지',
  },
  {
    src: './removeBgImage_3.png',
    description: '얼굴 없는 수직 첫 번째 이미지',
  },
  {
    src: './removeBgImage_4.png',
    description: '얼굴이 있는 파노라마 첫 번째 이미지',
  },
  {
    src: './removeBgImage_5.png',
    description: '얼굴 없는 파노라마 첫 번째 이미지',
  },
  {
    src: './removeBgImage_6.png',
    description: '옷만 있는 첫 번째 이미지',
  },
  // 폴더 1의 이미지 목록

  { src: './removeBgImage_7.png', description: '두 번째 이미지' },
  {
    src: './removeBgImage_8.png',
    description: '옷이 있는 두 번째 이미지',
  },
  {
    src: './removeBgImage_9.png',
    description: '얼굴 없는 수직 두 번째 이미지',
  },
  {
    src: './removeBgImage_10.png',
    description: '얼굴이 있는 수직 두 번째 이미지',
  },
  {
    src: './removeBgImage_11.png',
    description: '얼굴 없는 파노라마 두 번째 이미지',
  },
  {
    src: './removeBgImage_12.png',
    description: '옷만 있는 두 번째 이미지',
  },
  // 폴더 2의 이미지 목록

  { src: './removeBgImage_13.png', description: '세 번째 이미지' },
  {
    src: './removeBgImage_14.png',
    description: '옷이 있는 세 번째 이미지',
  },
  {
    src: './removeBgImage_15.png',
    description: '얼굴 없는 수직 세 번째 이미지',
  },
  {
    src: './removeBgImage_16.png',
    description: '얼굴이 있는 파노라마 세 번째 이미지',
  },
  {
    src: './removeBgImage_17.png',
    description: '얼굴 없는 파노라마 세 번째 이미지',
  },
  {
    src: './removeBgImage_18.png',
    description: '옷만 있는 세 번째 이미지',
  },
];

function displayImages() {
  var imageContainer = document.getElementById('imageContainer');
  imageContainer.innerHTML = ''; // 기존 이미지 초기화

  for (var i = 0; i < imageList.length; i++) {
    var imageSrc = imageList[i].src;
    var imageDescription = imageList[i].description;

    var imgElement = document.createElement('img');
    imgElement.src = imageSrc;
    imgElement.alt = imageDescription;
    imgElement.classList.add('thumbnail');

    var captionElement = document.createElement('div');
    captionElement.innerText = imageDescription;

    var figureElement = document.createElement('figure');
    figureElement.appendChild(imgElement);
    figureElement.appendChild(captionElement);

    imageContainer.appendChild(figureElement);
  }
}

displayImages();

function displayImagesBg() {
  var imageContainer = document.getElementById('imageContainerBg');
  imageContainer.innerHTML = ''; // 기존 이미지 초기화

  for (var i = 0; i < bgList.length; i++) {
    var imageSrc = bgList[i].src;
    var imageDescription = bgList[i].description;

    var imgElement = document.createElement('img');
    imgElement.src = imageSrc;
    imgElement.alt = imageDescription;
    imgElement.classList.add('thumbnail');

    var captionElement = document.createElement('div');
    captionElement.innerText = imageDescription;

    var figureElement = document.createElement('figure');
    figureElement.appendChild(imgElement);
    figureElement.appendChild(captionElement);

    imageContainer.appendChild(figureElement);
  }
}
displayImagesBg();

function changeBackground() {
  var body = document.body;
  var currentColor = body.style.backgroundColor;

  if (currentColor === '' || currentColor === 'initial') {
    // 배경색이 설정되지 않았거나 초기값인 경우, 검은색으로 설정
    body.style.backgroundColor = '#000000';
    body.style.color = '#ffffff';
    changeBorderToWhite();
  } else {
    // 이미 배경색이 설정된 경우, 초기값으로 되돌림
    body.style.backgroundColor = '';
    body.style.color = '#000000';
    changeBorderToBlack();
  }
}

function changeBorderToWhite() {
  var thumbnails = document.querySelectorAll('.thumbnail');

  thumbnails.forEach(function (thumbnail) {
    thumbnail.style.border = '2px solid white';
  });
}

function changeBorderToBlack() {
  var thumbnails = document.querySelectorAll('.thumbnail');

  thumbnails.forEach(function (thumbnail) {
    thumbnail.style.border = '2px solid black';
  });
}
