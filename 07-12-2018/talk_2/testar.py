import cv2

'''
Face Detector: Detects faces in a image
classifier: haarcascade_frontalface_default.xml from OpenCV library
'''

# load classifier
classifier = cv2.CascadeClassifier('E:\\Dropbox\\Empresa\\editais\\Palestra Jus Nov-2018\\codigo\\negao\\classifier\\cascade.xml')

# load image
img = cv2.imread(r"C:\Users\bratao\AppData\Local\Temp\tmp67loicew.jpg")

# convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


if img is None:
    raise ValueError("Nao existe")

# detect faces
faces = classifier.detectMultiScale(img, 1.3, 100)
print(faces)
# draw rectangles on image for every detected face
for (x,y,w,h) in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h), (255, 0, 0), 2)

# finally show image
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()