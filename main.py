import cv2

# Read image
image_path = 'C:/Users/ASUS/Desktop/MicrosoftTeams-image.png'
img = cv2.imread(image_path)

# Image processing
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
blurred = cv2.GaussianBlur(gray, (5, 5), 0)  # Gaussian smoothing
threshold = 127
ret, binary = cv2.threshold(blurred, threshold, 255, cv2.THRESH_BINARY)  # Simple Thresholding

# Find contours
# cv.findContours(img, mode, method)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Calculate the area of each detected contour, and rank the top three choices
Areas = []
for i, contour in enumerate(contours):
    area = cv2.contourArea(contour)  # calculate the area of a specific contour
    Areas.append((i, area))

Sorted_Areas = sorted(Areas, key=lambda x: x[1], reverse=True)

Top_three = []
for i in range(3):
    item_num = Sorted_Areas[i][0]
    cnt = contours[item_num]  # store the vector of points of a specific contour
    Top_three.append(cnt)

# Draw the result
draw_img = cv2.drawContours(img.copy(), Top_three, -1, (0, 0, 255), 2)
cv2.imshow('Result', draw_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('result.png', draw_img)