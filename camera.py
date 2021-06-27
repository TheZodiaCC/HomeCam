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

    def setup_cap(self, width, height, fps):
        self.camera_capture = cv2.VideoCapture(0)

        self.camera_capture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.camera_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        self.camera_capture.set(cv2.CAP_PROP_FPS, fps)

    def take_picture(self):
        self.setup_cap(Config.PICTURE_CAMERA_WIDTH, Config.PICTURE_CAMERA_HEIGHT, 1)

        _, self.frame = self.camera_capture.read()

        self.camera_capture.release()

    def start(self):
        self.camera_process = threading.Thread(target=self.process)

        self.is_running = True
        self.setup_cap(Config.PREVIEW_CAMERA_WIDTH, Config.PREVIEW_CAMERA_HEIGHT, Config.PREVIEW_CAMERA_FPS)
        self.camera_process.start()

    def stop(self):
        self.is_running = False
        self.camera_capture.release()
