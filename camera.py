import cv2
import threading
import os
import api_utils
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

    def record_video(self, length, output_dir, timestamp):
        self.setup_cap(Config.VIDEO_CAMERA_WIDTH, Config.VIDEO_CAMERA_HEIGHT, Config.VIDEO_CAMERA_FPS)
        start_time = timestamp

        if self.camera_capture.isOpened():
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            output = os.path.join(output_dir, f"{timestamp}.mp4")

            frame_size = (self.camera_capture.get(cv2.CAP_PROP_FRAME_WIDTH), self.camera_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
            frame_size = tuple(map(int, frame_size))

            writer = cv2.VideoWriter(output, fourcc, self.camera_capture.get(cv2.CAP_PROP_FPS), frame_size)

            while int(api_utils.generate_timestamp() - start_time) < length:
                ret, frame = self.camera_capture.read()

                if ret:
                    writer.write(frame)
                else:
                    break

            writer.release()
            self.camera_capture.release()

    def start(self):
        self.camera_process = threading.Thread(target=self.process)

        self.is_running = True
        self.setup_cap(Config.PREVIEW_CAMERA_WIDTH, Config.PREVIEW_CAMERA_HEIGHT, Config.PREVIEW_CAMERA_FPS)
        self.camera_process.start()

    def stop(self):
        self.is_running = False
        self.camera_capture.release()
