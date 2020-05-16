import cv2
import numpy as np

class FaceDetector:
    def __init__(self, cascade_file, scale_factor=1.2, min_neighbors=5, min_size=(30, 30)):
        self.scale_factor = scale_factor
        self.min_neighbors = min_neighbors
        self.min_size = min_size
        self.cascade = cv2.CascadeClassifier(cascade_file)


    def detect_faces(self, image):
        return [np.asarray(face).tolist() for face in self.cascade.detectMultiScale(
            image,
            scaleFactor=self.scale_factor,
            minNeighbors=self.min_neighbors,
            minSize=self.min_size
        )]

    def crop_face(self, image, target_dimensions, default_first=True):
        faces = self.detect_faces(image)
        if (len(faces) > 1 and default_first) or len(faces) is 1:
            x, y, w, h = faces[0]
            return cv2.resize(image[y:y+w, x:x+h], target_dimensions, interpolation=cv2.INTER_LINEAR)
        print("{numFaces} faces were found in image. Not cropping".format(numFaces=len(faces)))
        return None