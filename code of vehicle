import cv2

Model = "PTM.xml"  # Model

cap = cv2.VideoCapture(0)  # My default cam

cap.set(3, 640)  # Width of Window
cap.set(4, 480)  # Height of Window

if not cap.isOpened():
    print("Error: Webcam can't open")
    exit()

min_area = 500
count = 0

while True:
    success, img = cap.read()

    if not success:
        print("Error: Failed to capture frame")
        break

    plate_cascade = cv2.CascadeClassifier(Model)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)

    for (x, y, w, h) in plates:
        area = w * h

        if area > min_area:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, "Number Plate", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)

            img_roi = img[y: y + h, x:x + w]
            cv2.imshow("ROI", img_roi)

    cv2.imshow("Result", img)

    # Save the plate upon 's' press
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("platess/scaned_img_" + str(count) + ".jpg", img_roi)
        cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, "Plate Saved", (150, 265), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255), 2)
        cv2.imshow("Results", img)
        cv2.waitKey(500)
        count += 1
        
    # Exit loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):  
        break

cap.release()
cv2.destroyAllWindows()
