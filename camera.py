import cv2
import threading
from config import Config


class Camera:
    def __init__(self):
        self.camera_capture = None
        self.frame = None
        self.is_running = False
        self.camera_process = None

    def process(self):
        while self.camera_capture.isOpened() and self.is_running:
            ret, frame = self.camera_capture.read()

            if not ret:
                self.stop()

            else:
                self.frame = frame.copy()

    def preview_generator(self):
        while self.is_running:
            if self.frame is not None:
                _, frame = cv2.imencode('.jpg', self.frame)
                frame = frame.tobytes()

                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    def setup_cap(self):
        self.camera_capture = cv2.VideoCapture(0)

        self.camera_capture.set(cv2.CAP_PROP_FRAME_WIDTH, Config.CAMERA_WIDTH)
        self.camera_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, Config.CAMERA_HEIGHT)
        self.camera_capture.set(cv2.CAP_PROP_FPS, Config.CAMERA_FPS)

    def start(self):
        self.camera_process = threading.Thread(target=self.process)

        self.is_running = True
        self.setup_cap()
        self.camera_process.start()

    def stop(self):
        self.is_running = False
        self.camera_capture.release()
