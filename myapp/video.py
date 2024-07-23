import requests
from imutils.video import VideoStream
import imutils
import cv2, os, urllib.request
import numpy as np
from django.conf import settings


class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, frame = self.video.read()
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()


class IPWebCam(object):
    def __init__(self, url):
        self.url = "http://192.168.0.100:8080/shot.jpg"

    def __del__(self):
        pass  # No need to explicitly close anything for this example

    def get_frame(self):
        try:
            # Request the JPEG image from the IP webcam URL
            response = requests.get(self.url)
            if response.status_code == 200:
                # Convert the raw bytes to a NumPy array
                image_array = np.array(bytearray(response.content), dtype=np.uint8)
                # Decode the array to OpenCV format
                frame = cv2.imdecode(image_array, -1)
                # Encode frame as JPEG
                ret, jpeg = cv2.imencode('.jpg', frame)
                return jpeg.tobytes()
            else:
                print(f"Error accessing IP webcam URL: Status code {response.status_code}")
        except Exception as e:
            print(f"Error getting frame from IP webcam: {e}")
        return None
