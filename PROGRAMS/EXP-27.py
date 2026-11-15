


import cv2
import os

def detect_faces(image_path):

    # Get OpenCV Haar Cascade path
    cascade_path = os.path.join(
        cv2.__path__[0],
        "data",
        "haarcascade_frontalface_default.xml"
    )

    print("Cascade file location:", cascade_path)

    # Load cascade file
    face_cascade = cv2.CascadeClassifier(cascade_path)

    if face_cascade.empty():
        print("Error: Cascade file not loaded!")
        return

    # Read image
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Image not found!")
        return

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Draw rectangles
    for (x, y, w, h) in faces:
        cv2.rectangle(
            image,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

    print("Number of faces detected:", len(faces))

    # Save result
    cv2.imwrite("face_detected.jpg", image)

    # Display result
    cv2.imshow("Face Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


detect_faces(
    r"C:\Users\Dharshini\Downloads\Stylish Duck with Flowers.jpg"
)