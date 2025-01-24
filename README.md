# Face Recognition Attendance System

This project implements a Face Recognition Attendance System using Python, OpenCV, and the `face_recognition` library. It captures video from a webcam, identifies faces based on pre-encoded images, and marks attendance in a CSV file.

---

## Features
- Real-time face detection and recognition using a webcam.
- Pre-trained face encodings for known individuals.
- Automatically marks attendance with a timestamp in a CSV file.
- Detects and handles unknown faces.

---

## Prerequisites

### Libraries Used:
- `cmake`
- `dlib`
- `face_recognition`
- `cv2` (OpenCV)
- `numpy`

### Hardware Requirements:
- A webcam for real-time video capture.

---


## How It Works

1. **Face Encoding:**
   - The script reads images from the `students` folder and generates face encodings using the `face_recognition` library.

2. **Real-Time Detection:**
   - The webcam feed is processed frame by frame to detect faces.
   - Detected faces are compared with the pre-computed encodings to identify individuals.

3. **Attendance Marking:**
   - If a recognized face is detected, their name and the current timestamp are logged in `sheet.csv`.

4. **Visualization:**
   - Bounding boxes and names are displayed on the webcam feed for identified individuals.

---

## Output
- A real-time video feed showing recognized faces with names.
- A `sheet.csv` file containing attendance records.

---

## Sample Output in `sheet.csv`:
```
Name,Timestamp
Gurmehar,14:35:21
Joe Biden,14:36:45
Hitesh,14:37:10
```

---

## Notes
- Ensure all images in the `students` folder contain clear frontal views of faces.
- If a face is not detected in an image, the script will terminate with a message.

---

## Future Enhancements
- Integrate with a database for better data management.
- Add GUI for user-friendly interaction.
- Extend support for multiple cameras.
- Implement notification systems for marked attendance.

---

