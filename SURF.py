import cv2
from matplotlib import pyplot as plt

img = cv2.imread('fly01.png',  0)
img1 = cv2.imread('fly_3.jpg', 0)

# Create SURF object. You can specify params here or later.
# Here I set Hessian Threshold to 400
surf = cv2.xfeatures2d.SURF_create(400)

# Find keypoints and descriptors directly
kp, des = surf.detectAndCompute(img, None)
kp1, des1 = surf.detectAndCompute(img1, None)
print("len(kp)=%d" % len(kp))
# 699

# Check present Hessian threshold
print("surf.getHessianThreshold() = %d" % surf.getHessianThreshold())
# 400.0

# We set it to some 50000. Remember, it is just for representing in picture.
# In actual cases, it is better to have a value 300-500
surf.setHessianThreshold(50000)
print("now surf.getHessianThreshold() = %d" % surf.getHessianThreshold())

# Again compute keypoints and check its number.
kp, des = surf.detectAndCompute(img, None)
kp1, des1 = surf.detectAndCompute(img1, None)
print("len(kp)=%d" % len(kp))

# img2 = cv2.drawKeypoints(img, kp, None, (255, 0, 0), 4)
img2 = cv2.drawKeypoints(img, kp, None, (255, 0, 0), 4)
img4 = cv2.drawKeypoints(img1, kp1, None, (255, 0, 0), 4)

# create BFMatcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
# Match descriptors.
#matches = bf.match(des1, des)
# Sort them in the order of their distance.
#matches = sorted(matches, key = lambda x:x.distance)
# Draw first 10 matches.
#img3 = cv2.drawMatches(img,kp,img1,kp1,matches[:10], flags=2)

#plt.imshow(img3)
#plt.imshow(img2)
plt.imshow(img4)
plt.title('Image')
plt.show()