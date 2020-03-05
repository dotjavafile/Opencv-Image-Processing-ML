import cv2


img = cv2.imread('image.jpg')

img_dimen = img.shape
img_dtype = img.dtype
print(img_dimen)

h,w =0.0,0.0
h=int(img_dimen[0]*(20/100))
w=int(img_dimen[1]*0.2)
print("H: %.2f - W: %.2f" %(h,w))
n_dim = (w,h)

resized = cv2.resize(img,n_dim)
cv2.imshow("Resized image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("output.jpg", resized)