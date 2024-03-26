import cv2 as cv
import numpy as np
import os

data_folder_path = "D:\\opencv\\dataset"
dirs = os.listdir(data_folder_path)

face_regions = []
labels = []

# Load the pre-trained Haar Cascade classifier
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Mapping names to IDs
label_map = {}
current_id = 0

for dir_name in dirs:
    if dir_name not in label_map:
        label_map[dir_name] = current_id
        current_id += 1

    label_id = label_map[dir_name]
    subject_dir_path = data_folder_path + '\\' + dir_name
    subject_images_names = os.listdir(subject_dir_path)

    for image_name in subject_images_names:
        image_path = subject_dir_path + "/" + image_name
        image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)

        detected_faces = face_cascade.detectMultiScale(
            image, 
            scaleFactor=1.1, 
            minNeighbors=5, 
            minSize=(30, 30)
        )

        if len(detected_faces) == 0:
            print(f"No face detected in {image_path}")
            continue

        (x, y, w, h) = detected_faces[0]
        face_region = image[y:y+h, x:x+w]

        face_regions.append(face_region)
        labels.append(label_id)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.train(face_regions, np.array(labels))

test_img_path = 'D:\\opencv\\230508123210-01-how-to-watch-trump-town-hall.jpg'
test_img = cv.imread(test_img_path, 0)

faces = face_cascade.detectMultiScale(test_img, scaleFactor=1.1, minNeighbors=4, minSize=(20, 20))
if len(faces) > 0:
    (x, y, w, h) = faces[0]
    test_face = test_img[y:y+h, x:x+w]
    id, confidence = face_recognizer.predict(test_face)
    predicted_name = [name for name, label in label_map.items() if label == id][0]
    print(predicted_name)  # This will print the name of the recognized face
else:
    print("No faces detected.")
