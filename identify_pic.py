# 导入模块 cv2匹配算法

import cv2


def get_center():

    # 读入图片 big1.png是背景大图; small.png是需要寻找的小图（格式.jpg .png都行）
    img = cv2.imread("big1.png", 0)  # 0 读入灰度图
    img3 = cv2.imread("big1.png", 1)  # 1 读入彩色图
    img2 = img.copy()
    template = cv2.imread("small.png", 0)
    w, h = template.shape[::-1]

    # 算法
    method = 'cv2.TM_SQDIFF'


    img = img2.copy()
    method = eval(method)

    # 应用模板算法，返回一系列指标
    res = cv2.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)  # 从res中挑选最优指标

    # 注意 TM_SQDIFF 或者 TM_SQDIFF_NORMED 算法使用最小值为最优

    top_left = min_loc

    bottom_right = (top_left[0] + w, top_left[1] + h)

    # print(top_left, bottom_right)

    center = ((top_left[0]+bottom_right[0])/2, (top_left[1]+bottom_right[1])/2)
    # print(center)

    return center


