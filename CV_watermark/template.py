import cv2
import numpy as np
from matplotlib import pyplot as plt
from torch import empty


# img = cv2.imread(r'images/true/page_0.png',0)
# img2 = img.copy()
# template = cv2.imread('template.png',0)
# w, h = template.shape[::-1]
# # All the 6 methods for comparison in a list
# methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
#             'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
# for meth in methods:
#     img = img2.copy()
#     method = eval(meth)
#     # Apply template Matching
#     res = cv2.matchTemplate(img,template,method)
#     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
#     # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
#     if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
#         top_left = min_loc
#     else:
#         top_left = max_loc
#     bottom_right = (top_left[0] + w, top_left[1] + h)
#     cv2.rectangle(img, top_left, bottom_right, 255, 2)
#     plt.subplot(121),plt.imshow(res,cmap = 'gray')
#     plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
#     plt.subplot(122),plt.imshow(img,cmap = 'gray')
#     plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
#     plt.suptitle(meth)
#     plt.show()

# img_rgb = cv2.imread('mario.png')
# img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
# template = cv2.imread('mario_coin.png',0)
# w, h = template.shape[::-1]
# res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
# threshold = 0.8
# loc = np.where( res >= threshold)
# for pt in zip(*loc[::-1]):
#     cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
# cv2.imwrite('res.png',img_rgb)




img_rgb = cv2.imread(r'images/true/page_41.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('template.png', 0)
kf =  template.shape[1] / img_gray.shape[1] 

i_h, i_w = [int(i*kf) for i in img_gray.shape[::-1]]

img_gray = cv2.resize(img_gray, dsize=(i_h, i_w))
# template = cv2.resize(template, dsize=(img_gray.shape[1], int(template.shape[0]*kf)))

height, width = template.shape[::]

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
plt.imshow(res, cmap='gray')

threshold = 0.3 #For TM_CCOEFF_NORMED, larger values = good fit.
loc = np.where(res >= threshold)
print(*loc)
flag = True if len(loc[0]) > 0 else False

if flag:
    print('ДОВЕРЕННОСТЬ НОТАРИАЛЬНАЯ, ПРОВЕРЕНО!')

else:
    print('НЕ НОТАРИАЛЬНАЯ')
# for pt in zip(*loc[::-1]):
#     cv2.rectangle(img_rgb, pt, (pt[0] + int(width/kf), pt[1] + int(height/kf)), (255, 0, 0), 5) 

# cv2.imshow("Matched image", img_rgb)
# cv2.waitKey()
# cv2.destroyAllWindows()