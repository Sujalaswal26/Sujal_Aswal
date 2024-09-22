import cv2
from deepface import DeepFace

# Path of the image to be used
imgpath = '2.jpg'   # yaha pe path change kr skta hai like 1.jpg,2.jpg jo b image ka name hai maine rename krke 2 rakha tha to 2.jpg
image = cv2.imread(imgpath)

# Perform facial analysis for age, gender, and emotion
analyze = DeepFace.analyze(image, actions=['age', 'gender', 'emotion'])

# Print the results
print("Detected age:", analyze['age'])
print("Detected gender:", analyze['gender'])
print("Emotion detected:", analyze['dominant_emotion'])
