import cv2
from fer import FER

# Initialize the FER emotion detector
detector = FER()

def add_emoji(frame, emotion):
    """Overlay an emoji based on the detected emotion."""
    emoji_dict = {
        "happy": "😊",
        "sad": "😢",
        "angry": "😡",
        "surprise": "😲",
        "neutral": "😐",
        "fear": "😱",
        "disgust": "🤢"
    }
    if emotion in emoji_dict:
        cv2.putText(frame, emoji_dict[emotion], (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)

def main():
    # Start the webcam
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Flip the frame for mirror effect
        frame = cv2.flip(frame, 1)

        # Detect emotions in the current frame
        emotion, score = detector.top_emotion(frame)
        
        # Add emotion label to the frame
        cv2.putText(frame, f"Emotion: {emotion.capitalize()} ({score*100:.2f}%)", 
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Add an emoji overlay based on the emotion
        add_emoji(frame, emotion.lower())

        # Display the frame with emotion info
        cv2.imshow("Emotion Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
