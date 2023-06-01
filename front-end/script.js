const imageList1 = [
  {
    src: './images/first_images/original.jpg',
    description: '원본 이미지'
  },
  {
    src: './images/first_images/result.png',
    description: '확장 완료된 이미지'
  },
  {
    src: './images/first_images/result_onlyClothes.png',
    description: '옷만',
  },
  {
    src: './images/first_images/result_withClothes.png',
    description: '얼굴 포함',
  },
  {
    src: './images/first_images/result_vertical_noFace.png',
    description: '수직 이미지',
  },
  {
    src: './images/first_images/result_panorama_withFace.png',
    description: '얼굴이 있는 파노라마',
  },
  {
    src: './images/first_images/result_panorama_noFace.png',
    description: '얼굴 없는 파노라마',
  },
];

const imageList2 = [
  {
    src: './images/second_images/original.jpg',
    description: '원본 이미지'
  },
  {
    src: './images/second_images/result.png',
    description: '확장 완료된 이미지'
  },
  {
    src: './images/second_images/result_onlyClothes.png',
    description: '옷만',
  },
  {
    src: './images/second_images/result_withClothes.png',
    description: '얼굴 포함',
  },
  {
    src: './images/second_images/result_vertical_noFace.png',
    description: '수직 이미지',
  },
  {
    src: './images/second_images/result_panorama_withFace.png',
    description: '얼굴이 있는 파노라마',
  },
  {
    src: './images/second_images/result_panorama_noFace.png',
    description: '얼굴 없는 파노라마',
  },
]
  // 폴더 2의 이미지 목록

  const imageList3 = [
    {
      src: './images/third_images/original.jpg',
      description: '원본 이미지'
    },    
  {
    src: './images/third_images/result.png',
    description: '확장 완료된 이미지'
  },
  {
    src: './images/third_images/result_onlyClothes.png',
    description: '옷만',
  },
  {
    src: './images/third_images/result_withClothes.png',
    description: '얼굴 포함',
  },
  {
    src: './images/third_images/result_vertical_noFace.png',
    description: '수직 이미지',
  },
  {
    src: './images/third_images/result_panorama_withFace.png',
    description: '얼굴이 있는 파노라마',
  },
  {
    src: './images/third_images/result_panorama_noFace.png',
    description: '얼굴 없는 파노라마',
  },
  // 폴더 3의 이미지 목록
];

const imageList4 = [
  {
    src: './images/4th_images/original.jpg',
    description: '원본 이미지'
  },
  {
    src: './images/4th_images/result.png',
    description: '확장 완료된 이미지'
  },
  {
    src: './images/4th_images/result_onlyClothes.png',
    description: '옷만',
  },
  {
    src: './images/4th_images/result_withClothes.png',
    description: '얼굴 포함',
  },
  {
    src: './images/4th_images/result_vertical_noFace.png',
    description: '수직 이미지',
  },
  {
    src: './images/4th_images/result_panorama_withFace.png',
    description: '얼굴이 있는 파노라마',
  },
  {
    src: './images/4th_images/result_panorama_noFace.png',
    description: '얼굴 없는 파노라마',
  },
  // 폴더 3의 이미지 목록
];

const noBackground = [
    {
      src: './images/first_images/noBackground.png',
      description: '배경 없는 사진',
    },
    {
      src: './images/second_images/noBackground.png',
      description: '배경 없는 사진',
    },
    {
      src: './images/third_images/noBackground.png',
      description: '배경 없는 사진',
    },
    {
      src: './images/4th_images/noBackground.png',
      description: '배경 없는 사진',
    },
]


const container1 = document.querySelector('#image-container1');
const container2 = document.querySelector('#image-container2');
const container3 = document.querySelector('#image-container3');
const container4 = document.querySelector('#image-container4');
const container5 = document.querySelector('#noBackground');

function displayImages(imageList, container) {
  imageList.forEach(image => {
    const card = document.createElement('div');
    card.classList.add('image-card');

    const img = document.createElement('img');
    img.src = image.src;

    const description = document.createElement('p');
    description.textContent = image.description;

    card.appendChild(img);
    card.appendChild(description);
    container.appendChild(card);
  });
}


displayImages(imageList1, container1);
displayImages(imageList2, container2);
displayImages(imageList3, container3);
displayImages(imageList4, container4);
displayImages(noBackground, container5);

toggleButton.addEventListener('click', function() {
  document.body.classList.toggle('dark');
});