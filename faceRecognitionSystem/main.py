import cv2
import face_recognition

# Load a known image and encode it
known_image = face_recognition.load_image_file("known_person.jpg")
known_encoding = face_recognition.face_encodings(known_image)[0]

# List of known encodings and names
known_encodings = [known_encoding]
known_names = ["Known Person"]

# Initialize webcam
video_capture = cv2.VideoCapture(0)

print("Starting face recognition. Press 'q' to quit.")

while True:
    # Capture a frame from the webcam
    ret, frame = video_capture.read()

    # Convert the frame from BGR to RGB (face_recognition uses RGB)
    rgb_frame = frame[:, :, ::-1]

    # Detect faces and compute face encodings
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Check if the detected face matches known faces
        matches = face_recognition.compare_faces(known_encodings, face_encoding)
        name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_names[first_match_index]

        # Draw a box around the face and label it
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

    # Display the frame
    cv2.imshow("Face Recognition", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
video_capture.release()
cv2.destroyAllWindows()