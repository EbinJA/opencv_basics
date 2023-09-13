import cv2
import numpy as np

# Load the input video
input_video = cv2.VideoCapture('dog_video.mp4')

# Define raindrop parameters
raindrop_length = 20
raindrop_thickness = 1
num_raindrops = 100

while input_video.isOpened():
    ret, frame = input_video.read()
    if not ret:
        break

    # Create an empty black image for rain
    rain = np.zeros_like(frame)

    # Generate random raindrops and overlay them on the rain image
    for _ in range(num_raindrops):
        x = np.random.randint(0, frame.shape[1])
        y = np.random.randint(0, frame.shape[0])
        cv2.line(rain, (x, y), (x, y + raindrop_length), (255, 255, 255), raindrop_thickness)

    # Add rain to the frame
    result = cv2.add(frame, rain)

    # Display or save the result
    cv2.imshow('Rainy Video', result)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release video and close window
input_video.release()
cv2.destroyAllWindows()
