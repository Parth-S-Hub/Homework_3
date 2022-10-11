import cv2

# Read the image.
img = cv2.imread('C:/Users/Parth Shinde/Desktop/CLEMSON/Coursework/Computing & Sim for Autonomy/Homework/HW3/test.jpg')

# Apply bilateral filter
bilateral = cv2.bilateralFilter(img,10,50,100,borderType=cv2.BORDER_CONSTANT)


# Save the output.
cv2.imwrite('bilateral.jpg', bilateral)
cv2.imshow("Orignal", img)
cv2.imshow("Filtered", bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()