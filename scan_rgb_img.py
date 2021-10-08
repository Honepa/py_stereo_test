import sys
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from interpol import interpol

img = cv.imread(sys.argv[1],1)

# X,Y = [x for x in np.where(edges>0)]

img_red_c = img[:,:,2]
img_green_c = img[:,:,1]
img_blue_c = img[:,:,0]

# other way:
# X_r = np.where(img_red_c>254)[0]
# Y_r = np.where(img_red_c>254)[1]
# X_b = np.where(img_blue_c<20)[0]
# Y_b = np.where(img_blue_c<20)[1]
# X_g = np.where(img_green_c<20)[0]
# Y_g = np.where(img_green_c<20)[1]

# # TODO: cut array by the shortest one!
# X_ints = np.intersect1d(np.intersect1d(X_r, X_b), np.intersect1d(X_r, X_g))
# Y_ints = np.intersect1d(np.intersect1d(Y_r, Y_b), np.intersect1d(Y_r, Y_g))[:len(x_ints)]

# the working way

mask_g = (img_green_c < 70) & (img_blue_c < 70) & (img_red_c > 114)
res = img_red_c * mask_g

# plt.imshow(res,cmap = 'gray')
# plt.show()

edges = cv.Canny(res,200,255)

res = interpol(edges)
# print(res)

# plt.imshow(edges,cmap = 'gray')
f = plt.figure()
plt_idx = 1
for x,z,y in res:
	# a = (1,1)
	# plt_vals = a[0]*100 + a[1]*10 + plt_idx
	# y1 = f.add_subplot(plt_vals)
	# y1.plot(r)
	plt.scatter(x,y)
	plt.plot(x,z)

plt.show()

