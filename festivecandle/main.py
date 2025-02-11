import cv2
import numpy as np
import pygame
import sounddevice as sd
import threading
import time

# Initialize Pygame for background music
pygame.init()
pygame.mixer.init()

# Load the background music (will play after candle is blown out)
background_music_path = 'newYear.mp3'  # Update this path with your music file

# Global flags and variables
blown_out = False
snowflakes = []

def detect_blow(signal, threshold=0.1, min_blow_duration=0.2):
    """Detect blow based on audio signal amplitude and duration."""
    amplitude = np.max(np.abs(signal))
    if amplitude > threshold:
        # Check if the blow lasts long enough to be a real blow, not a sudden word or breath.
        blow_duration = len(signal) / 44100  # Duration in seconds
        return blow_duration >= min_blow_duration
    return False

def audio_listener():
    """Thread to continuously listen for a blow."""
    global blown_out
    duration = 1.0  # seconds
    fs = 44100  # Sample rate
    while not blown_out:
        signal = sd.rec(int(duration * fs), samplerate=fs, channels=1)
        sd.wait()  # Wait until recording is finished
        if detect_blow(signal, threshold=0.1):  # Set a higher threshold
            blown_out = True
            pygame.mixer.music.load(background_music_path)
            pygame.mixer.music.play()

def draw_snowfall(frame):
    """Draw falling snowflakes."""
    global snowflakes
    height, width, _ = frame.shape
    # Add new snowflakes
    if len(snowflakes) < 100:
        snowflakes.append([np.random.randint(0, width), 0])

    # Update snowflakes positions
    for flake in snowflakes:
        flake[1] += np.random.randint(2, 5)  # Fall speed
        cv2.circle(frame, (flake[0], flake[1]), np.random.randint(2, 5), (255, 255, 255), -1)

    # Remove snowflakes that fall off-screen
    snowflakes = [flake for flake in snowflakes if flake[1] < height]

def draw_candle(frame, blown_out):
    """Draw the candle and its flame."""
    # Draw the candle body
    cv2.rectangle(frame, (300, 350), (340, 480), (255, 255, 255), -1)  # Candle body
    cv2.rectangle(frame, (310, 360), (330, 480), (255, 235, 205), -1)  # Candle wax

    if not blown_out:
        # Flickering flame effect
        flicker_intensity = np.random.randint(5, 15)
        flame_center = (320, 320)
        outer_flame_color = (0, 140 + flicker_intensity, 255)
        inner_flame_color = (0, 255, 255)

        # Outer flame
        cv2.ellipse(frame, flame_center, (15 + flicker_intensity, 30 + flicker_intensity), 0, 0, 360, outer_flame_color, -1)

        # Inner flame
        cv2.ellipse(frame, flame_center, (10, 20), 0, 0, 360, inner_flame_color, -1)

        # Add a glowing halo around the flame
        alpha = 0.4
        overlay = frame.copy()
        cv2.circle(overlay, flame_center, 40 + flicker_intensity, (0, 140, 255), -1)
        cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)

def draw_glittering_flowers(frame):
    """Draw glittering flowers after the candle is blown out."""
    for _ in range(10):  # Reduced to avoid overcrowding
        flower_center = (np.random.randint(0, 640), np.random.randint(0, 480))
        flower_color = (np.random.randint(0, 256), np.random.randint(0, 256), np.random.randint(0, 256))
        flower_radius = np.random.randint(5, 15)
        cv2.circle(frame, flower_center, flower_radius, flower_color, -1)

def draw_face_background(frame, face_coords):
    """Highlight your face area."""
    overlay = frame.copy()
    for (x, y, w, h) in face_coords:
        face_roi = frame[y:y+h, x:x+w]
        face_overlay = cv2.addWeighted(face_roi, 0.7, overlay[y:y+h, x:x+w], 0.3, 0)
        frame[y:y+h, x:x+w] = face_overlay

def main():
    """Main function to render the candle and listen for blow detection."""
    global blown_out
    step = 0  # Background gradient step

    # Start audio listening in a separate thread
    audio_thread = threading.Thread(target=audio_listener, daemon=True)
    audio_thread.start()

    # Capture from webcam
    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Resize frame
        frame = cv2.resize(frame, (640, 480))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        if not blown_out:
            draw_face_background(frame, faces)
            draw_candle(frame, blown_out)
            draw_snowfall(frame)
        else:
            # Animated greeting text
            cv2.putText(frame, "Merry Christmas and", (20, 200), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)
            cv2.putText(frame, "Happy New Year 2025!", (20, 260), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)
            draw_glittering_flowers(frame)

        # Show the frame
        cv2.imshow('Festive Candle', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
