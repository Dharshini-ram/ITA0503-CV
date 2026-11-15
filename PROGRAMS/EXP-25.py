import cv2

watch_cascade = cv2.CascadeClassifier(
    r"C:\Users\Dharshini\CV-exp\watch_cascade.xml"
)

if watch_cascade.empty():
    print("Cascade file not found!")
    exit()

image = cv2.imread(r"C:\Users\Dharshini\Downloads\WATCH.webp")

if image is None:
    print("Image not found!")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

watches = watch_cascade.detectMultiScale(gray, 1.1, 5)

for (x, y, w, h) in watches:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Watch Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()