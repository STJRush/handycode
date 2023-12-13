import cv2
import pytesseract

# Set the path to the tesseract executable
# Update according to your Tesseract installation path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Example for Windows
# pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'  # Example for Linux

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Capture one frame
ret, frame = cap.read()

# Release the webcam
cap.release()

if not ret:
    print("Failed to capture image from webcam.")
else:
    # Save the captured image
    image_path = 'captured_image.jpg'
    cv2.imwrite(image_path, frame)

    # Load the saved image
    saved_image = cv2.imread(image_path)

    # Process the image
    gray = cv2.cvtColor(saved_image, cv2.COLOR_BGR2GRAY)
    contrast = cv2.convertScaleAbs(gray, alpha=1.5, beta=0)
    blurred = cv2.GaussianBlur(contrast, (5, 5), 0)
    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Use Tesseract to extract the number
    text = pytesseract.image_to_string(thresh, config='--psm 6 digits')
    print('Detected Number:', text.strip())

    # Display the images for verification
    cv2.imshow('Captured Image', saved_image)
    cv2.imshow('Processed Image', thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
