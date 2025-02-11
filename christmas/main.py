import cv2
import os
import time

# Load Haar cascades for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load Santa hat image
hat_path = r'C:\Users\User\OneDrive\Desktop\christmas\santa_hat.jpg'  # Use raw string notation
santa_hat = cv2.imread(hat_path)

if santa_hat is None:
    print("Error: Santa hat image not found. Please check the file path.")
    exit()

def overlay_santa_hat(face, hat):
    """
    Overlay the Santa hat on the face.
    """
    hat_width = face.shape[1]
    hat_height = int(hat.shape[0] * (hat_width / hat.shape[1]))
    resized_hat = cv2.resize(hat, (hat_width, hat_height))
    
    y1, y2 = 0, hat_height
    x1, x2 = 0, hat_width

    for c in range(0, 3):
        face[y1:y2, x1:x2, c] = resized_hat[:, :, c]

    return face

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face_roi = frame[y:y+h, x:x+w]
        frame[y:y+h, x:x+w] = overlay_santa_hat(face_roi, santa_hat)

    # Display the frame with Santa hat
    cv2.imshow("Christmas Photo Booth", frame)
    
    # Automatically save the frame when a face is detected
    if len(faces) > 0:
        filename = f"christmas_photo_{time.strftime('%Y%m%d_%H%M%S')}.png"
        cv2.imwrite(filename, frame)
        print(f"Saved {filename}")
        time.sleep(5)  # Wait for 5 seconds before capturing the next image

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit the application
        break

cap.release()
cv2.destroyAllWindows()
