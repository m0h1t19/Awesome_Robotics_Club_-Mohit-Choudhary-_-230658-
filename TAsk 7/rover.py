import cv2

# Load the image
image = cv2.imread('img.png')

# Apply Non-Local Means Denoising
noise_filtered_image = cv2.fastNlMeansDenoisingColored(image, None, 22, 20, 11, 21)

# Display the result
cv2.imshow('Original Image', image)
cv2.imshow('Denoised Image', noise_filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the denoised image
cv2.imwrite('denoised_image.jpg', noise_filtered_image)
