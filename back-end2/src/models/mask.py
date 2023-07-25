import cv2
import numpy as np

from models.image import Image

class Mask(Image):
    def __init__(self):
        super().__init__()
        self.smallest_box_x = None
        self.smallest_box_y = None
        self.smallest_box_width = None
        self.smallest_box_height = None
        self.touch_border_left = None
        self.touch_border_top = None
        self.touch_border_right = None
        self.touch_border_bottom = None

    def set_smallest_box(self):
        contours, _ = cv2.findContours(self.np_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # 모든 객체의 윤곽선을 하나의 리스트로 병합
        all_contours = np.concatenate(contours)
        # 윤곽선을 감싸는 최소 사각형 좌표 계산
        object_x, object_y, object_w, object_h = cv2.boundingRect(all_contours)

        self.smallest_box_x = object_x
        self.smallest_box_y = object_y
        self.smallest_box_width = object_w
        self.smallest_box_height = object_h
    
    def get_long_side_length(self):
        if self.smallest_box_height >= self.smallest_box_width:
            return self.smallest_box_height
        else:
            return self.smallest_box_width
        
    def check_touching_border(self, extra = 10):
        if self.smallest_box_x <= extra + 0:
            self.touch_border_left = True
        else:
            self.touch_border_left = False

        if self.smallest_box_y <= extra + 0:
            self.touch_border_top = True
        else:
            self.touch_border_top = False

        if self.smallest_box_x + self.smallest_box_width >= self.width - extra:
            self.touch_border_right = True
        else:
            self.touch_border_right = False

        if self.smallest_box_y + self.smallest_box_height >= self.height - extra:
            self.touch_border_bottom = True
        else:
            self.touch_border_bottom = False
            