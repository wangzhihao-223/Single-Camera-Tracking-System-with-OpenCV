import cv2
import numpy as np

def integer_brightness_adjust(frame, adjustment):
    # Convert pixel values to integers
    frame_int = frame.astype(int)
    
    # Apply brightness adjustment to each pixel
    adjusted_frame_int = frame_int + adjustment
    
    # Limit pixel values to the range 0-255
    adjusted_frame_int[adjusted_frame_int < 0] = 0
    adjusted_frame_int[adjusted_frame_int > 255] = 255
    
    # Convert pixel values back to uint8 type
    adjusted_frame = adjusted_frame_int.astype(np.uint8)
    
    return adjusted_frame

# Open the camera
video_capture = cv2.VideoCapture(0)  # Use camera index 0 for the default camera

# Check if the camera opened successfully
if not video_capture.isOpened():
    print("Error: Unable to open camera.")
    exit()

# Read the first frame from the camera
ret, frame = video_capture.read()

# Check if the frame was read successfully
if not ret:
    print("Error: Unable to read the camera frame.")
    exit()

# Get the dimensions of the camera frame
height, width = frame.shape[:2]

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_video = cv2.VideoWriter('../output_video.avi', fourcc, 30, (width, height))

# Process each frame from the camera
while True:
    # Adjust the brightness of the frame
    adjusted_frame = integer_brightness_adjust(frame, adjustment=50)
    
    # Write the adjusted frame to the output video
    output_video.write(adjusted_frame)

    # Display the adjusted frame
    cv2.imshow('float_Grey', adjusted_frame)
    
    # Check if the user pressed the 'q' key to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    # Read the next frame from the camera
    ret, frame = video_capture.read()
    
    # Check if the frame was read successfully
    if not ret:
        break

# Release camera and video objects
video_capture.release()
output_video.release()
cv2.destroyAllWindows()
